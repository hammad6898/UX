# Competitive Landscape (verified Nov 2026)

Sources were checked by live web search on 2026-11-18. Vendor accuracy claims are self-reported. Some vendor sites (fleck.ai, uiuxauditor.ai, canaryusers.ai) could not be opened from the research environment, so their details come from search snippets only.

## 1. AI UX audit tools (closest competitors)

| Product | What it does | Gap vs. us |
|---|---|---|
| **Baymard UX-Ray 2.0** | Automated heuristic evaluation of live URLs or screenshots against Baymard's research-backed guidelines (209 UX parameters as of 2026, with a claimed 95% accuracy). Has a Chrome extension. Free tier finds 2 issues; full version needs Pro/Max plans. | **E-commerce only.** Single-page focus, no flow exploration, no generated fixes. Strongest credibility in the space. |
| **UXUI Auditor.ai** | "Deep UX audit & automated redesign" plus predictive attention maps. | Closest in pitch (audit + redesign). Details unverified, so evaluate it hands-on. |
| **UXAuditPro, UXLens, Talos, Krux, Design Audit Lens (~$99/mo), UXAudit.Now** | Screenshot or URL analyzers scoring against Nielsen/Baymard-style heuristics. Krux analyzes screen recordings of walkthroughs. | Mostly single-screen, generic findings, no navigation, little or no fix generation. |
| **Fleck** | UX audit guidance and tooling. Explicitly says strategy and trade-offs still need a designer. | Positions automation as a first pass only. |

## 2. Chrome extensions (direct overlap with our extension)

| Product | Notes |
|---|---|
| **synthux** (open source, MIT) | Nielsen heuristics plus synthetic user profiles, local or BYOK LLM. Roadmap includes before/after code fixes and a priority matrix. Only ~39 users. **Watch this one.** |
| **HeuristiCheck** | Nielsen heuristics plus AI remediation and WCAG AA, runs in the browser. |
| **Heuristic Inspector** | Annotate elements, custom rules, PDF export. |
| **Occhio Inspector** | Manual annotation with severity ratings (a tool for designers, not an automated auditor). |
| **Refyn It** | Credit-based tiered AI audits (Basic/Pro/Premium). |
| **UX Risk Detector, UX Intelligence Agent** | Smaller AI audit extensions. |

**Takeaway:** single-page AI audit extensions are becoming a commodity. We don't win on "AI checks this page." We win on flows, evidence quality and fixes.

## 3. AI browser agents and synthetic users

| Product | Notes |
|---|---|
| **Loop11 AI Browser Agents** | Run usability tasks with ChatGPT/Claude/Gemini agents. Its own study found AI agents succeeded on **0–25%** of tasks vs. **62–95%** for humans, so agents are weak stand-ins for users. |
| **CanaryUsers, Synthetic Users, Uxia, Delve AI** | AI personas or agents for usability testing and interviews. |
| **synthetic-user-harness** (open source) | One Claude agent per persona in Playwright, producing structured reviews and Core Web Vitals. A good reference implementation. |
| **Research caveat** | A May 2026 survey found only 8% of UX researchers use synthetic participants and 88% doubt their quality. Synthetic users tend to be "too agreeable" and underestimate cognitive load. |

**Takeaway:** don't market "AI users test your product." Use the agent to *explore and map* flows, and have the expert rubric do the judging.

## 4. Behavior analytics (adjacent, and a pricing threat)

| Product | Notes |
|---|---|
| **Microsoft Clarity (free)** | Copilot summaries of recordings and heatmaps. **New Nov 4, 2026:** "simulation assessments" in which AI agents attempt key tasks on your site and report completion, time and friction points (commerce/travel first), plus Ask Clarity (an AI analyst) and an agent-traffic dashboard. |
| Hotjar, FullStory, Contentsquare, PostHog, LogRocket | Need real traffic and show symptoms, not fixes. |

**Takeaway:** Clarity is free and now runs agent task simulations, though focused on *AI-agent readiness* rather than human UX. Our differentiator has to be expert-grade diagnosis plus fixes, and working **before** you have traffic.

## 5. AI design generation (fix and mockup side)

| Product | Notes |
|---|---|
| **Google Stitch** (built on acquired Galileo AI) | Free tier. Can redesign an existing page from a screenshot or URL, generate variations, and export to Figma or code. |
| UX Pilot (~$14–19/mo + credits), Uizard (Miro), Visily, v0, Lovable | Generate UI from prompts. Some offer AI design review inside Figma. |

**Takeaway:** "redesign my page" is available for free (Stitch). Our fixes must be **tied to a specific diagnosed problem**, stay **faithful to the real product** (a patched DOM, not a reimagined page), and be **exportable as code or Figma**.

## Positioning summary

No tool found does all four:
1. **Explores multi-step flows** autonomously (incl. behind login via the extension)
2. **Diagnoses with evidence** at expert level, across all verticals (not just e-commerce)
3. **Prioritizes** for a non-designer founder
4. **Shows the fix on their real product** (before/after), exportable

Biggest threats: Baymard (credibility; could expand beyond e-commerce), Microsoft Clarity (free; already simulates agent tasks), Google Stitch (free redesigns).

## Sources
- https://baymard.com/blog/ai-heuristic-evaluations
- https://baymard.com/blog/ux-ray-progress-2026
- https://baymard.com/product/ux-ray
- https://ask.baymard.com/help-center/ux-ray-chrome-extension
- https://fleck.ai/guides/best-ux-audit-tools
- https://uiuxauditor.ai/
- https://www.uxauditpro.com/
- https://www.uxlens.pro/
- https://talos.tools/website-uiux-analyzer
- https://www.trykrux.com/
- https://www.stork.ai/en/design-audit-lens
- https://github.com/synthuxapp/synthux
- https://chromewebstore.google.com/detail/pkbdpflhdjbibkpadnkojkecobcdndae (HeuristiCheck)
- https://chromewebstore.google.com/detail/heuristic-inspector/opjfancdaoajjokijfdmdjlmhocepnde
- https://chromewebstore.google.com/detail/refyn-it-instant-ai-power/fcnkdiambdmlfjlpdfnnandaejfbcice
- https://loop11.medium.com/introducing-ai-browser-agents-a-new-way-to-run-usability-tests-in-loop11-31f08e9b70ab
- https://www.loop11.com/ai-vs-human-usability-testing-a-comparative-analysis-using-loop11/
- https://www.canaryusers.ai/blog/ai-usability-testing-tools
- https://github.com/berober2003/synthetic-user-harness
- https://synthers.ai/blog/synthetic-user-bias/
- https://pipelinemag.ai/posts/synthetic-users-too-agreeable-ux-testing/
- https://www.firecrawl.dev/blog/best-browser-agents
- https://www.seroundtable.com/microsoft-clarity-gains-agentic-analytics-and-ask-clarity-42449.html
- https://www.emarketer.com/content/microsoft-clarity-gives-retailers-new-ways-track-ai-agents-checkout-friction
- https://www.contentgrip.com/microsoft-clarity-agent-analytics/
- https://www.rundown.ai/guides/how-to-use-google-stitch-to-redesign-your-entire-website-for-free
- https://www.banani.co/de/blog/google-stitch-ai-review
- https://flowstep.ai/blog/ux-pilot-pricing
- https://www.nngroup.com/articles/ai-agents-as-users/
- https://merj.com/blog/agent-interaction-research
