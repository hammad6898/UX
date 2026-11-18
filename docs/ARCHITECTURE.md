# UX Audit Platform: Architecture & Tech Stack (Draft v0.1)

## 1. Product principles

1. **Zero-effort start.** Paste a URL or click the extension, and see the first result in under 60 seconds. No signup for a Quick Check.
2. **Evidence or it didn't happen.** Every finding points at a real element, screenshot region or rule. No generic advice.
3. **Prioritize for founders.** Lead with "fix these 3 first," not 80 findings.
4. **Show, don't tell.** The top issues come with a before/after of *their* screen.
5. **Expert rubric over AI vibes.** The judging logic is a versioned heuristic library written by a UX designer (you). The model applies it; it doesn't invent it.

## 2. Two modes, one pipeline

| | **Quick Check** | **Deep Audit** |
|---|---|---|
| Input | URL, or extension on the current tab | URL + goals ("sign up", "checkout"), optional login via extension |
| Scope | 1 screen (+ mobile viewport) | 3–10 flows, 20–100 screens |
| Time | < 60 s, live streaming results | 5–20 min, background job, notification when done |
| Output | Score, top 5 issues, 1 fix mockup | Flow map, full findings, prioritized roadmap, 3–10 fix mockups, PDF/share link, re-audit diff |
| Price | Free / lead magnet | Paid per audit or subscription |

Both modes run the **same pipeline** with different budgets, so you build it once.

```
 INPUT ─► CAPTURE ─► EXPLORE ─► DIAGNOSE ─► PRIORITIZE ─► FIX ─► REPORT
          (state)    (flows)    (3 layers)   (score)      (mockups)
           Quick Check skips EXPLORE (single state)
```

## 3. Inputs (easiest first)

1. **URL**: public pages, crawled in a cloud browser.
2. **Browser extension**: audits the current tab *inside the user's logged-in session* (no password sharing). Can also "record a flow" while the user clicks through, which beats autonomous exploration for complex apps.
3. **Screenshots / screen recording upload**: covers **desktop apps and mobile apps on day one** with no native integration (frames are extracted from the video).
4. *(Later)* Figma file link, native desktop helper (see §10).

## 4. System components

```
┌──────────────┐  ┌──────────────┐
│  Web app     │  │  Extension   │   clients
│  (Next.js)   │  │  (WXT, MV3)  │
└──────┬───────┘  └──────┬───────┘
       └──────┬──────────┘
        ┌─────▼──────┐      ┌───────────────┐
        │  API       │─────►│ Postgres      │  audits, screens, flows,
        │  (Next.js  │      │ (Supabase)    │  findings, fixes, users
        │  routes)   │      └───────────────┘
        └─────┬──────┘      ┌───────────────┐
              │             │ Object store  │  screenshots, DOM snapshots,
              ▼             │ (R2 / S3)     │  mockup renders
     ┌──────────────────┐   └───────────────┘
     │ Job orchestrator │  durable multi-step jobs, retries, progress events
     │ (Trigger.dev)    │
     └────────┬─────────┘
   ┌──────────┼───────────────┬───────────────┐
   ▼          ▼               ▼               ▼
 Capture   Explorer       Analysis         Fix
 worker    agent          engine           generator
   │          │               │               │
   └──────────┴─── Cloud browser (Browserbase / Steel, Playwright) ─┘
                          │
                    Claude API
```

### 4.1 Capture (per screen state)
For every state, collect a **ScreenState** bundle:
- Full-page and viewport screenshots (desktop 1440, mobile 390)
- DOM snapshot + **accessibility tree** + computed styles of visible elements
- Element bounding boxes (so findings can point at exact pixels)
- Console errors, network failures, Core Web Vitals (LCP, CLS, INP)
- Extracted **design tokens**: colors, fonts, spacing, radii, button styles (reused by the fix generator)

From the extension, the content script collects the same bundle locally and uploads it.

### 4.2 Explorer agent (Deep Audit)
- Goal-directed: "Complete signup as a new user", "Find pricing and start a trial".
- Loop: observe (screenshot + accessibility tree) → choose action → act via Playwright → capture the new state.
- Use **accessibility-tree / DOM actions first** (cheap, reliable). Fall back to **Claude computer use** (`computer_toolset_20260801`) for canvas-heavy or unusual UIs.
- **State deduplication**: hash of normalized DOM structure + perceptual screenshot hash, so "same page, different product" doesn't explode the graph.
- Output: a **Flow Graph** (nodes = states, edges = actions), with dead ends, loops, errors and step counts.
- **Safety rails**: never submit payments, never delete or send anything real, stay on the target domain, use test data for forms, keep a hard step budget per flow, and pause and ask the user at CAPTCHAs or 2FA (via the extension).

> Research note: AI agents are poor stand-ins for users (Loop11: 0–25% task success vs. 62–95% for humans). Use the agent to **map and reach** states, not to judge usability by whether it succeeded.

### 4.3 Analysis engine (the core IP)
Three layers, merged into one findings list:

| Layer | What | How | Reliability |
|---|---|---|---|
| **A. Deterministic** | Accessibility (WCAG AA), contrast, target size, missing labels, font sizes, layout shift, performance, broken links, console errors, inconsistent button styles across screens | axe-core, Lighthouse, custom DOM/style rules | Very high, no AI |
| **B. Screen heuristics** | Visual hierarchy, CTA clarity, copy clarity, affordances, feedback, error states, empty states, trust signals, consistency | Claude vision on screenshot + accessibility tree, applying the **Heuristic Library** with structured output (JSON schema) | Medium-high, made grounded |
| **C. Flow heuristics** | Too many steps, repeated input, forced signup before value, dead ends, missing progress indication, unclear next step, inconsistent navigation | Flow Graph metrics + Claude reasoning over the flow narrative | Medium, our differentiator |

**Grounding & anti-hallucination:**
- Every AI finding must cite an `element_id` (from the captured tree) or a bounding box. Findings that cite nothing are dropped.
- A **verification pass**: a second, cheaper call checks each finding against the evidence ("Is this actually visible in the screenshot? Y/N + reason").
- Show a confidence level, and label findings "Confirmed" (rule-based) or "Expert review" (AI).

**Heuristic Library** (versioned JSON/YAML in the repo, written by you):
```yaml
id: form.inline-validation
category: Forms
heuristic: Nielsen #9 Help users recognize, diagnose, recover from errors
applies_to: [form]
check: Errors shown only after submit; no inline validation on complex fields
severity_default: major
why_it_matters: ...
fix_patterns: [inline-validation, field-hints]
examples: [good.png, bad.png]
```
This is your moat: your 5 years of judgment, codified and tested.

### 4.4 Prioritization
`priority = severity (1–4) × reach (flow importance × screen position) × confidence ÷ effort (S/M/L)`
Output: a **Top 3 / Next 10 / Backlog** roadmap in plain language.

### 4.5 Fix generator
Two modes:
1. **Patch mode (default, web)**: Claude gets the DOM subtree + design tokens + the finding + a fix pattern, and returns an **HTML/CSS patch**. We apply it in the cloud browser, re-screenshot, **re-run axe on the result** (the fix must not create new issues), and render a **before/after slider**. Faithful to their brand by construction. Export as a code diff.
2. **Concept mode (bigger redesigns / screenshot-only input)**: generate 2–3 alternative layouts as HTML using their extracted tokens, rendered to images. Export HTML; Figma export later via an HTML→Figma plugin.

### 4.6 Report
- Interactive web report: score, flow map (React Flow), annotated screenshots with pins, findings grouped by flow, before/after sliders.
- Share link, PDF export, "Copy as ticket" (Linear/Jira/GitHub issue).
- **Re-audit**: run again after changes and show what's fixed, what regressed and the score delta. This drives retention.

## 5. Tech stack

| Area | Choice | Why |
|---|---|---|
| Language | **TypeScript everywhere** | One language for the extension, web, workers and Playwright |
| Monorepo | pnpm + Turborepo | Shared types/schemas between extension, web and workers |
| Web app + API | **Next.js** (App Router) on Vercel | Fast to ship; route handlers for the API |
| Extension | **WXT** (Manifest V3, React) | Chrome + Firefox + Edge from one codebase, hot reload |
| UI | Tailwind + shadcn/ui, **React Flow** (flow maps) | Fast, good-looking defaults |
| Jobs | **Trigger.dev** (or Inngest) | Long-running durable jobs, retries, live progress to the UI; no infrastructure to run |
| Browser | **Playwright** on **Browserbase** or **Steel** | Managed cloud browsers built for agents; avoid running Chromium fleets yourself |
| Agent actions | Playwright + accessibility tree; **Stagehand**/**Browser Use** as optional helpers; Claude computer use as a fallback | Cheap and reliable first, vision when needed |
| Rule checks | **axe-core**, **Lighthouse**, custom rules | Industry standard, trusted |
| LLM | **Claude API**: `claude-opus-5-5` (vision, 1M context, structured outputs, computer use) | See §6 |
| DB | **Postgres on Supabase** + Drizzle ORM | Auth + DB + storage in one; easy start |
| Files | Cloudflare **R2** (or Supabase Storage) | Cheap screenshot storage, no egress fees |
| Auth | Supabase Auth (or Clerk) | Magic link + Google |
| Payments | Stripe (credits + subscription) | Standard |
| LLM observability | Langfuse | Trace every prompt/finding; vital for quality tuning |
| Product analytics | PostHog | Funnels on your own product (practice what you preach) |
| PDF | Playwright `page.pdf()` of the report page | No separate PDF stack |

## 6. AI usage plan (Claude)

- **Default model: `claude-opus-5-5`** ($4 / $20 per 1M input/output tokens) for screen heuristics, flow reasoning and fix generation. Adaptive thinking; set `effort` per step (e.g. `low` for verification, `high` for flow analysis and fixes). Note that Opus 5.5 defaults to `medium`, so set it explicitly.
- **Structured outputs** (`output_config.format` with a JSON schema) for every finding, so the analysis returns typed data, never prose to parse.
- **Prompt caching**: the Heuristic Library + system prompt are large and identical across calls. Put them first with `cache_control`, so cached reads cost a fraction of the price.
- **Message Batches API (50% cheaper)** for Deep Audit screen analysis, which isn't latency-sensitive. Quick Check uses streaming for live results.
- **Computer use** (`computer_toolset_20260801`) only as an Explorer fallback.
- **Your call on cost:** cheaper models (`claude-sonnet-5-5` at $2/$10, `claude-haiku-5-5` at $0.10/$0.50) could handle the verification pass or deduplication. Decide this after the eval set (§8) shows whether quality holds.
- **Refusal handling**: check `stop_reason` and enable server-side fallbacks.

## 7. Data model (core tables)

```
projects(id, owner_id, name, root_url, design_tokens)
audits(id, project_id, mode[quick|deep], status, goals[], score, created_at)
screens(id, audit_id, url, viewport, screenshot_key, dom_key, a11y_key, state_hash)
flows(id, audit_id, goal, status, step_count)
flow_edges(flow_id, from_screen, to_screen, action, order)
findings(id, audit_id, screen_id?, flow_id?, layer[rule|screen|flow], heuristic_id,
         title, description, evidence{element_id,bbox}, severity, confidence,
         effort, priority, status[open|fixed|dismissed])
fixes(id, finding_id, mode[patch|concept], patch_html, before_key, after_key, validated)
heuristics(id, version, yaml)   -- or kept as files in the repo
```

## 8. Quality & evals (do this from week 1)

Quality is the product, and you're the domain expert:
1. Pick **30 real sites** (a mix of SaaS, e-commerce and marketing sites).
2. **Audit them by hand** with your own heuristics to create the ground truth.
3. Measure the system: **precision** (are the findings real?), **recall** (did it catch your top issues?) and **priority agreement**.
4. Re-run this on every prompt or heuristic change. Don't ship changes that lower precision.

Target precision ≥ 85% before public launch. False positives kill trust faster than missed issues.

## 9. Security & trust
- The extension asks for minimal permissions (`activeTab` + `scripting`, granted on click), not "read all sites."
- Mask password fields and obvious PII in captured DOM and screenshots before upload. Users can redact more.
- Cloud browser sessions are isolated per audit and destroyed after.
- Respect `robots.txt` for URL crawls and rate-limit per domain. Only audit sites the user owns or has rights to (checkbox + domain verification for Deep Audits).

## 10. Desktop apps (phased)
1. **Now:** screenshot / screen-recording upload → screen + flow analysis + concept-mode fixes.
2. **Later:** a small native helper (Tauri) that reads OS accessibility trees (macOS AX, Windows UI Automation) + screenshots and drives the app via Claude computer use. Same pipeline downstream.
3. Electron apps can be audited much like web apps (they're Chromium).

## 11. Build roadmap

| Phase | Weeks | Deliverable |
|---|---|---|
| **0. Foundations** | 1–2 | Monorepo, Heuristic Library v1 (~40 heuristics), eval set of 30 hand-audited sites |
| **1. Quick Check (web)** | 3–6 | URL → capture → layers A + B → prioritized top 5 → web report. Measure precision on the eval set |
| **2. Extension** | 7–9 | Audit current tab (logged-in pages), overlay pins on the live page, open the full report |
| **3. Fixes** | 10–12 | Patch-mode before/after for the top 3 findings, with axe re-validation |
| **4. Deep Audit** | 13–18 | Explorer agent, flow graph, layer C, background jobs, flow map UI, PDF/share |
| **5. Monetize + retain** | 19–22 | Stripe, re-audit diff, "copy as ticket," upload screenshots/recordings |
| **6. Expand** | later | Concept-mode redesigns, Figma export, desktop helper, scheduled monitoring |

## 12. Open decisions
- [ ] Pricing model: per-audit credits vs. subscription vs. both
- [ ] Vertical focus at launch (SaaS onboarding? e-commerce? Avoid competing head-on with Baymard in e-commerce)
- [ ] Browserbase vs. Steel vs. self-hosted Playwright (cost at scale)
- [ ] Model mix after evals (all Opus 5.5 vs. cheaper models for verification)
- [ ] Brand / product name
