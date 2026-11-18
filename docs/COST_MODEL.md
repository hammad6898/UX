# Cost Model & Pricing (Draft v0.1)

These are estimates from list prices (Claude API, Nov 2026) and assumed token volumes. **Validate them with 5–10 real runs**: log `usage` per step in Langfuse and replace these numbers with measured ones.

## 1. What an "Ultra Deep Audit" does

- 6–10 goal-driven flows (signup, onboarding, core task, checkout/upgrade, settings, contact/support…)
- The agent **clicks, types, fills forms with test data, opens menus and modals, triggers errors on purpose** (empty submit, invalid email) to evaluate error states
- ~120 unique screen states × 2 viewports (desktop + mobile) ≈ **240 screen analyses**
- ~600 agent actions (incl. retries)
- Rule checks (axe, Lighthouse) on every state
- Screen-level + flow-level expert analysis, verification pass, prioritized roadmap
- **10 validated fix mockups** (patched on their real page, before/after)

## 2. Model assignment (reliability first)

| Job | Model | Why |
|---|---|---|
| Explorer agent (click, type, navigate) | `claude-opus-5-5` + computer use, **escalate to `claude-fable-5-2` when stuck** (3 failed attempts on a step) | High step volume; Opus 5.5 handles routine navigation; Fable steps in for hard states |
| Screen heuristic analysis ("the UX designer") | `claude-fable-5-2` | Most capable model, used where judgment quality matters most |
| Flow analysis (multi-step journey critique) | `claude-fable-5-2` | Hardest reasoning: whole-journey context |
| Verification pass (is each finding real?) | `claude-opus-5-5`, low effort | Independent second opinion; a different model reduces correlated errors |
| Prioritized roadmap / executive summary | `claude-fable-5-2` | One call, high visibility |
| Fix generation (HTML/CSS patch + self-check) | `claude-fable-5-2` | Must be correct, on-brand and accessible |

Prices used: Opus 5.5 $4 in / $20 out per 1M tokens, Fable 5.2 $8 / $40, cache reads $0.20/1M for both. Batch API = 50% off for non-urgent analysis.

## 3. Cost per Ultra Deep Audit

| Stage | Volume assumption | Est. cost |
|---|---|---|
| Exploration agent | 600 steps × ~25k input (≈70% cached) + ~800 output tokens each; +15% Fable escalations | **$30–40** |
| Screen analysis (Fable, batched) | 240 × (~30k cached heuristic library + ~15k fresh screenshot/DOM, ~4k output) | **$35** (≈$70 unbatched) |
| Verification (Opus, batched) | 240 × (~15k in, ~1.5k out) | **$11** |
| Flow analysis (Fable) | 8 flows × (~100k in, ~10k out) | **$10** |
| Roadmap / summary (Fable) | 1 × (~150k in, ~15k out) | **$2** |
| Fix generation (Fable) | 10 fixes × ~2 iterations (~40k in, ~15k out each) | **$20** |
| Cloud browser, Lighthouse, storage, jobs | ~1–3 browser-hours + storage | **$3–8** |
| Retry / failure buffer | +25% | **$25–30** |
| **Total cost per audit** | | **≈ $120–160** |

Rough comparisons:
- Same audit with Opus 5.5 everywhere: **≈ $70–90**
- **Quick Check** (1 screen, 2 viewports, Fable analysis, 1 fix): **≈ $1–2**
- **Re-audit** (only re-analyze changed screens, typically 20–30%): **≈ $30–50**

### Cost levers (without sacrificing quality)
1. **Prompt caching** of the heuristic library + system prompt (already assumed above).
2. **Batch API** for all non-live analysis (already assumed above).
3. **State deduplication**: identical templates (product pages, blog posts) are analyzed once.
4. **Incremental re-audits**: hash each screen and skip unchanged ones.
5. **Per-audit budget caps** (task budgets plus a hard dollar ceiling), so a runaway agent can't cost $500.
6. **Context editing** in the explorer: drop old screenshots from the agent's context; it keeps the flow log, not every image.

## 4. Market anchors

| Option | Typical price |
|---|---|
| Freelance UX audit | ~$500–3,000, 1–2 weeks (approximate market range, not verified) |
| Agency UX audit | ~$5,000–25,000+, 2–6 weeks (approximate market range, not verified) |
| Self-serve AI audit tools (single page) | ~$15–100/month (e.g. UX Pilot ~$14–19/mo, Design Audit Lens $99/mo) |
| Baymard UX-Ray (e-commerce) | Enterprise subscription, price not public |

Our position: **agency-depth output, delivered in under an hour, at a fraction of freelancer price.**

## 5. Recommended pricing

| Tier | Price | Includes | Est. cost | Gross margin |
|---|---|---|---|---|
| **Quick Check** | Free (3/month, email required) | 1 screen, top 5 issues, 1 fix | ~$1.50 | lead magnet |
| **Deep Audit (one-off)** | **$499** | Full ultra-deep audit, 10 fixes, PDF + share link, 1 re-audit within 30 days | ~$140 + ~$40 re-audit | **~64%** |
| **Starter** | **$199/mo** | 1 deep audit/mo (capped 5 flows / 60 screens) + 20 quick checks + re-audits | ~$90 | **~55%** |
| **Growth** | **$499/mo** | 3 deep audits/mo + unlimited quick checks (fair use) + Jira/Linear export + team seats | ~$300 (typical usage below max) | **~40–60%** |
| **Expert-Reviewed Audit** | **$1,500–2,500** | Deep audit + **you** review, edit and add a 30-min call | ~$150 + your time | **high** |

Notes:
- SaaS gross margins usually target 70%+. AI-heavy products often launch at 50–65% and improve as model prices fall and caching/dedup are tuned. Plan to reprice or shift the Fable/Opus mix once you have eval data.
- The **Expert-Reviewed** tier is the best way to start: it earns real money from day one, every review **becomes ground-truth data** for the eval set, and it builds trust while the AI earns its reputation.
- Cap usage on subscriptions (flows/screens per audit) so heavy sites don't destroy margins.

## 6. Recommended launch path
1. **Months 1–3:** sell the Expert-Reviewed Audit ($1,500) to 10–20 startups. The AI does 80%, you do 20%. Learn which findings clients act on.
2. **Months 3–6:** launch the self-serve Deep Audit at $499 once precision ≥ 85% on the eval set.
3. **Months 6+:** add subscriptions (re-audits + monitoring are the retention engine).
