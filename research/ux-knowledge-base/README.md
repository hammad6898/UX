# UX Knowledge Base (for training and grounding the audit engine)

A structured, cited dataset of what a UX designer uses to audit an interface: heuristics, laws, standards, guidelines, cognitive biases, deceptive patterns, metrics, numeric thresholds, research methods and the core literature from 1908 to 2025.

It feeds the **Heuristic Library** described in [`docs/ARCHITECTURE.md`](../../docs/ARCHITECTURE.md). The `detection_layer` and `severity_default` columns use the same terms as the three analysis layers: deterministic, screen and flow.

## Files

| File | What it is |
|---|---|
| `UX_Knowledge_Base.xlsx` | The full workbook: 25 sheets, README sheet first |
| `ALL_RULES.csv` | Every rule/guideline row (10,386) in one flat table |
| `data/ALL_RULES.jsonl` | Same rows as JSON Lines (best for RAG, embeddings, fine-tuning prep) |
| `data/<source>.jsonl` | One file per source, same schema |
| `data/heuristic_sets_index.jsonl` | 53 heuristic sets (author, year, item count, citation) |
| `data/bibliography.jsonl` | 298 seminal papers, books, standards and laws (1908–2025) |
| `data/dark_pattern_instances.jsonl` | 4,174 labeled real-world dark-pattern texts |
| `data/manifest.json` | Row counts and licenses per source |
| `scripts/` | Extractors and curated sets; `run_all.sh` rebuilds everything |

## What's inside

| Sheet | Rows | Contents |
|---|---:|---|
| **Audit_Rules** | 157 | Product-ready rules (forms, navigation, search, content, visual, feedback, errors, mobile, onboarding/auth, e-commerce, trust/privacy, accessibility, AI/voice, data display, performance, i18n, motion, flows). Each has a check question, detection layer, default severity, applies-to, Nielsen/WCAG mapping and evidence |
| **Heuristics** + Heuristic_Sets | 429 / 53 | Complete heuristic sets: Nielsen 10 (1994) and Nielsen–Molich (1990), Shneiderman 8, Tognazzini, Gerhardt-Powals, Bastien & Scapin, ISO 9241-110/-112/-210/-11, Weinschenk & Barker, Mandel, Hansen 1971, Rams, Universal Design, Inclusive Design, GOV.UK principles (incl. 2025 addition) and Service Standard, Microsoft HAX 18, Google PAIR, Apple and Material principles, cognitive walkthrough, mobile (Bertini, SMASH), games (Pinelle, HEP), conversational agents (Langevin 2021), Grice, medical devices (Zhang 2003), visualization (Shneiderman, Tufte, Cleveland–McGill, Forsell–Johansson), Stanford credibility, Persuasive Systems Design, Privacy by Design, usable security, usability definitions (Nielsen 5, ISO, 5Es, honeycomb, Garrett), Krug, IA principles, microinteractions, error messages, UI states, VSD, POUR |
| **Laws_Principles** | 131 | Perception (Gestalt, Weber–Fechner, preattentive, banner/change/inattentional blindness, F-pattern), memory (Miller, Cowan, chunking, cognitive load, serial position, Zeigarnik), motor (Fitts, Hick–Hyman, steering, KLM, MHP, thumb zone), timing (0.1/1/10 s, Doherty, RAIL), decision-making (prospect theory, defaults, choice overload, Fogg, SDT, nudge, EAST, COM-B), design laws (Jakob, Tesler, Postel, Conway, Goodhart), Norman's interaction model, human error and automation, learning, research sample-size laws |
| **Biases_Behavior** | 87 | Cognitive biases and behavioral effects, each with its UX implication and an audit or ethics check (including research biases) |
| **Deceptive_Patterns** + DP_Instances | 98 / 4,174 | Taxonomies: Brignull 2010 and 2023, Gray 2018 and 2024, Mathur 2019 and 2021, EDPB, FTC 2022, EU DSA Art. 25, California CPRA, India CCPA 2023, attention-capture patterns. Plus labeled instance datasets |
| **Metrics_Methods** | 77 | SUS (all 10 items and scoring), UMUX, UMUX-LITE, SEQ, ASQ, PSSUQ, QUIS, SUMI, AttrakDiff, UEQ, SUPR-Q, NASA-TLX, NPS, CSAT, CES, HEART, task metrics, lostness, severity scale, Kano, readability formulas, contrast formula, and 39 research and evaluation methods |
| **Thresholds** | 49 | Numeric cheat sheet: contrast, target sizes, text spacing, line length, response times, Core Web Vitals, animation, sample sizes, NHTSA glance limits, NIST passwords, localization expansion, consent symmetry |
| **WCAG22_SC** | 87 | All WCAG 2.2 success criteria (normative text, level, year introduced) with Understanding "in brief", intent and benefits |
| WCAG_Failures / WCAG_Techniques | 96 / 351 | Every documented failure (F1–F112) and technique |
| WCAG3_Draft | 245 | Current WCAG 3 draft requirements (non-normative) |
| ACT_Rules / Axe_Rules / Lighthouse | 94 / 105 / 59 | Automatable test rules for layer A, with their WCAG mappings |
| ARIA_Patterns / COGA_Patterns | 30 / 59 | Keyboard and ARIA expectations per component; cognitive-accessibility design patterns |
| Checklists | 454 | A11Y Project checklist and Front-End Checklist rules |
| DesignSystems | 6,490 | Section-level guidance ("when to use", "how it works", do/don't) from GOV.UK, NHS, USWDS, IBM Carbon, Shopify Polaris and GitHub Primer |
| Gov_Content_Service | 1,288 | 18F content, UX and accessibility guides, Federal Plain Language Guidelines, Digital.gov guides, US Digital Services Playbook, 18F methods |
| Bibliography / Timeline | 298 / 13 decades | Seminal works by year, with venue, contribution and a lookup link |

## Schema (rule rows)

`kb_layer, id, source_set, source_org, author, year, category, subcategory, title, statement, rationale, audit_check, detection_layer, threshold, applies_to, level, severity_default, citation, url, text_origin, license, confidence`

- **detection_layer**: `deterministic` (DOM, axe or Lighthouse can check it), `screen` (vision plus accessibility tree on one screen), `flow` (needs a multi-step journey), `organizational / research` (process advice you can't see on screen). Design-system rows are tagged `screen / flow (guideline)`.
- **severity_default**: a starting point (critical / major / minor / n/a). Calibrate it on the eval set (ARCHITECTURE §8).
- **text_origin**: `verbatim` only for openly licensed or public-domain sources. Everything else is `paraphrased (curated)` and cites the original.
- **confidence**: `high` means well established or checked against the source; `medium` means written from memory of the source or only confirmed secondhand. Verify medium rows before quoting exact wording.

## How it was collected

- **Open sources (verbatim, with attribution):** shallow clones of the official GitHub repositories (`scripts/fetch_sources.sh`), parsed by `wcag.py`, `standards2.py`, `designsystems.py` and `misc.py`. The session's network blocked direct access to most websites, so official source repos were used instead of scraping pages.
- **Curated knowledge (paraphrased, cited):** `curated_*.py` and `bibliography.py`, written from the primary literature. Facts I was unsure of were checked with web search (GOV.UK's 11th principle, NIST SP 800-63B-4 numbers, Langevin 2021, Tognazzini 2014). Anything still uncertain is marked `confidence = medium`.
- **Rebuild:** `scripts/run_all.sh` clones the sources and regenerates every file. The output is deterministic.

## Licenses (check before redistributing)

| Source | License |
|---|---|
| W3C (WCAG, ACT, APG, COGA, WCAG 3) | W3C Document / Software and Document License: copy with attribution |
| USWDS, 18F, GSA, plainlanguage.gov, USDS Playbook | Public domain (US Government) / CC0 |
| GOV.UK Design System, NHS service manual | Open Government Licence v3.0 (code MIT) |
| axe-core | MPL-2.0 · Lighthouse, Carbon, A11Y Project: Apache-2.0 · Polaris, Primer, Front-End Checklist: MIT |
| Dark-pattern instances (Mathur et al.) | **GPL-3.0**. Keep this file separate if your product code must not be GPL |
| Curated rows | Original summaries for this project. Cite the original sources |

Proprietary sources (NN/g articles, Baymard Institute, Apple HIG, Material, ISO standards, Laws of UX site) were **not copied**. Their ideas appear only as paraphrased, cited summaries.

## Known gaps and how to close them

| Gap | Why it's missing | To add it |
|---|---|---|
| Smith & Mosier (1986), 944 guidelines (public, US Air Force/MITRE) | Hosts blocked (`hcibib.org`, `www.comp.nus.edu.sg`) | Allow those hosts in the environment, then parse `hcibib.org/sam/1.html`–`6.html` |
| HHS Research-Based Web Design & Usability Guidelines (2006), 209 guidelines (public domain) | usability.gov retired; archives blocked | Allow `cybercemetery.unt.edu` or `webarchive.library.unt.edu`, then parse `guidelines_book.pdf` |
| "Every paper": full scholarly metadata (100k+ HCI papers) | `api.openalex.org`, `api.crossref.org` and `api.semanticscholar.org` blocked | Allow `api.openalex.org` (CC0 data) to pull all CHI/CSCW/UIST/TOCHI papers with abstracts and citation counts |
| Full Laws of UX, NN/g and Baymard guideline text | Copyrighted or proprietary | License them, or keep using the paraphrased summaries here |
| ISO 9241 full text, MIL-STD-1472, FAA HF-STD-001, IEC 62366 | Paywalled or not fetched | MIL-STD-1472 and FAA HF-STD are public domain; add `quicksearch.dla.mil` / `www.faa.gov` |

## Using it in the product

1. Seed Heuristic Library v1 from **Audit_Rules**. Its fields already match the YAML in ARCHITECTURE.md: `id`, `category`, `heuristic` → rationale "Maps to", `applies_to`, `check` → `audit_check`, `severity_default`.
2. Wire the **Axe_Rules / ACT_Rules / Lighthouse / Thresholds** rows to layer A (deterministic).
3. Put `ALL_RULES.jsonl` behind retrieval for layers B and C, so every AI finding can cite a `source_set` + `id` + `citation`. That supports the "evidence or it didn't happen" principle.
4. Use **DP_Instances** as labeled examples for a deceptive-pattern detector, and **Bibliography** for citations in reports.
