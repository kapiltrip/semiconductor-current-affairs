# Semiconductor Current Affairs Daily Notebook

This repository is for tracking semiconductor, VLSI, chip-design, fabrication, packaging, equipment, policy, and market current affairs.

The main goal is to create a daily study notebook: every date gets one Markdown file with newspaper/editorial images, source snippets, discussion notes, concept review, VLSI relevance, and interview-ready questions.

The goal is not to collect every article. The goal is to build discussion-ready knowledge: what happened, why it matters, which companies or countries are affected, and what technical or business question it raises.

## How To Use This Repo

### Daily, 20-30 minutes

1. Create or open today's folder at `YYYY-MM-DD/README.md`.
2. Put news screenshots, editorials, or snippets in `images/YYYY-MM-DD/`.
3. Add every screenshot filename and source URL to `images/YYYY-MM-DD/links.md`.
4. Add the image links at the top of the daily file.
5. Write the discussion below the images:
   - What happened?
   - Why does it matter?
   - Is it local/India news, international news, or both?
   - Which semiconductor segment is involved?
   - What VLSI concept should I revise?
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

2026-06-16/
  README.md

2026-06-17/
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

## Note Quality Standard

Every good note should answer:

1. What happened?
2. Why does it matter?
3. Is this local/India, international, or both?
4. Which part of the semiconductor value chain is affected?
5. What technical concept should I learn from this?
6. What definition, example, and question should I revise later?

## Daily File Format

Each daily file should follow this shape:

```text
Title and date
Images / newspaper snippets
Source links
Discussion
News coverage mix: local / international
VLSI relevance
Concept review table
India relevance
Key terms
Questions to revise
What to follow next
```

## Concept Review Standard

Each daily file should include a concept-review table. Keep it short, but make it useful for revision.

| Concept | Quick Definition | Why It Matters In This News | Revise Next |
|---|---|---|---|
| HBM | Stacked high-bandwidth DRAM used close to AI accelerators. | AI chip performance is limited by memory bandwidth. | DRAM vs HBM, bandwidth, packaging. |

Use this section for concepts like HBM, CoWoS, OSAT, ATMP, GAA, EUV, DFT, STA, RTL, interposer, yield, PDK, export controls, and foundry economics.

Images should live under `images/YYYY-MM-DD/`. From a daily page such as `2026-06-17/README.md`, link an image like this:

```markdown
![News Screenshot 1](../images/2026-06-17/news-01.png)
```

## Screenshot Rule

Screenshots should capture the headline, date, source name, and short visible snippet only. Do not save full article pages or full newspaper/editorial text. The daily note should contain your own summary and discussion, with the source link for reading.

## Current Status

This repository is intended to be versioned with git and pushed to GitHub after the initial local commit.
