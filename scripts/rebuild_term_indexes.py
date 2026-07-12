"""Rebuild the project-wide glossary and page-end term indexes.

The daily notes remain the source of truth for day-specific definitions. This
script collects their explicit ``Term:`` / ``Definition:`` pairs (or the early
notes' Concept Review rows), canonicalizes common aliases, and writes:

* a clickable navigation strip on every daily page;
* a concise, linked glossary at the end of every daily page; and
* the master A-Z glossary with backlinks to every day where a term is taught.

Run from the repository root with ``python scripts/rebuild_term_indexes.py``.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


CORE_TERMS: dict[str, tuple[str, str]] = {
    "ASIC": (
        "An application-specific integrated circuit is a chip built for a defined workload rather than general-purpose programming. Specialization can improve performance and energy efficiency, but raises design cost and reduces flexibility.",
        "https://www.arm.com/glossary/asic",
    ),
    "ATMP": (
        "Assembly, testing, marking, and packaging covers the post-fabrication work that turns wafer dies into identified, qualified, shippable semiconductor products. India policy often uses ATMP where international industry language may use OSAT.",
        "https://www.ism.gov.in/",
    ),
    "DFT": (
        "Design for testability adds structures such as scan chains, test access, and built-in self-test so manufacturing defects can be detected after a chip is fabricated. Good DFT raises test coverage while controlling test time and cost.",
        "https://semiengineering.com/knowledge_centers/test/design-for-test/",
    ),
    "DLI": (
        "The Design Linked Incentive scheme is an Indian government program supporting semiconductor design companies through design infrastructure and financial incentives intended to help domestic designs reach commercial products.",
        "https://chips-dli.gov.in/",
    ),
    "DUV lithography": (
        "Deep-ultraviolet lithography uses 193 nm or 248 nm light to transfer circuit patterns from a mask onto photoresist-coated wafers. It remains essential across mature and advanced processes; advanced nodes may require repeated DUV patterning where one EUV exposure can sometimes reduce the step count.",
        "https://www.asml.com/en/technology/lithography-principles",
    ),
    "EDA": (
        "Electronic design automation is the software and methodology stack used to design, simulate, verify, implement, and sign off integrated circuits. It lets engineering teams manage designs containing millions or billions of transistors with repeatable checks.",
        "https://www.synopsys.com/glossary/what-is-electronic-design-automation.html",
    ),
    "Fab": (
        "A semiconductor fabrication plant processes wafers through repeated deposition, lithography, etch, implantation, cleaning, and metrology steps to build integrated circuits. A fab is front-end manufacturing; assembly and final test happen later.",
        "https://www.semi.org/en/resources/semiconductor101",
    ),
    "Fabless": (
        "A fabless company designs and sells chips but contracts wafer manufacturing to a foundry. This model avoids owning a capital-intensive fab but makes process portability, capacity agreements, packaging, and supplier execution strategically important.",
        "https://www.semi.org/en/resources/semiconductor101",
    ),
    "GAA": (
        "A gate-all-around transistor places the gate around the channel on multiple sides, improving electrostatic control compared with a FinFET as dimensions shrink. Commercial versions commonly use stacked nanosheet channels.",
        "https://www.samsung.com/semiconductor/minisite/tech/gate-all-around/",
    ),
    "IDM": (
        "An integrated device manufacturer designs and manufactures at least some of its own semiconductor products. The model provides tighter design-process control but requires sustained investment in fabs, tools, process R&D, yield, and capacity.",
        "https://www.semi.org/en/resources/semiconductor101",
    ),
    "Lithography": (
        "Lithography is the chip-patterning process: light projects a mask pattern onto light-sensitive photoresist on a wafer, after which etch or deposition transfers that pattern into a material layer. A modern chip needs many aligned lithography steps; smaller wavelengths and tighter process control enable denser features.",
        "https://www.asml.com/en/technology/lithography-principles",
    ),
    "Node": (
        "A process node is the name for a semiconductor manufacturing generation, such as 5 nm, 3 nm, or 2 nm. Modern node numbers are comparative technology labels rather than the direct measurement of one transistor feature.",
        "https://irds.ieee.org/",
    ),
    "OSAT": (
        "An outsourced semiconductor assembly and test provider receives fabricated wafers or dies, packages them, performs electrical and reliability tests, and ships qualified parts. OSAT is a business/manufacturing role; ATMP names the corresponding activity set often used in India.",
        "https://www.semi.org/en/resources/semiconductor101",
    ),
    "RTL": (
        "Register-transfer level is a digital design abstraction describing registers, combinational logic, and the data transfers that occur on clock events. RTL is commonly written in Verilog, SystemVerilog, or VHDL and then synthesized into gates.",
        "https://www.synopsys.com/glossary/what-is-register-transfer-level.html",
    ),
    "Semiconductor": (
        "A semiconductor is a material whose electrical conductivity can be controlled, enabling devices such as diodes and transistors. In this project the word also refers broadly to the industry that designs, fabricates, packages, tests, and supplies integrated circuits.",
        "https://www.semi.org/en/resources/semiconductor101",
    ),
    "Tape-out": (
        "Tape-out is the controlled release of a completed chip-design database to the foundry for mask preparation and fabrication. It proves design handoff, not working silicon: manufacturing, packaging, bring-up, validation, qualification, and yield ramp still follow.",
        "https://semiengineering.com/knowledge_centers/eda-design/definitions/tape-out/",
    ),
    "VLSI": (
        "Very-large-scale integration is the design and manufacture of integrated circuits containing very large numbers of transistors on one die or system. In practice, VLSI work spans architecture, RTL, verification, DFT, physical design, signoff, and silicon validation.",
        "https://www.computer.org/",
    ),
    "Wafer": (
        "A wafer is a thin, polished disc of semiconductor material on which many chip dies are fabricated in parallel. Its diameter, crystal quality, defect density, and process uniformity strongly affect manufacturing cost and yield.",
        "https://www.semi.org/en/resources/semiconductor101",
    ),
    "WFE": (
        "Wafer fabrication equipment is the tool category used to manufacture wafers, including lithography, deposition, etch, cleaning, ion implantation, metrology, inspection, and process-control systems. Spending becomes output only after installation, qualification, and yield ramp.",
        "https://www.semi.org/en/market-data",
    ),
    "Yield": (
        "Manufacturing yield is the share of fabricated dies or packaged devices that meet required electrical, functional, performance, and reliability specifications. Higher yield lowers cost per good chip; a capacity announcement without qualified yield does not prove saleable output.",
        "https://www.semi.org/en/resources/semiconductor101",
    ),
}


ALIASES = {
    "american depositary receipt": "American Depositary Receipt (ADR)",
    "american depositary receipt (adr)": "American Depositary Receipt (ADR)",
    "american depositary share (ads) and american depositary receipt (adr)": "American Depositary Receipt (ADR)",
    "advanced packaging and test facility": "Advanced packaging",
    "capital expenditure": "Capital expenditure (capex)",
    "design linked incentive (dli)": "DLI",
    "electronic design automation": "EDA",
    "earnings quiet period": "Quiet period",
    "export control": "Export controls",
    "export-control compliance": "Export controls",
    "extreme ultraviolet (euv) lithography": "EUV lithography",
    "gate-all-around transistor": "GAA",
    "gaa / nanosheet": "GAA",
    "gaa / ribbonfet": "GAA",
    "hbm": "High-Bandwidth Memory (HBM)",
    "hbm (high bandwidth memory)": "High-Bandwidth Memory (HBM)",
    "high bandwidth memory": "High-Bandwidth Memory (HBM)",
    "high bandwidth memory (hbm)": "High-Bandwidth Memory (HBM)",
    "high-bandwidth memory": "High-Bandwidth Memory (HBM)",
    "high-bandwidth memory (hbm)": "High-Bandwidth Memory (HBM)",
    "nand flash memory": "NAND flash",
    "outsourced semiconductor assembly and test": "OSAT",
    "outsourced semiconductor assembly and test (osat)": "OSAT",
    "semiconductor design tools": "EDA",
    "system-on-chip": "System-on-chip (SoC)",
    "tapeout": "Tape-out",
}


def canonical(term: str) -> str:
    clean = re.sub(r"\s+", " ", term.strip()).rstrip(".")
    return ALIASES.get(clean.casefold(), clean)


def slug(value: str) -> str:
    value = value.casefold().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "term"


def strip_source(definition: str) -> tuple[str, str]:
    match = re.search(r"\s+Source:\s*(https?://\S+)\s*$", definition)
    if match:
        return definition[: match.start()].strip(), match.group(1).rstrip(".,)")
    markdown_match = re.search(
        r"\s+Source:\s*\[[^\]]+\]\((https?://[^)]+)\)\s*$", definition
    )
    if markdown_match:
        return definition[: markdown_match.start()].strip(), markdown_match.group(1)
    return definition.strip(), ""


def concise(definition: str) -> str:
    definition = re.sub(r"\s+", " ", definition).strip()
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", definition)
    result = " ".join(sentences[:2])
    if len(result) <= 520:
        return result
    return result[:517].rsplit(" ", 1)[0] + "..."


def table_safe(value: str) -> str:
    return value.replace("|", "&#124;").replace("\n", " ")


def parse_terms(text: str) -> list[tuple[str, str, str]]:
    found: list[tuple[str, str, str]] = []
    pattern = re.compile(r"^Term:\s*(.+?)\s*$\n^Definition:\s*(.+?)\s*$", re.MULTILINE)
    for match in pattern.finditer(text):
        definition, source = strip_source(match.group(2))
        found.append((canonical(match.group(1)), definition, source))
    if found:
        return found

    # The first six notes predate the Term/Definition convention. Their Concept
    # Review tables are the reviewed teaching source for the local glossary.
    concept_match = re.search(
        r"^## Concept Review\s*$([\s\S]*?)(?=^## |^### India Relevance)",
        text,
        re.MULTILINE,
    )
    if concept_match:
        for line in concept_match.group(1).splitlines():
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0] not in {"Concept", "---", ""}:
                found.append((canonical(cells[0]), cells[1], ""))
    return found


def heading_anchors(text: str) -> dict[str, str]:
    anchors: dict[str, str] = {}
    for heading in re.findall(r"^##\s+(.+?)\s*$", text, re.MULTILINE):
        anchors[heading.casefold()] = slug(heading)
    return anchors


def choose_anchor(anchors: dict[str, str], candidates: list[str]) -> tuple[str, str] | None:
    for candidate in candidates:
        if candidate.casefold() in anchors:
            return candidate, anchors[candidate.casefold()]
    return None


def add_or_refresh_navigation(text: str) -> str:
    text = re.sub(r"\n\*\*Page navigation:\*\*.*?\n", "\n", text)
    anchors = heading_anchors(text)
    source = choose_anchor(
        anchors,
        ["Source Map", "Source Snippets", "Source Images And Manifest", "Source Images", "News Images"],
    )
    analysis = choose_anchor(anchors, ["Discussion", "Confirmed Facts", "Analysis"])
    concept = choose_anchor(anchors, ["Concept Review"])
    follow = choose_anchor(
        anchors,
        ["What To Watch Next", "What To Follow Next", "Follow-Up Ledger", "Follow-Up"],
    )

    links: list[str] = []
    if source:
        links.append(f"[Sources](#{source[1]})")
    if analysis:
        links.append(f"[Main analysis](#{analysis[1]})")
    if concept:
        links.append(f"[Concept review](#{concept[1]})")
    if follow:
        links.append(f"[Follow-up](#{follow[1]})")
    links.append("[Technical terms](#technical-terms-used-today)")
    links.append("[Master glossary](../knowledge-base/glossary.md)")
    nav = "\n**Page navigation:** " + " · ".join(links) + "\n"

    quick = re.search(r"^## Quick Index\s*$", text, re.MULTILINE)
    if quick:
        next_heading = re.search(r"^##\s+", text[quick.end() :], re.MULTILINE)
        insert_at = quick.end() + (next_heading.start() if next_heading else 0)
        return text[:insert_at].rstrip() + "\n" + nav + "\n" + text[insert_at:].lstrip("\n")

    date_match = re.search(r"^Date:\s*.+?$", text, re.MULTILINE)
    insert_at = date_match.end() if date_match else text.find("\n")
    quick_block = (
        "\n\n## Quick Index\n\n"
        "Use the page navigation below to jump directly to evidence, explanation, revision, or definitions.\n"
    )
    return text[:insert_at] + quick_block + nav + "\n" + text[insert_at:].lstrip("\n")


def daily_glossary(terms: list[tuple[str, str, str]]) -> str:
    best: dict[str, tuple[str, str]] = {}
    for term, definition, source in terms:
        previous = best.get(term)
        if not previous or len(definition) > len(previous[0]):
            best[term] = (definition, source)

    ordered = sorted(best.items(), key=lambda item: item[0].casefold())
    index = " · ".join(
        f"[{term}](#daily-term-{slug(term)})" for term, _ in ordered
    )
    rows = []
    for term, (definition, _) in ordered:
        rows.append(
            "| "
            f'<a id="daily-term-{slug(term)}"></a>'
            f"[**{table_safe(term)}**](../knowledge-base/glossary.md#term-{slug(term)})"
            f" | {table_safe(concise(definition))} |"
        )

    return (
        "## Technical Terms Used Today\n\n"
        "[Back to quick index](#quick-index) · "
        "[Open the master A-Z glossary](../knowledge-base/glossary.md)\n\n"
        f"**Term index:** {index}\n\n"
        "| Term | Meaning |\n"
        "|---|---|\n"
        + "\n".join(rows)
        + "\n\n"
        "This page-end index covers the specialist terms central to this day's study. "
        "The fuller explanation, news context, and source remain at first use; the master glossary "
        "combines repeated terms across all days.\n"
    )


def build_master(
    definitions: dict[str, tuple[str, str]], appearances: dict[str, set[str]]
) -> str:
    def group_key(term: str) -> str:
        return term[0].upper() if term and term[0].isalpha() else "0-9"

    letters = sorted({group_key(term) for term in definitions if term}, key=lambda x: (x != "0-9", x))
    term_index = " · ".join(
        f"[{letter}](#letter-{slug(letter)})" for letter in letters
    )
    lines = [
        "# Semiconductor Technical-Term Index",
        "",
        "This is the master A-Z glossary for every specialist term indexed in the daily notes through "
        "**2026-07-12**. Each entry gives a usable meaning, an authoritative reference when available, "
        "and backlinks to the days where the term is taught in context.",
        "",
        "[Notebook home](../README.md) · [Daily index](../README.md#daily-index)",
        "",
        "## A-Z Index",
        "",
        term_index,
        "",
        "## How To Use This Glossary",
        "",
        "Start with the short meaning on a daily page. Use this master entry when the term repeats across "
        "stories or when you want its source and every related day. Acronyms and expanded names are "
        "canonicalized—for example, **HBM** and **High-Bandwidth Memory** point to one entry.",
        "",
    ]

    grouped: dict[str, list[str]] = defaultdict(list)
    for term in definitions:
        grouped[group_key(term)].append(term)

    for letter in letters:
        lines.extend([f'<a id="letter-{slug(letter)}"></a>', f"# {letter}", ""])
        for term in sorted(grouped[letter], key=str.casefold):
            definition, source = definitions[term]
            lines.extend(
                [
                    f'<a id="term-{slug(term)}"></a>',
                    f"## {term}",
                    "",
                    definition,
                    "",
                ]
            )
            days = sorted(appearances.get(term, set()))
            if days:
                day_links = ", ".join(
                    f"[{day}](../{day}/README.md#daily-term-{slug(term)})" for day in days
                )
                lines.extend([f"**Appears in:** {day_links}", ""])
            if source:
                lines.extend([f"**Reference:** {source}", ""])
            lines.extend(["[Back to A-Z index](#a-z-index)", ""])

    lines.extend(
        [
            "## Scope Note",
            "",
            "The index covers semiconductor, VLSI, manufacturing, packaging, equipment, memory, policy, "
            "and market terms that carry a specialist meaning in this notebook. Ordinary English words and "
            "company names are intentionally excluded. Add new terms to a daily note using the `Term:` and "
            "`Definition:` lines, then rerun `python scripts/rebuild_term_indexes.py`.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    daily_files = sorted(ROOT.glob("2026-??-??/README.md"))
    definitions: dict[str, tuple[str, str]] = dict(CORE_TERMS)
    appearances: dict[str, set[str]] = defaultdict(set)
    parsed_by_file: dict[Path, list[tuple[str, str, str]]] = {}

    for path in daily_files:
        original = path.read_text(encoding="utf-8")
        # Never parse the generated page-end summary as a second source.
        source_text = re.split(r"^## Technical Terms Used Today\s*$", original, maxsplit=1, flags=re.MULTILINE)[0]
        terms = parse_terms(source_text)
        parsed_by_file[path] = terms
        for term, definition, source in terms:
            appearances[term].add(path.parent.name)
            current = definitions.get(term)
            if current is None or len(definition) > len(current[0]):
                definitions[term] = (definition, source)

    for path, terms in parsed_by_file.items():
        text = path.read_text(encoding="utf-8")
        text = re.split(r"^## Technical Terms Used Today\s*$", text, maxsplit=1, flags=re.MULTILINE)[0].rstrip()
        text = add_or_refresh_navigation(text).rstrip()
        text += "\n\n" + daily_glossary(terms)
        path.write_text(text, encoding="utf-8", newline="\n")

    glossary = build_master(definitions, appearances)
    (ROOT / "knowledge-base" / "glossary.md").write_text(
        glossary, encoding="utf-8", newline="\n"
    )
    print(
        f"Updated {len(daily_files)} daily pages and indexed "
        f"{len(definitions)} canonical technical terms."
    )


if __name__ == "__main__":
    main()
