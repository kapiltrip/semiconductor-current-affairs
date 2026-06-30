# Semiconductor Current Affairs Daily Notebook

This repository is for tracking semiconductor, VLSI, chip-design, fabrication, packaging, equipment, policy, and market current affairs.

The main goal is to create a daily study notebook: every date gets one Markdown file with embedded newspaper/editorial reference images, source snippets, full original editorial-style analysis, concept review, VLSI relevance, and interview-ready questions.

The goal is not to collect every article. The goal is to build discussion-ready knowledge: what happened, why it matters, which companies or countries are affected, and what technical or business question it raises.

## How To Use This Repo

### Daily, 20-30 minutes

1. Create or open today's folder at `YYYY-MM-DD/README.md`.
2. Put news screenshots, related editorial reference images, or snippets in `images/YYYY-MM-DD/`.
3. Add every screenshot filename and source URL to `images/YYYY-MM-DD/links.md`.
4. Embed the relevant image links at the top of the daily file, before the explanation.
5. Write the full original discussion below the images:
   - What happened?
   - Why does it matter?
   - Is it local/India news, international news, or both?
   - Which semiconductor segment is involved?
   - What VLSI concept should I revise?
   - Which technical terms need next-line definitions?
   - What question could someone ask me?
6. Add only the most important items to `trackers/news-log.md`.

### Weekly, 45-60 minutes

1. Review the daily files from the week.
2. Create a weekly brief from `templates/weekly-brief.md`.
3. Update the relevant knowledge-base page.
4. Add 5-10 interview or discussion questions at the end of the weekly brief.

### Monthly, 2-3 hours

1. Review all weekly briefs.
2. Update the industry map, company notes, India tracker, and glossary.
3. Pick one deep-dive topic, such as advanced packaging, EUV lithography, HBM, export controls, or India OSAT/fab policy.

## Repo Structure

```text
images/
  README.md
  2026-06-16/
    links.md
  2026-06-17/
    links.md
  2026-06-18/
    links.md
  2026-06-19/
    links.md
  2026-06-20/
    links.md
  2026-06-21/
    links.md

2026-06-16/
  README.md

2026-06-17/
  README.md

2026-06-18/
  README.md

2026-06-19/
  README.md

2026-06-20/
  README.md

2026-06-21/
  README.md

briefings/
  2026/
    2026-06-17-weekly-brief.md

knowledge-base/
  glossary.md
  india-semiconductor-tracker.md
  industry-map.md

sources/
  semiconductor-news-sources.md

templates/
  daily-note.md
  news-note.md
  weekly-brief.md

trackers/
  news-log.md
```

## What To Track

- Local / India: India Semiconductor Mission, SEMICON India, state incentives, design startups, OSAT/ATMP, compound semiconductor projects, VLSI hiring and skilling.
- International: TSMC, Intel, Samsung, NVIDIA, ASML, export controls, China, Taiwan, US CHIPS Act, EU/Japan/Korea supply-chain policy.
- Market: global semiconductor sales, WSTS/SIA updates, memory cycles, foundry utilization, equipment spending.
- Technology: process nodes, EUV and High-NA EUV, GAA, backside power delivery, chiplets, HBM, advanced packaging, silicon photonics.
- Companies: TSMC, Samsung, Intel, NVIDIA, AMD, Broadcom, Qualcomm, Apple, ASML, Applied Materials, Lam Research, KLA, Synopsys, Cadence, Arm.
- India: India Semiconductor Mission, DLI, OSAT/ATMP, compound semiconductors, design startups, skilling, state incentives.
- Policy: US-China export controls, CHIPS Act, EU Chips Act, Japan/Korea/Taiwan incentives, supply-chain localization.
- VLSI career relevance: design verification, DFT, physical design, STA, RTL, EDA tools, packaging-aware design.

## Daily Index

| Date | Daily Note | Images / Links | Focus |
|---|---|---|---|
| 2026-06-16 | [2026-06-16/README.md](2026-06-16/README.md) | [images/2026-06-16/links.md](images/2026-06-16/links.md) | Intel 18A-P, TSMC CoWoS vs CoPoS, AMD-MEXT memory wall, SiMa physical AI |
| 2026-06-17 | [2026-06-17/README.md](2026-06-17/README.md) | [images/2026-06-17/links.md](images/2026-06-17/links.md) | TSMC-Amkor advanced packaging, Huawei/export controls, Intel market reaction, India SEMICON 2026 |
| 2026-06-18 | [2026-06-18/README.md](2026-06-18/README.md) | [images/2026-06-18/links.md](images/2026-06-18/links.md) | Intel Foundry leadership, SK hynix HBM4E, Amazon Trainium, Apple-Intel reported signal |
| 2026-06-19 | [2026-06-19/README.md](2026-06-19/README.md) | [images/2026-06-19/links.md](images/2026-06-19/links.md) | VLSI scaling paths, TSMC A16, Samsung 3D stacked FET, 2D materials, InP photonics, MLPerf |
| 2026-06-20 | [2026-06-20/README.md](2026-06-20/README.md) | [images/2026-06-20/links.md](images/2026-06-20/links.md) | Memory crunch, ASML/EUV export-control dispute, Intel packaging reset, SK hynix HBM4E, SEMICON India |
| 2026-06-21 | [2026-06-21/README.md](2026-06-21/README.md) | [images/2026-06-21/links.md](images/2026-06-21/links.md) | ASML/EUV China concern, AMD-Samsung foundry report, Intel packaging, memory crunch, SEMICON India |
| 2026-06-22 | [2026-06-22/README.md](2026-06-22/README.md) | [images/2026-06-22/links.md](images/2026-06-22/links.md) | Micron AI-memory expectations, AMD-Samsung foundry report, ASML China concern |
| 2026-06-23 | [2026-06-23/README.md](2026-06-23/README.md) | [images/2026-06-23/links.md](images/2026-06-23/links.md) | Memory-stock selloff, AI-chip slump, AMD-Samsung and ASML follow-ups |
| 2026-06-24 | [2026-06-24/README.md](2026-06-24/README.md) | [images/2026-06-24/links.md](images/2026-06-24/links.md) | Micron earnings watch, Cerebras earnings, Korea memory rebound, SEMICON India |
| 2026-06-25 | [2026-06-25/README.md](2026-06-25/README.md) | [images/2026-06-25/links.md](images/2026-06-25/links.md) | Micron record quarter, Qualcomm Dragonfly, OpenAI/Broadcom Jalapeno, Pax Silica |
| 2026-06-26 | [2026-06-26/README.md](2026-06-26/README.md) | [images/2026-06-26/links.md](images/2026-06-26/links.md) | IBM nanostack, Micron-Qualcomm rally, SK hynix ADR, Pax Silica, TSMC price pressure |
| 2026-06-27 | [2026-06-27/README.md](2026-06-27/README.md) | [images/2026-06-27/links.md](images/2026-06-27/links.md) | Apple memory-price pass-through, semiconductor inflation, AI inference-memory follow-up |
| 2026-06-28 | [2026-06-28/README.md](2026-06-28/README.md) | [images/2026-06-28/links.md](images/2026-06-28/links.md) | HBM-led memory supercycle, HBM4E packaging, MR-MUF, thermal/yield constraints |
| 2026-06-29 | [2026-06-29/README.md](2026-06-29/README.md) | [images/2026-06-29/links.md](images/2026-06-29/links.md) | Korea chip hub, Nvidia China pressure, AI-chip share rally, BCD-on-SOI power electronics |
| 2026-06-30 | [2026-06-30/README.md](2026-06-30/README.md) | [images/2026-06-30/links.md](images/2026-06-30/links.md) | Korea capex-cycle risk, AI-server MLCCs, Jewar PCB/ISM catch-up, June systems synthesis |

## Note Quality Standard

Every good note should answer:

1. What happened?
2. Why does it matter?
3. Is this local/India, international, or both?
4. Which part of the semiconductor value chain is affected?
5. What technical concept should I learn from this?
6. What technical terms appeared, and were they defined deeply on the next line?
7. What definition, example, and question should I revise later?

## Daily File Format

Each daily file should follow this shape:

```text
Title and date
Embedded source images / screenshots
Source links
Full original editorial/news discussion
Technical terms / deep cited definitions
News coverage mix: local / international
VLSI relevance
Concept review table
India relevance
Key terms
Questions to revise
What to follow next
```

## Concept Review Standard

Each daily file should include a concept-review table. Keep it short, but make it useful for revision. Definitions should be deep enough that the note saves a separate search later.

| Concept | Deep Definition | Why It Matters In This News | Revise Next | Source |
|---|---|---|---|---|
| HBM | High-Bandwidth Memory is stacked DRAM connected through dense vertical and package-level interconnects so an AI accelerator can access memory with much higher bandwidth than ordinary DIMM-style memory. The important idea is not only capacity; it is short, wide data movement close to the compute die, which reduces the memory bottleneck in training and inference workloads. | AI chip performance is limited by memory bandwidth. | DRAM vs HBM, TSVs, bandwidth, packaging. | https://www.jedec.org/ |

Use this section for concepts like HBM, CoWoS, OSAT, ATMP, GAA, EUV, DFT, STA, RTL, interposer, yield, PDK, export controls, and foundry economics.

## Technical Term Definition Standard

When a technical term first appears in a daily note, define it immediately in the next line. Do not only put all definitions at the end. The goal is that the note itself teaches the term at the point where it is needed.

Use this format:

```markdown
Term: EUV lithography
Definition: EUV lithography is a chip-patterning method that uses 13.5 nm extreme-ultraviolet light to print very small features on advanced wafers. It matters because shorter wavelength light can pattern smaller structures with fewer multi-patterning steps than older DUV flows, but EUV tools are extremely complex, expensive, and export-controlled because they are critical for leading-edge logic manufacturing. Source: https://www.asml.com/en/technology/lithography-principles
```

Good definitions should include:

- What the term means in plain language.
- What physical, circuit, manufacturing, business, or policy problem it solves.
- Why it matters in today's news.
- One example or comparison when useful, such as EUV vs DUV, HBM vs ordinary DRAM, or CoWoS vs EMIB.
- A citation from a reliable source. Prefer primary sources and standards bodies; use technical explainers only when primary sources are not readable.

Images should live under `images/YYYY-MM-DD/`. From a daily page such as `2026-06-17/README.md`, link an image like this:

```markdown
![News Screenshot 1](../images/2026-06-17/news-01.png)
```

## Screenshot And Editorial Coverage Rule

Include the relevant images/screenshots directly in the daily note before the explanation, so the visual source and study discussion stay together.

Saved screenshots should stay focused on source identification: headline, date, source name, and a short visible snippet.

Related editorials are welcome and should get complete original coverage in the daily note: explain the thesis, main arguments, evidence, counterpoints, semiconductor/VLSI relevance, India angle, and discussion questions. The note should be original study writing with the source link for reading, not a pasted article body or paywalled page capture.

## Current Status

Daily notes are created through 2026-06-30, with source manifests and readable headline/source screenshots captured where browser access allowed. Full article/editorial bodies are not duplicated; the daily notes use original study explanations with source links. The June 30 note uses verified text sources because the optional screenshot-capture dependency was unavailable.
