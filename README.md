# Semiconductor Current Affairs Daily Notebook

This repository is for tracking semiconductor, VLSI, chip-design, fabrication, packaging, equipment, policy, and market current affairs.

The main goal is to create a daily study notebook: every date gets one Markdown file with embedded newspaper/editorial reference images, source snippets, full original editorial-style analysis, concept review, VLSI relevance, and interview-ready questions.

The goal is not to collect every article. The goal is to build discussion-ready knowledge: what happened, why it matters, which companies or countries are affected, and what technical or business question it raises.

## Study Navigation

- [Daily index](#daily-index): open any date from 2026-06-16 through 2026-08-08.
- [A-Z technical-term index](knowledge-base/glossary.md): open a definition, its source, and every day where the term is taught.
- [Semiconductor industry map](knowledge-base/industry-map.md): place each story in the value chain.
- [India semiconductor tracker](knowledge-base/india-semiconductor-tracker.md): follow projects, policy, and ecosystem evidence.
- [Running news log](trackers/news-log.md): scan the chronological evidence ledger.

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
   - Which technical terms need an inline explanation and a page-end glossary entry?
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
YYYY-MM-DD/README.md          Daily study page with quick links and page-end term index
images/YYYY-MM-DD/            Saved source images and links.md manifest
knowledge-base/glossary.md    Master A-Z technical-term index
knowledge-base/               Industry map and India semiconductor tracker
briefings/2026/               Weekly synthesis
trackers/news-log.md           Chronological evidence ledger
templates/                     Reusable daily, story, and weekly formats
scripts/                       Index-maintenance utilities
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
| 2026-07-01 | [2026-07-01/README.md](2026-07-01/README.md) | [images/2026-07-01/links.md](images/2026-07-01/links.md) | Etched inference ASIC, NIO automotive AI, MEMS timing, SOX market concentration |
| 2026-07-02 | [2026-07-02/README.md](2026-07-02/README.md) | [images/2026-07-02/links.md](images/2026-07-02/links.md) | SK hynix NAND/packaging capex, Infineon Dresden fab, Micron-GM memory, Asian chip selloff |
| 2026-07-03 | [2026-07-03/README.md](2026-07-03/README.md) | [images/2026-07-03/links.md](images/2026-07-03/links.md) | Kioxia 332-layer NAND, FormFactor probe cards, Socionext A14 chiplet, memory equipment spending |
| 2026-07-04 | [2026-07-04/README.md](2026-07-04/README.md) | [images/2026-07-04/links.md](images/2026-07-04/links.md) | CG Semi commercial-production milestone, India OSAT qualification, Infineon digital fab, Cadence verification agents |
| 2026-07-05 | [2026-07-05/README.md](2026-07-05/README.md) | [images/2026-07-05/links.md](images/2026-07-05/links.md) | CG Semi first shipment, G1/G2 capacity arithmetic, India production count, PQC secure-chip watch |
| 2026-07-06 | [2026-07-06/README.md](2026-07-06/README.md) | [images/2026-07-06/links.md](images/2026-07-06/links.md) | SK hynix U.S. offering, Samsung profit forecast, TSMC earnings watch, memory-allocation policy |
| 2026-07-07 | [2026-07-07/README.md](2026-07-07/README.md) | [images/2026-07-07/links.md](images/2026-07-07/links.md) | Samsung Q2 guidance, SIA May sales record, TSMC quiet period, India Semicon 2.0, SK hynix offering watch |
| 2026-07-08 | [2026-07-08/README.md](2026-07-08/README.md) | [images/2026-07-08/links.md](images/2026-07-08/links.md) | Samsung PM1763 PCIe 6.0 SSD, memory-stock volatility, SK hynix ADR demand, TSMC/SIA/ISM watch |
| 2026-07-09 | [2026-07-09/README.md](2026-07-09/README.md) | [images/2026-07-09/links.md](images/2026-07-09/links.md) | Micron-GlobalWafers wafer supply, SK hynix oversubscription, Apple-Broadcom U.S. chips, Meta Iris watch, TSMC/ISM pending |
| 2026-07-10 | [2026-07-10/README.md](2026-07-10/README.md) | [images/2026-07-10/links.md](images/2026-07-10/links.md) | SK hynix Nasdaq trading launch, SKHYV-to-SKHY mechanics, TSMC June-sales delay, India OSAT/Semicon 2.0 watch |
| 2026-07-11 | [2026-07-11/README.md](2026-07-11/README.md) | [images/2026-07-11/links.md](images/2026-07-11/links.md) | SK hynix first-day outcome, TSMC/ASML earnings-week setup, India Semicon 2.0 official-watch, follow-up cleanup |
| 2026-07-12 | [2026-07-12/README.md](2026-07-12/README.md) | [images/2026-07-12/links.md](images/2026-07-12/links.md) | India AI-semiconductor design talent, ASML Q2 checkpoint, TSMC July 13 revenue watch, SK hynix settlement, SEMICON India |
| 2026-07-13 | [2026-07-13/README.md](2026-07-13/README.md) | [images/2026-07-13/links.md](images/2026-07-13/links.md) | TSMC June revenue, India USD 350B consumption forecast, helium materials risk, SK hynix regular-way trading |
| 2026-07-14 | [2026-07-14/README.md](2026-07-14/README.md) | [images/2026-07-14/links.md](images/2026-07-14/links.md) | Intel Leixlip capacity, Submer MP liquid cooling/data centers, Nvidia compliance, China IC export-value interpretation |
| 2026-07-15 | [2026-07-15/README.md](2026-07-15/README.md) | [images/2026-07-15/links.md](images/2026-07-15/links.md) | ASML Q2 results, EUV/DUV capacity plans, India Semicon 2.0, design/materials/ATMP/talent pillars |
| 2026-07-16 | [2026-07-16/README.md](2026-07-16/README.md) | [images/2026-07-16/links.md](images/2026-07-16/links.md) | TSMC Q2 results, 2 nm revenue share, Q3 guidance, Arizona/capex expansion, market expectations risk |
| 2026-07-17 | [2026-07-17/README.md](2026-07-17/README.md) | [images/2026-07-17/links.md](images/2026-07-17/links.md) | Global AI/chip-stock selloff, SOX drawdown, memory volatility, capex-intensity debate, Semicon 2.0 follow-up |
| 2026-07-18 | [2026-07-18/README.md](2026-07-18/README.md) | [images/2026-07-18/links.md](images/2026-07-18/links.md) | Weekend synthesis: TSMC A14 roadmap, chip-index bear market, Moonshot Kimi K3, Semicon 2.0/MPMS Telangana follow-up |
| 2026-07-19 | [2026-07-19/README.md](2026-07-19/README.md) | [images/2026-07-19/links.md](images/2026-07-19/links.md) | Semicon 2.0 design co-investment, IEEE ITC India DFT/test agenda, SK hynix chipflation and U.S.-fab watch |
| 2026-07-20 | [2026-07-20/README.md](2026-07-20/README.md) | [images/2026-07-20/links.md](images/2026-07-20/links.md) | TSMC Arizona ramp and physical constraints, Rapidus-Cadence agentic EDA, ITC India career follow-up |
| 2026-07-21 | [2026-07-21/README.md](2026-07-21/README.md) | [images/2026-07-21/links.md](images/2026-07-21/links.md) | AMD-Microsoft Helios, memory contract risk, China/Korea memory rotation, India equipment components |
| 2026-07-22 | [2026-07-22/README.md](2026-07-22/README.md) | [images/2026-07-22/links.md](images/2026-07-22/links.md) | NVIDIA-Wistron U.S. AI-system manufacturing, AMD Advancing AI setup, TSMC 2027 price reports, China export-control watch, Paras MP OSAT |
| 2026-07-23 | [2026-07-23/README.md](2026-07-23/README.md) | [images/2026-07-23/links.md](images/2026-07-23/links.md) | Alphabet AI capex, Supermicro AI-server margin signal, AMD/Intel proof-point watch, NVIDIA Japan sovereign AI, SEMI equipment forecast, Paras OSAT process detail |
| 2026-07-24 | [2026-07-24/README.md](2026-07-24/README.md) | [images/2026-07-24/links.md](images/2026-07-24/links.md) | AMD Helios/MI400 launch, AMD-Cerebras disaggregated inference, Intel Q2/Foundry/equipment signal, Tesla chipmaking, China AI-chip self-reliance, Paras MP OSAT follow-up |
| 2026-07-25 | [2026-07-25/README.md](2026-07-25/README.md) | [images/2026-07-25/links.md](images/2026-07-25/links.md) | Samsung-Broadcom memory/foundry/packaging MOU, SK-NVIDIA AI factory/HBM, NAVER-NVIDIA-Brookfield Korea AI infrastructure, SK hynix CTI NAND, India Nano semiconductor track |
| 2026-07-26 | [2026-07-26/README.md](2026-07-26/README.md) | [images/2026-07-26/links.md](images/2026-07-26/links.md) | Sunday catch-up: official TSMC/AMD/Intel checks, Korea AI-stack consolidation, BTS Electro-Semicon, KWIN City semiconductor park, AI-chip cycle watch |
| 2026-07-27 | [2026-07-27/README.md](2026-07-27/README.md) | [images/2026-07-27/links.md](images/2026-07-27/links.md) | CXMT Shanghai debut, Synopsys-NVIDIA agentic EDA at DAC, NVIDIA Vera CPU for EDA, DAC heterogeneous integration, earnings checkpoint queue, SEMICON India ecosystem follow-up |
| 2026-07-28 | [2026-07-28/README.md](2026-07-28/README.md) | [images/2026-07-28/links.md](images/2026-07-28/links.md) | Cadence Q2 EDA results, Amkor Q2 packaging/test results, China DUV/CXMT pressure, SIA U.S. investment tracker, NXP/KLA/Lam/SK hynix evidence queue, India Semicon 2.0 follow-up |
| 2026-07-29 | [2026-07-29/README.md](2026-07-29/README.md) | [images/2026-07-29/links.md](images/2026-07-29/links.md) | SK hynix Q2 memory/HBM4 result, NXP Q2 physical-AI and SDV recovery, KLA Q4 process-control result, Lam/Samsung pending checkpoints, Intel 18A-P/14A EDA enablement, CXMT policy pressure, India Semicon 2.0 execution watch |
| 2026-07-30 | [2026-07-30/README.md](2026-07-30/README.md) | [images/2026-07-30/links.md](images/2026-07-30/links.md) | Samsung Q2 memory/foundry checkpoint, Lam June-quarter WFE result, Qualcomm input-cost pressure, Arm AI data-center IP, Amkor packaging/test context, DAC EDA close, CXMT policy watch, SEMICON India execution |
| 2026-07-31 | [2026-07-31/README.md](2026-07-31/README.md) | [images/2026-07-31/links.md](images/2026-07-31/links.md) | Microsoft Azure capacity and AI capex, Amazon Trainium/Graviton custom silicon, Apple memory-cost pressure, Samsung IR HBM4E/SOCAMM2 follow-up, Arm AI infrastructure CPU/IP, India talent pipeline, chip-stock rebound and CXMT policy watch |
| 2026-08-01 | [2026-08-01/README.md](2026-08-01/README.md) | [images/2026-08-01/links.md](images/2026-08-01/links.md) | Weekend catch-up: Korea chip-export surge, CXL memory expansion, Linde fab gases, Renesas/SkyWater manufacturing shifts, Cadence-Samsung EDA/IP, ASIP India OSAT watch, CXMT/YMTC policy pressure |
| 2026-08-02 | [2026-08-02/README.md](2026-08-02/README.md) | [images/2026-08-02/links.md](images/2026-08-02/links.md) | Sunday catch-up: ASIP Visakhapatnam OSAT foundation proof, FMS memory/storage setup, Apacer allocation warning, Nvidia financing risk, China DUV/ASML export-control watch, Bengaluru India Nano, CXMT/YMTC policy status |
| 2026-08-03 | [2026-08-03/README.md](2026-08-03/README.md) | [images/2026-08-03/links.md](images/2026-08-03/links.md) | Kioxia XL1 CXL memory expansion, Socionext-imec autonomous-edge chiplets, onsemi/Advanced Energy/AMD earnings checkpoints, Bengaluru India Nano opening, Qnity/Entegris materials watch, CSIS EDA export controls, MediaTek AI-chip financing report, SEMICON West Phoenix catch-up |
| 2026-08-04 | [2026-08-04/README.md](2026-08-04/README.md) | [images/2026-08-04/links.md](images/2026-08-04/links.md) | AMD Q2 record data-center result, onsemi and Advanced Energy Q2 proof updates, Microchip-Micron PCIe 6 storage, Marvell AI memory infrastructure, Kioxia FMS flash storage, Qnity materials, India Nano/C-VISTA |
| 2026-08-05 | [2026-08-05/README.md](2026-08-05/README.md) | [images/2026-08-05/links.md](images/2026-08-05/links.md) | Infineon AI data-center power, GlobalFoundries silicon photonics and RISC-V/IP, Samsung zHBM/zNAND-O, SEMI AI manufacturing, reported optical-transceiver policy risk, Karnataka nano roadmap, AMD expectation-risk follow-up |
| 2026-08-06 | [2026-08-06/README.md](2026-08-06/README.md) | [images/2026-08-06/links.md](images/2026-08-06/links.md) | Sandisk and WD storage earnings, Astera AI fabric switches, SK hynix-Sandisk HBF standard, SEMI/NVMe standards, China countermeasures and optical-policy risk, SpaceX-Nvidia market signal, SEMICON India Hackathon |
| 2026-08-07 | [2026-08-07/README.md](2026-08-07/README.md) | [images/2026-08-07/links.md](images/2026-08-07/links.md) | SIA Q2 global sales surge, MKS equipment and packaging demand, AOI 800G optics, Silicon Motion MonTitan, Himax CPO, SiTime timing, policy status, TSMC follow-up, India workforce |
| 2026-08-08 | [2026-08-08/README.md](2026-08-08/README.md) | [images/2026-08-08/links.md](images/2026-08-08/links.md) | Weekend catch-up: SK hynix fab capex, ACM equipment/ECP, Microchip recovery, optical/InP policy risk, Nvidia-China access reporting, GF India support hub, Ceva/TSMC proof queue |

## Note Quality Standard

Every good note should answer:

1. What happened?
2. Why does it matter?
3. Is this local/India, international, or both?
4. Which part of the semiconductor value chain is affected?
5. What technical concept should I learn from this?
6. What technical terms appeared, and can I jump to their meanings from the page index?
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

When a technical term first appears in a daily note, define it inline when the surrounding argument needs the meaning immediately. Every daily note must also finish with a clickable `Technical Terms Used Today` section, and every entry must link to the master A-Z glossary. This gives both context while reading and fast revision at the end.

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

Daily notes are reviewed through 2026-08-08. All 54 pages have clickable page navigation and end-of-page technical-term indexes, while the master glossary canonicalizes repeated terms and links back to the relevant days. Source manifests and readable headline/source screenshots, official source images, or clearly labeled generated metadata reference cards are included where available. Full article/editorial bodies are not duplicated; the daily notes use original study explanations with source links. July 18 is text-link-only because clean screenshot capture was blocked or timed out; July 19-August 8 use generated reference cards after browser capture proved unreliable, and the cards explicitly state that they are not webpage screenshots.
