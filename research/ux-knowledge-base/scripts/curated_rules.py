from common import *
R = []
def X(rid, cat, title, rule, why, check, layer, sev, applies, cite, maps='', threshold='', conf='high'):
    R.append(C(rid, title, '', '', rule, (f'Maps to: {maps}. ' if maps else '') + why, check, layer, threshold, cite, cat, maps,
               applies=applies, sev=sev, conf=conf, source_set='Curated: audit rules (evidence-based)'))
N = 'Nielsen #'
F = 'Forms & input'
# ---------------- FORMS ----------------
X('form.labels-visible', F, 'Every field has a visible, persistent label', 'Each input has a visible text label that stays visible while typing; placeholders are not used as the only label.',
  'Placeholder-only labels disappear on input, burden memory, look like pre-filled values, often fail contrast, and are unreliable for assistive tech.', 'Does every input have a visible label that remains after the user starts typing?',
  'deterministic (DOM: label/aria-labelledby) + screen', 'major', 'form', 'Sherwin, K. (2014). Placeholders in Form Fields Are Harmful. NN/g; WCAG 2.2 SC 3.3.2, 1.3.1, 2.5.3.', N + '6; WCAG 3.3.2')
X('form.label-placement', F, 'Labels above fields for fastest completion', 'Place labels above inputs (top-aligned) in single-column forms; left-aligned labels only when scanning label names matters more than speed.',
  'Eye-tracking showed top-aligned labels yield the fastest completion with fewest fixations; they also work on mobile and with long translations.', 'Are labels top-aligned and close to their fields?',
  'screen', 'minor', 'form', 'Penzo, M. (2006). Label Placement in Forms. UXmatters; Wroblewski, L. (2008). Web Form Design. Rosenfeld Media.', 'Gestalt proximity')
X('form.single-column', F, 'Use a single-column layout', 'Arrange form fields in one column, except closely related short fields (e.g., city/postcode) that can share a row.',
  'Multi-column forms cause users to skip fields or misinterpret the reading order, and break on narrow screens.', 'Is the form laid out in a single column?',
  'screen', 'minor', 'form', 'Baymard Institute checkout research; Jarrett, C. & Gaffney, G. (2009). Forms that Work. Morgan Kaufmann.', N + '8', conf='medium')
X('form.inline-validation', F, 'Validate inline after the field is completed', 'Validate fields when the user leaves them (on blur) or after a short pause for complex inputs; do not validate while users are still typing their first attempt, and do not wait until submit for everything.',
  'In a 2009 test, inline validation produced a 22% increase in success, 22% fewer errors, 31% higher satisfaction, 42% faster completion and 47% fewer eye fixations versus after-submit validation.',
  'Are errors shown next to the field after it is completed (not only after submit, and not prematurely while typing)?', 'flow', 'major', 'form',
  'Wroblewski, L. (2009). Inline Validation in Web Forms. A List Apart.', N + '9; WCAG 3.3.1, 3.3.3')
X('form.error-summary', F, 'Show an error summary and inline messages on submit', 'On submit with errors, show an error summary at the top linking to each field, move focus to it, and show a specific message next to each field.',
  'Users of all abilities, including screen reader users, need to know errors exist and get to them quickly.', 'On failed submit, is there an error summary with links to each field, and specific inline messages?',
  'flow', 'major', 'form', 'GOV.UK Design System: Error summary & Error message components; WCAG 2.2 SC 3.3.1, 3.3.3.', N + '9; WCAG 3.3.1')
X('form.error-message-quality', F, 'Error messages are specific and constructive', 'Error messages say exactly what is wrong and how to fix it, in plain language, without blaming the user (e.g., "Enter a date of birth in the past" not "Invalid input").',
  'Vague errors increase recovery time and abandonment.', 'Do error messages name the field, describe the problem and the fix?', 'screen', 'major', 'form',
  'Nielsen, J. (2001). Error Message Guidelines. NN/g; GOV.UK Design System: Error message.', N + '9')
X('form.preserve-input', F, 'Preserve user input after errors and navigation', 'Never clear valid fields after a validation error, page reload or back navigation (except sensitive fields like passwords/CVV where required).',
  'Re-entering data is a major cause of frustration and abandonment.', 'After a failed submit or going back, are previously entered values still present?', 'flow', 'critical', 'form',
  'Raskin (2000) first law; Nielsen #3/#9; WCAG 3.3.7 Redundant Entry.', N + '3; WCAG 3.3.7')
X('form.redundant-entry', F, 'Do not ask for the same information twice', 'Auto-fill or offer to reuse information already given in the same process (e.g., "billing same as shipping").',
  'Redundant entry adds effort and errors and is a WCAG 2.2 Level A requirement.', 'Is any information requested more than once in a flow?', 'flow', 'major', 'form',
  'WCAG 2.2 SC 3.3.7 Redundant Entry (2023).', 'WCAG 3.3.7')
X('form.only-necessary', F, 'Ask only for what you need', 'Every field must be justified by a clear need; remove optional and nice-to-have fields, or defer them until after the core task.',
  'Each extra field increases effort and abandonment; unnecessary personal data collection also conflicts with data minimisation (GDPR Art. 5).', 'Is every field necessary for the task at this point?',
  'screen', 'major', 'form', 'Jarrett & Gaffney (2009); GOV.UK Service Manual: Designing good questions (question protocol); GDPR Art. 5(1)(c).', N + '8')
X('form.optional-required', F, 'Clearly mark optional (or required) fields', 'Mark optional fields with "(optional)" when most fields are required, or mark required fields consistently; explain any symbol used.',
  'Users otherwise guess and either skip required fields or waste effort on optional ones.', 'Is it clear which fields are optional or required?', 'deterministic (partial) + screen', 'minor', 'form',
  'GOV.UK Design System: Question pages; Baymard Institute research on required/optional marking.', N + '6', conf='medium')
X('form.input-types', F, 'Use appropriate input types and mobile keyboards', 'Use type="email", "tel", "url", "number" (or inputmode="numeric" for codes), and date controls appropriately so mobile users get the right keyboard.',
  'Correct keyboards reduce typing errors and effort on touch devices.', 'Do fields trigger the appropriate mobile keyboard?', 'deterministic (DOM attributes)', 'minor', 'form, mobile',
  'HTML Living Standard; Google Web Fundamentals (2016) form best practices.', N + '7')
X('form.autocomplete', F, 'Support browser autofill with autocomplete attributes', 'Add correct autocomplete tokens (name, email, tel, street-address, postal-code, cc-number, one-time-code, new-password, current-password).',
  'Autofill speeds completion dramatically and is required for personal data fields under WCAG 1.3.5.', 'Do personal-data fields have valid autocomplete attributes?', 'deterministic (DOM attributes)', 'major', 'form',
  'WCAG 2.2 SC 1.3.5 Identify Input Purpose; HTML autofill spec.', 'WCAG 1.3.5')
X('form.field-width', F, 'Size fields to the expected input length', 'Make field widths reflect the expected length (short for postcode/CVV, long for address lines).',
  'Field length is a cue to the expected answer; mismatched widths cause uncertainty.', 'Do field widths match expected input length?', 'screen', 'minor', 'form',
  'Wroblewski (2008); GOV.UK Design System: Text input (fixed width inputs).', N + '2', conf='medium')
X('form.forgiving-format', F, 'Accept input in any reasonable format', 'Accept spaces, dashes, brackets, mixed case and leading/trailing spaces in phone numbers, card numbers, postcodes and codes; normalize on the server.',
  'Strict format rules create avoidable errors (Postel’s law).', 'Do fields accept common variations instead of rejecting them?', 'deterministic (input fuzzing) + flow', 'major', 'form',
  'Postel (1980); GOV.UK Design System: Text input; Baymard Institute research.', N + '5')
X('form.select-vs-radio', F, 'Use radios for few options and autocomplete for many', 'Use radio buttons for up to about 5–7 mutually exclusive options so all are visible; use a select for longer lists, and an autocomplete/combobox for very long lists such as countries.',
  'Dropdowns hide options and require extra clicks; long dropdowns are hard to scan.', 'Are small option sets shown as radios and very long lists searchable?', 'screen', 'minor', 'form',
  'GOV.UK Design System: Radios / Select ("avoid the select component if possible"); NN/g (2017) Dropdowns: Design Guidelines.', N + '6', conf='medium')
X('form.dates', F, 'Use the right date input for the date type', 'For memorable dates (date of birth), use separate day/month/year text inputs; for nearby dates, a date picker can help; always show the expected format.',
  'Date pickers are slow for distant dates; ambiguous formats cause errors across locales.', 'Is the date input appropriate to the kind of date and is the format clear?', 'screen', 'minor', 'form',
  'GOV.UK Design System: Date input & Dates pattern.', N + '5')
X('form.no-disabled-submit', F, 'Do not disable the submit button to signal errors', 'Keep the primary submit button enabled and explain errors on submit, instead of disabling it until the form is valid.',
  'Disabled buttons give no explanation of what is wrong, are often low contrast, and are skipped by keyboard users.', 'Is the submit button enabled, with errors explained on submit?', 'screen', 'minor', 'form',
  'GOV.UK Design System: Button ("disabled buttons"); Silver, A. (2019). Form Design Patterns. Smashing.', N + '9', conf='medium')
X('form.no-reset', F, 'Avoid reset/clear buttons next to submit', 'Do not place "Reset" or "Clear" buttons next to "Submit".',
  'Users accidentally wipe their entries; the action is rarely needed.', 'Is there a reset/clear-form button near the submit button?', 'deterministic (DOM) + screen', 'major', 'form',
  'Nielsen, J. (2000). Reset and Cancel Buttons. NN/g.', N + '5')
X('form.button-labels', F, 'Button labels describe the action', 'Primary buttons use specific verbs ("Create account", "Pay £24.99") rather than generic labels ("Submit", "OK").',
  'Specific labels confirm the outcome and reduce errors.', 'Do action buttons say what will happen?', 'screen', 'minor', 'form, actions',
  'GOV.UK Design System: Button; USWDS: Button usability guidance.', N + '2')
X('form.password-ux', F, 'Password fields support managers, paste and visibility', 'Allow paste and password managers, offer a show/hide toggle, show requirements before typing, and do not impose composition rules or periodic changes.',
  'Blocking paste and complex rules lower security and usability; NIST and WCAG 3.3.8 require support for password managers/copy-paste.', 'Can users paste, use a password manager, and reveal the password? Are requirements shown up front?',
  'deterministic (DOM: onpaste, autocomplete) + flow', 'major', 'authentication', 'NIST SP 800-63B-4 (2025); WCAG 2.2 SC 3.3.8 Accessible Authentication; NCSC (2015) Password guidance.', 'WCAG 3.3.8', threshold='≥ 15 chars single-factor; ≥ 64 max accepted')
X('form.captcha', F, 'Avoid cognitive-function CAPTCHAs', 'Avoid puzzles or transcription CAPTCHAs; use invisible risk scoring, rate limiting or accessible alternatives.',
  'CAPTCHAs block disabled users and reduce conversion; WCAG 2.2 3.3.8 restricts cognitive function tests.', 'Does the flow include a CAPTCHA without an accessible, non-cognitive alternative?', 'screen', 'major', 'form, authentication',
  'W3C (2021). Inaccessibility of CAPTCHA; WCAG 2.2 SC 3.3.8.', 'WCAG 3.3.8')
X('form.names', F, 'Do not force assumptions about names', 'Use a single "Full name" field unless separate parts are really needed; accept apostrophes, hyphens, spaces, accents and non-Latin characters; do not require a last name.',
  'Name structures vary worldwide; strict validation excludes real users.', 'Do name fields accept international names and characters?', 'deterministic (input fuzzing)', 'major', 'form',
  'W3C Internationalization (2011, updated). Personal names around the world; GOV.UK Design System: Names pattern.', N + '2')
X('form.addresses', F, 'Make address entry flexible and fast', 'Offer address lookup with a manual-entry fallback, auto-detect city/region from postcode where reliable, and allow international formats.',
  'Address entry is one of the most error-prone parts of checkout.', 'Is there address autocomplete with manual fallback, and support for international addresses?', 'flow', 'minor', 'form, checkout',
  'GOV.UK Design System: Addresses pattern; Baymard Institute checkout research.', N + '7', conf='medium')
X('form.sex-gender', F, 'Ask about sex or gender only when needed, and well', 'Only ask if required, explain why, and follow inclusive patterns.',
  'Unnecessary or poorly designed questions exclude and upset users.', 'Is sex/gender asked only when necessary, with explanation and inclusive options?', 'screen', 'minor', 'form',
  'GOV.UK Design System: Gender or sex pattern.', 'Ethics')
X('form.multi-step-progress', F, 'Long forms are split into steps with progress', 'Break long forms into logical steps ("one thing per page" where appropriate) and show progress and remaining steps.',
  'Chunking reduces cognitive load; progress indicators motivate completion (goal-gradient).', 'Are long forms divided into steps with a progress indicator?', 'flow', 'minor', 'form',
  'GOV.UK Service Manual: Structuring forms ("one thing per page"); Hull (1932)/Kivetz et al. (2006) goal-gradient.', N + '1')
X('form.check-answers', F, 'Let users review answers before final submission', 'Before submitting important or irreversible information, show a summary with change links.',
  'Review steps catch errors before they become costly (WCAG 3.3.4 for legal/financial).', 'Is there a review step with change links before final submission of consequential forms?', 'flow', 'major', 'form',
  'GOV.UK Design System: Check answers pattern; WCAG 2.2 SC 3.3.4 Error Prevention (Legal, Financial, Data).', N + '5; WCAG 3.3.4')
X('form.help-text', F, 'Provide hint text where needed, next to the field', 'Place hints (format, examples, why it is asked) between the label and the input, not in tooltips or placeholders.',
  'Visible hints prevent errors; tooltip help is often missed and inaccessible.', 'Are formats and constraints explained in visible hint text near the field?', 'screen', 'minor', 'form',
  'GOV.UK Design System: Text input hint; WCAG 2.2 SC 3.3.2.', N + '10; WCAG 3.3.2')
X('form.character-count', F, 'Show limits before users exceed them', 'For limited text fields, show the limit and remaining characters; do not silently truncate.',
  'Silent truncation loses data; hidden limits cause errors.', 'Are character limits shown and enforced transparently?', 'screen', 'minor', 'form',
  'GOV.UK Design System: Character count.', N + '5')
X('form.mobile-zoom', F, 'Avoid input zoom on mobile', 'Use at least 16 px font size for inputs so iOS Safari does not zoom on focus.',
  'Unexpected zoom disorients users and hides context.', 'Are input font sizes ≥ 16 px on mobile?', 'deterministic (computed styles)', 'minor', 'form, mobile', 'iOS Safari behavior; common practice.', N + '4', threshold='≥ 16 px', conf='medium')
X('form.consent-unchecked', F, 'Consent and marketing checkboxes are unchecked by default', 'Never pre-check boxes for marketing, data sharing, terms acceptance or paid extras.',
  'Pre-ticked consent is invalid under GDPR (CJEU Planet49, 2019) and is a recognized deceptive pattern (preselection).', 'Are any consent, marketing or paid-option checkboxes pre-checked?', 'deterministic (DOM: checked)', 'critical', 'form, consent',
  'CJEU C-673/17 Planet49 (2019); GDPR Recital 32; Mathur et al. (2019).', 'Ethics; GDPR')

# ---------------- NAVIGATION & IA ----------------
NV = 'Navigation & IA'
X('nav.logo-home', NV, 'Logo links to the homepage', 'Place the logo top-left (in LTR languages) and link it to the homepage.', 'Strong convention users rely on (Jakob’s law).', 'Does the logo link to the homepage?', 'deterministic (DOM)', 'minor', 'website',
  'Nielsen, J. & Tahir, M. (2001). Homepage Usability: 50 Websites Deconstructed. New Riders; NN/g research on logo placement (2016).', N + '4')
X('nav.visible-desktop', NV, 'Keep primary navigation visible on desktop', 'On desktop and large screens, show main navigation items rather than hiding them behind a hamburger icon.',
  'Hidden navigation is used less and lowers discoverability and task efficiency.', 'On desktop, is primary navigation visible without opening a menu?', 'screen', 'major', 'website, web app',
  'Pernice, K. & Budiu, R. (2016). Hamburger Menus and Hidden Navigation Hurt UX Metrics. NN/g.', N + '6', conf='medium')
X('nav.you-are-here', NV, 'Show users where they are', 'Highlight the current section in navigation, use page titles that match the link clicked, and use breadcrumbs for deep hierarchies.',
  'Users who land from search or deep links need orientation (Krug’s trunk test).', 'Can a user tell which site, section and page they are on?', 'screen', 'major', 'website, web app',
  'Krug, S. (2000). Don\'t Make Me Think (trunk test); WCAG 2.2 SC 2.4.2, 2.4.8.', N + '1')
X('nav.breadcrumbs', NV, 'Use breadcrumbs for hierarchical sites', 'Show breadcrumbs (hierarchy, not history) on sites with more than two levels.',
  'Breadcrumbs show location and offer quick upward navigation.', 'On deep pages, are hierarchy breadcrumbs present?', 'deterministic (DOM) + screen', 'minor', 'website',
  'NN/g (2018). Breadcrumbs: 11 Design Guidelines for Desktop and Mobile; GOV.UK Design System: Breadcrumbs.', N + '1', conf='medium')
X('nav.labels-scent', NV, 'Navigation labels are specific and user-language', 'Use descriptive, distinct labels that predict their content; avoid vague labels (Solutions, Resources, Products & Services) and internal jargon.',
  'Strong information scent drives successful navigation (Pirolli & Card 1999).', 'Would a new user know which navigation item leads to their goal?', 'screen', 'major', 'website, app',
  'Pirolli & Card (1999); Spool, J. (2004). The Right Trigger Words. UIE.', N + '2')
X('nav.task-based-ia', NV, 'Organize navigation around user tasks, not the org chart', 'Group content by user goals and mental models rather than internal departments.',
  'Conway’s law makes org-centric navigation common; it confuses users.', 'Does navigation reflect user tasks rather than internal structure?', 'screen', 'major', 'website',
  'Rosenfeld, L. & Morville, P. (1998). Information Architecture for the World Wide Web. O\'Reilly; Conway (1968).', N + '2')
X('nav.link-text', NV, 'Links have descriptive text', 'Link text makes sense out of context; avoid "click here", "read more" and bare URLs.',
  'Users and screen readers scan links; descriptive text improves scent and accessibility.', 'Is each link’s purpose clear from its text?', 'deterministic (DOM) + screen', 'major', 'web',
  'WCAG 2.2 SC 2.4.4 / 2.4.9; Nielsen (2009). "Learn More" Links: You Can Do Better.', 'WCAG 2.4.4')
X('nav.link-styling', NV, 'Links look like links', 'Use a distinct color and underline (at least for inline links), and different styling for visited links where useful.',
  'Users must distinguish clickable from non-clickable text; color alone fails for color-blind users.', 'Are links visually distinguishable from body text by more than color?', 'screen', 'major', 'web',
  'Nielsen (2004). Guidelines for Visualizing Links. NN/g; WCAG 2.2 SC 1.4.1.', 'WCAG 1.4.1')
X('nav.consistent', NV, 'Navigation is consistent across pages', 'Keep navigation in the same place and order on every page.', 'Consistency reduces relearning; WCAG 3.2.3 requires it.', 'Is navigation in the same position and order across pages?', 'flow', 'major', 'website',
  'WCAG 2.2 SC 3.2.3 Consistent Navigation.', 'WCAG 3.2.3')
X('nav.consistent-help', NV, 'Help is in a consistent location', 'If help mechanisms (contact, chat, FAQ) appear on multiple pages, they appear in the same relative order.', 'Users needing help must find it predictably.', 'Is help/contact in a consistent location across pages?', 'flow', 'minor', 'website',
  'WCAG 2.2 SC 3.2.6 Consistent Help.', 'WCAG 3.2.6')
X('nav.skip-link', NV, 'Provide a skip link and landmarks', 'Provide a "Skip to main content" link and use landmarks (header, nav, main, footer).', 'Keyboard and screen-reader users need to bypass repeated blocks.', 'Is there a working skip link and landmark structure?', 'deterministic (DOM)', 'major', 'web',
  'WCAG 2.2 SC 2.4.1 Bypass Blocks.', 'WCAG 2.4.1')
X('nav.footer', NV, 'Footer provides contact, legal and key links', 'Include contact details, privacy, terms, accessibility statement and important secondary links in the footer.', 'Users look to the footer for these by convention.', 'Does the footer include contact, privacy, terms and accessibility links?', 'deterministic (DOM) + screen', 'minor', 'website',
  'Common convention; Stanford Web Credibility Guidelines (2002).', N + '4')
X('nav.hover-menus', NV, 'Mega/dropdown menus are robust to pointer movement', 'Use hover-intent delays and "safe triangles" so menus do not close while users move diagonally; also support click/tap and keyboard.',
  'Accidental closing frustrates users (steering law); hover-only menus fail on touch and keyboard.', 'Do dropdown menus stay open during diagonal movement and work by click, tap and keyboard?', 'flow', 'minor', 'website',
  'Accot & Zhai (1997) steering law; NN/g (2017) Mega Menus Work Well for Site Navigation.', N + '7', conf='medium')
X('nav.carousel', NV, 'Avoid relying on auto-rotating carousels for key content', 'Do not put important content in later carousel slides; if used, do not auto-rotate (or provide pause), show slide count and allow swipe/keyboard.',
  'Carousel slides beyond the first get very little engagement and auto-rotation causes banner blindness and accessibility failures.', 'Is important content hidden in later carousel slides, and does the carousel auto-rotate without pause?', 'screen', 'minor', 'website',
  'Runyon, E. (2013). Carousel Interaction Stats (University of Notre Dame); WCAG 2.2 SC 2.2.2; NN/g (2013) Auto-Forwarding Carousels Annoy Users.', 'WCAG 2.2.2', conf='medium')
X('nav.infinite-scroll', NV, 'Use infinite scroll only for feed-like content', 'Prefer pagination or "load more" for goal-oriented browsing; keep the footer reachable, preserve position on back navigation.',
  'Infinite scroll hinders finding specific items, reaching footers, and returning to position.', 'If infinite scroll is used, can users reach the footer and return to the same position after back navigation?', 'flow', 'minor', 'website, app',
  'NN/g (2014). Infinite Scrolling Is Not for Every Website.', N + '3', conf='medium')
X('nav.back-button', NV, 'The back button works as expected', 'Browser/OS back returns to the previous view and state; single-page apps update history for meaningful view changes; modals and filters behave predictably.',
  'Back is one of the most used navigation features; breaking it is a severe usability problem.', 'Does browser/OS back return to the previous state without losing data?', 'flow', 'major', 'web app, website',
  'Nielsen, J. (1999). Top Ten Mistakes in Web Design ("Breaking the Back button").', N + '3')
X('nav.new-windows', NV, 'Do not open new windows/tabs unexpectedly', 'Open links in the same tab unless there is a strong reason (e.g., leaving a form in progress), and warn users when a new tab opens.',
  'Unexpected new windows break the back button and disorient users, especially screen reader users.', 'Do links open new tabs without warning?', 'deterministic (DOM: target=_blank)', 'minor', 'web',
  'Nielsen (1999). Top Ten Mistakes in Web Design; WCAG technique G201.', N + '3')
X('nav.404', NV, 'Helpful page-not-found and error pages', 'Error pages explain what happened in plain language and offer a path forward (search, links, contact).', 'Dead ends cause abandonment.', 'Do 404/500 pages explain and offer next steps?', 'flow', 'minor', 'website',
  'GOV.UK Design System: Page not found pages; Nielsen (1998). Improving the Dreaded 404 Error Message.', N + '9')

# ---------------- SEARCH ----------------
SR = 'Search & filtering'
X('search.visible', SR, 'Search is visible as an open field on content-rich sites', 'On sites with lots of content or products, show an open search box in the header rather than only an icon.', 'Search-dominant users look for a box; icon-only search reduces use.', 'On content-rich sites, is search an open input in the header?', 'screen', 'minor', 'website',
  'Nielsen (2008). Search: Visible and Simple. NN/g.', N + '7', conf='medium')
X('search.tolerant', SR, 'Search tolerates typos, synonyms and plurals', 'Search should handle misspellings, synonyms, abbreviations and singular/plural, and support product codes.', 'Exact-match search fails many real queries.', 'Do misspelled or synonym queries return relevant results?', 'flow', 'major', 'website, app',
  'Baymard Institute e-commerce search research; Hearst, M. (2009). Search User Interfaces. Cambridge University Press.', N + '5', conf='medium')
X('search.no-dead-ends', SR, 'No-results pages offer a way forward', 'When there are no results, show spelling suggestions, related categories, popular items or contact options.', 'Zero-result dead ends cause abandonment.', 'Does a no-results page offer suggestions and next steps?', 'flow', 'major', 'website, app',
  'Hearst (2009); Baymard Institute research.', N + '9')
X('search.query-preserved', SR, 'Keep the query visible and editable', 'Show the query in the search box on the results page so users can refine it.', 'Refinement is common; retyping wastes effort.', 'Is the search query preserved in the input on the results page?', 'deterministic (DOM) + flow', 'minor', 'website, app',
  'Hearst (2009). Search User Interfaces.', N + '6')
X('search.autocomplete', SR, 'Offer query suggestions', 'Provide autocomplete suggestions that are keyboard-accessible and highlight the completed portion.', 'Suggestions reduce typing and guide users to effective queries.', 'Are search suggestions offered and keyboard-accessible?', 'flow', 'minor', 'website, app',
  'Baymard Institute autocomplete research; WAI-ARIA APG Combobox pattern.', N + '7', conf='medium')
X('search.facets', SR, 'Provide relevant filters and sorting for large result sets', 'Offer filters that match how users choose (price, size, availability, ratings), show applied filters, counts, and easy removal.',
  'Filters help users narrow large sets; hidden or irrelevant filters frustrate.', 'Can users filter and sort by the attributes that matter, and see/remove applied filters?', 'flow', 'major', 'e-commerce, catalogs',
  'Hearst (2006). Design recommendations for hierarchical faceted search interfaces. SIGIR Workshop; Baymard Institute research.', N + '7', conf='medium')

# ---------------- CONTENT ----------------
CT = 'Content & microcopy'
X('content.plain-language', CT, 'Use plain language', 'Write in short sentences with common words, active voice, and "you"; explain or avoid jargon and acronyms.', 'Plain language improves comprehension for everyone, including experts.', 'Is copy free of unexplained jargon, long sentences and passive voice?', 'screen', 'major', 'all',
  'Federal Plain Language Guidelines (2011); GOV.UK content design; WCAG 2.2 SC 3.1.3, 3.1.4, 3.1.5.', N + '2', threshold='Reading age ~9–12 / grade ≤ 8 for public audiences')
X('content.scannable', CT, 'Make content scannable', 'Use meaningful headings, short paragraphs, bulleted lists, and highlighted keywords; front-load the important words.',
  'Users read about 20–28% of words on a page; concise, scannable, objective text improved measured usability by 124% in Morkes & Nielsen’s study.', 'Can the key message be grasped by scanning headings and the first words of paragraphs?', 'screen', 'major', 'all',
  'Morkes, J. & Nielsen, J. (1997). Concise, SCANNABLE, and Objective: How to Write for the Web; Weinreich et al. (2008).', N + '8')
X('content.inverted-pyramid', CT, 'Put the most important information first', 'Lead with the conclusion or the user’s answer, then supporting details.', 'Users decide in seconds whether to continue reading.', 'Does each page/section start with the most important information?', 'screen', 'minor', 'all',
  'Nielsen (1996). Inverted Pyramids in Cyberspace. NN/g.', N + '8')
X('content.headings', CT, 'Headings are descriptive and hierarchical', 'Use one H1 per page that states the topic and a logical heading hierarchy without skipped levels.', 'Headings support scanning and screen reader navigation.', 'Is there a single descriptive H1 and a logical heading hierarchy?', 'deterministic (DOM) + screen', 'major', 'web',
  'WCAG 2.2 SC 1.3.1, 2.4.6, 2.4.10.', 'WCAG 2.4.6')
X('content.value-prop', CT, 'Homepage communicates what it is and why it matters within seconds', 'A visitor can tell what the organization/product does, who it is for, and what to do next from the first viewport.',
  'Users leave quickly if purpose is unclear; first impressions form in ~50 ms.', 'From the first viewport, can a new user tell what this is, who it is for, and what to do?', 'screen', 'critical', 'website, landing page',
  'Nielsen & Tahir (2001). Homepage Usability; Lindgaard et al. (2006).', N + '2')
X('content.microcopy-tone', CT, 'Tone fits the situation', 'Use a calm, respectful tone in errors and serious contexts; avoid jokes about money, health, failure or loss.', 'Inappropriate humor in serious moments erodes trust.', 'Is the tone appropriate in errors and high-stakes moments?', 'screen', 'minor', 'all',
  'Mailchimp Content Style Guide (2013, voice & tone); NN/g (2016) The Four Dimensions of Tone of Voice.', N + '2', conf='medium')
X('content.sentence-case', CT, 'Use sentence case and avoid ALL CAPS for long text', 'Use sentence case for headings, labels and buttons; avoid long passages in uppercase.', 'Uppercase text is slower to read and can read as shouting.', 'Is body text and are long labels in sentence case?', 'deterministic (computed styles) + screen', 'minor', 'all',
  'GOV.UK content design style guide; Tinker, M. A. (1963). Legibility of Print.', N + '8', conf='medium')
X('content.no-justify', CT, 'Avoid fully justified body text', 'Left-align body text in LTR languages; avoid justified text that creates uneven word spacing ("rivers").', 'Uneven spacing hampers reading, especially for people with dyslexia.', 'Is body text left-aligned (not justified)?', 'deterministic (computed styles)', 'minor', 'all',
  'WCAG 2.2 SC 1.4.8 Visual Presentation; British Dyslexia Association Style Guide.', 'WCAG 1.4.8')
X('content.numbers', CT, 'Format numbers, dates and money clearly', 'Use numerals, consistent units, locale-appropriate formats, and unambiguous dates (e.g., "4 June 2025").', 'Ambiguous formats cause errors across locales.', 'Are numbers, dates and currencies formatted clearly and consistently?', 'screen', 'minor', 'all',
  'GOV.UK style guide: Numbers and Dates; NHS: Numbers, measurements, dates and time.', N + '4')
X('content.freshness', CT, 'Show when content was updated', 'Show last-updated dates on time-sensitive content and remove outdated information.', 'Stale content harms credibility.', 'Do time-sensitive pages show when they were last updated?', 'screen', 'minor', 'website',
  'Fogg (2002). Stanford Web Credibility Guidelines #8.', 'Credibility')
X('content.alt-text', CT, 'Images have meaningful alternative text', 'Informative images have concise alt text that conveys their purpose; decorative images have empty alt.', 'Required for screen reader users and when images fail to load.', 'Do informative images have meaningful alt text and decorative ones empty alt?', 'deterministic (DOM) + screen', 'critical', 'web',
  'WCAG 2.2 SC 1.1.1; W3C WAI Images Tutorial (alt decision tree).', 'WCAG 1.1.1')
X('content.text-on-images', CT, 'Text over images remains legible', 'Ensure sufficient contrast for text over images using overlays, solid backgrounds or text shadows.', 'Busy backgrounds make text unreadable and fail contrast.', 'Is text over images legible with adequate contrast everywhere it overlaps?', 'screen', 'major', 'all',
  'WCAG 2.2 SC 1.4.3; common practice.', 'WCAG 1.4.3')
X('content.meta', CT, 'Pages have unique titles and meta descriptions', 'Each page has a unique, descriptive <title> (page – site) and meta description.', 'Titles orient users, appear in tabs, bookmarks and search results.', 'Does each page have a unique descriptive title and meta description?', 'deterministic (DOM)', 'minor', 'web',
  'WCAG 2.2 SC 2.4.2 Page Titled; Google Search Central documentation.', 'WCAG 2.4.2')
X('content.pdf', CT, 'Avoid PDFs for content meant to be read on screen', 'Publish information as HTML pages; offer PDFs only for printing or formal documents, and label them with file type and size.',
  'PDFs are hard to read on mobile, often inaccessible, and break navigation.', 'Is essential content locked in PDFs, and are file links labeled with type and size?', 'deterministic (links) + screen', 'minor', 'website',
  'Nielsen (2001/2020). Avoid PDF for On-Screen Reading. NN/g; GOV.UK (2018) Why GOV.UK content should be published in HTML and not PDF.', N + '4')

# ---------------- VISUAL DESIGN ----------------
VD = 'Visual design & layout'
X('visual.hierarchy', VD, 'Clear visual hierarchy with one primary focus per view', 'Use size, weight, color and position so the most important element and the primary action stand out; avoid competing focal points.',
  'Hierarchy guides attention and speeds comprehension (Von Restorff, preattentive processing).', 'Is there one clear visual focus and primary action per screen?', 'screen', 'major', 'all',
  'Treisman & Gelade (1980); von Restorff (1933); Few, S. & Lidwell, W. (2003) Universal Principles of Design.', N + '8')
X('visual.grouping', VD, 'Related items are grouped, unrelated items separated', 'Use proximity, common region and alignment to group related information and controls.', 'Gestalt grouping drives how users parse layouts.', 'Do spacing and containers reflect the logical grouping of content?', 'screen', 'minor', 'all',
  'Wertheimer (1923); Palmer (1992).', 'Gestalt')
X('visual.consistency', VD, 'Consistent components and styles', 'The same component looks and behaves the same everywhere (buttons, links, inputs, icons, spacing, type scale).', 'Inconsistency forces relearning and erodes trust.', 'Are buttons, links and inputs styled consistently across screens?', 'deterministic (style clustering) + screen', 'minor', 'all',
  'Nielsen #4; Shneiderman rule 1.', N + '4')
X('visual.affordance', VD, 'Interactive elements look interactive', 'Buttons look like buttons, links look like links, and non-interactive elements avoid interactive styling (e.g., underlined non-links, button-like labels).',
  'Flat designs with weak signifiers cause users to miss actions or click non-interactive elements.', 'Can users distinguish clickable from non-clickable elements?', 'screen', 'major', 'all',
  'Moran, K. (2017). Flat UI Elements Attract Less Attention and Cause Uncertainty. NN/g; Norman (2013) signifiers.', N + '6')
X('visual.icons-labeled', VD, 'Icons have text labels', 'Pair icons with visible text labels, especially for actions that are not universally understood; icon-only buttons need accessible names and tooltips.',
  'Few icons are universally understood (home, search, print); unlabeled icons are ambiguous.', 'Are non-universal icons accompanied by visible text labels?', 'screen', 'major', 'all',
  'Harley, A. (2014). Icon Usability. NN/g; Wiedenbeck, S. (1999). The use of icons and labels in an end user application program. BIT, 18(2), 68–82.', N + '6')
X('visual.color-not-only', VD, 'Do not rely on color alone', 'Convey status and meaning with text, icons or patterns in addition to color (errors, required fields, chart series).', 'About 8% of men have color vision deficiency.', 'Is any information conveyed by color alone?', 'screen', 'major', 'all',
  'WCAG 2.2 SC 1.4.1 Use of Color.', 'WCAG 1.4.1')
X('visual.contrast', VD, 'Text and UI contrast meets WCAG', 'Text contrast ≥ 4.5:1 (≥ 3:1 for large text); UI component boundaries and focus indicators ≥ 3:1.', 'Low contrast is the most common accessibility failure on the web.', 'Do all text and UI components meet contrast minimums?', 'deterministic (computed colors)', 'major', 'all',
  'WCAG 2.2 SC 1.4.3, 1.4.11; WebAIM Million report (annual).', 'WCAG 1.4.3', threshold='4.5:1 / 3:1')
X('visual.typography', VD, 'Readable typography', 'Body text ≥ 16 px, line height ~1.5, line length ~45–75 characters, sufficient paragraph spacing, and limited typefaces.', 'Classic legibility research and WCAG text presentation guidance.', 'Do body text size, line height and line length fall within readable ranges?', 'deterministic (computed styles)', 'minor', 'all',
  'Tinker, M. A. & Paterson, D. G. (1929–1940) legibility studies; Bringhurst (1992); WCAG 2.2 SC 1.4.8, 1.4.12.', N + '8', threshold='≥16px; 1.4–1.6; 45–75 chars')
X('visual.whitespace', VD, 'Adequate whitespace and density for the context', 'Use whitespace to separate groups and improve legibility; match density to the user (dense for expert tools, relaxed for consumer sites).', 'Crowded layouts increase visual complexity and lower first impressions.', 'Is density appropriate for the audience and are groups clearly separated?', 'screen', 'minor', 'all',
  'Tuch et al. (2012); Reinecke et al. (2013).', N + '8', conf='medium')
X('visual.layout-shift', VD, 'Content does not jump while loading', 'Reserve space for images, ads and embeds so content does not shift; avoid inserting content above what users are reading.', 'Layout shifts cause misclicks and lost place (CLS).', 'Does content shift during load or interaction?', 'deterministic (CLS)', 'major', 'web',
  'Google Core Web Vitals: CLS ≤ 0.1.', N + '1', threshold='CLS ≤ 0.1')
X('visual.dark-mode', VD, 'Support user color preferences', 'Respect prefers-color-scheme and system font size settings where feasible; ensure both themes meet contrast.', 'Users rely on system preferences for comfort and accessibility.', 'Does the interface respect dark mode and text-size preferences, with adequate contrast in both themes?', 'deterministic (media queries) + screen', 'minor', 'web, app',
  'CSS Media Queries Level 5; Apple HIG Dark Mode; WCAG 1.4.4.', 'Personalization', conf='medium')

# ---------------- FEEDBACK & STATUS ----------------
FB = 'Feedback & system status'
X('feedback.immediate', FB, 'Every action gets immediate feedback', 'Buttons and controls show pressed/loading states immediately; outcomes are confirmed.', 'Users repeat actions or abandon when nothing seems to happen (double submissions, duplicate payments).', 'Does every action give visible feedback within ~100 ms?', 'flow', 'major', 'all',
  'Nielsen #1; Miller (1968); Norman (1988).', N + '1', threshold='≤ 100 ms acknowledgement')
X('feedback.loading', FB, 'Show progress for waits longer than ~1 second', 'Use skeleton screens or spinners for 1–10 s, and determinate progress with time estimates and cancel for longer waits.', 'Unexplained waits feel longer and cause abandonment.', 'Do loading states appear for waits over ~1 s, with progress for longer operations?', 'flow', 'major', 'all',
  'Nielsen (1993) response times; Maister (1985); Harrison et al. (2007).', N + '1')
X('feedback.success', FB, 'Confirm success clearly', 'After important actions (payment, submission, save), show a clear confirmation with what happens next and a reference number where relevant.', 'Closure reduces anxiety and support contacts.', 'After key actions, is there a clear confirmation and next steps?', 'flow', 'major', 'all',
  'Shneiderman rule 4 (closure); GOV.UK Design System: Confirmation pages.', N + '1')
X('feedback.toasts', FB, 'Do not auto-dismiss important messages', 'Transient toasts must not carry critical information or actions; give enough time to read, allow pausing, and announce them to screen readers.', 'Auto-dismissed messages are missed, especially by slow readers and screen reader users.', 'Do any critical messages or actions disappear automatically?', 'flow', 'major', 'all',
  'WCAG 2.2 SC 2.2.1 Timing Adjustable, 4.1.3 Status Messages; Material Design snackbar guidance.', 'WCAG 4.1.3', conf='medium')
X('feedback.status-messages', FB, 'Status messages are announced to assistive tech', 'Use live regions (role=status/alert) for dynamic messages such as "added to cart" or validation results.', 'Screen reader users otherwise miss updates.', 'Are dynamic status messages exposed via live regions?', 'deterministic (DOM)', 'major', 'web',
  'WCAG 2.2 SC 4.1.3 Status Messages.', 'WCAG 4.1.3')
X('feedback.empty-states', FB, 'Design empty states', 'Empty screens explain what will appear, why it is empty, and how to get started (with a primary action).', 'Blank screens look broken and stall new users.', 'Do empty states explain and offer a next step?', 'screen', 'minor', 'app',
  'Hurff (2015) UI Stack; Primer/Carbon empty states patterns.', N + '10')
X('feedback.system-state', FB, 'Show saved/unsaved and sync state', 'Indicate when data is saving, saved, offline or out of sync.', 'Users need to trust that work is preserved.', 'Is save/sync state visible in editors and long forms?', 'screen', 'minor', 'app',
  'Tognazzini: Protect users\' work; Primer: Saving pattern.', N + '1', conf='medium')

# ---------------- ERRORS & CONTROL ----------------
ER = 'Errors & recovery'
X('error.undo', ER, 'Prefer undo to confirmation for routine actions', 'Offer undo for deletions and changes where feasible; reserve confirmation dialogs for irreversible, high-impact actions.', 'Confirmations get habituated and clicked through (Raskin); undo protects without slowing users.', 'Can users undo routine destructive actions (delete, archive, send)?', 'flow', 'major', 'app',
  'Raskin (2000); Shneiderman rule 6.', N + '3')
X('error.destructive-confirm', ER, 'Irreversible actions require deliberate confirmation', 'Destructive irreversible actions (delete account, cancel order, permanent data loss) explain consequences and require explicit confirmation naming the action.', 'Prevents costly slips.', 'Do irreversible actions explain consequences and require an explicit, specifically labeled confirmation?', 'flow', 'critical', 'all',
  'Nielsen #5; WCAG 2.2 SC 3.3.4.', N + '5')
X('error.destructive-separation', ER, 'Separate destructive actions from frequent ones', 'Place destructive actions away from common actions, and style them distinctly (e.g., not the default/primary style).', 'Adjacent destructive buttons cause slips (Fitts, slips).', 'Are destructive actions visually and spatially separated from common actions?', 'screen', 'major', 'all',
  'Norman (1981) slips; Fitts (1954).', N + '5')
X('error.exits', ER, 'Users can always exit, cancel or go back', 'Every modal, flow and wizard has a clear way to cancel or go back without losing work unexpectedly.', 'Trapped users abandon or make mistakes.', 'Can users cancel/close any flow, modal or wizard and go back a step?', 'flow', 'major', 'all',
  'Nielsen #3; WCAG 2.1.2 No Keyboard Trap.', N + '3')
X('error.timeouts', ER, 'Warn before session timeouts and allow extension', 'Warn users before a session times out, allow them to extend, and preserve data if it expires.', 'Timeouts destroy work and disproportionately affect disabled and slower users.', 'Are users warned and allowed to extend before timeouts, with data preserved?', 'flow', 'major', 'web app, forms',
  'WCAG 2.2 SC 2.2.1, 2.2.6; GOV.UK timeout warning pattern.', 'WCAG 2.2.1')
X('error.offline', ER, 'Handle offline and network errors gracefully', 'Explain connectivity problems, retry automatically where safe, and never silently lose user input.', 'Mobile networks fail often.', 'Is there a clear message and retry path when the network fails, without data loss?', 'flow', 'major', 'app, web app',
  'Primer: Degraded experiences pattern; Google Offline UX considerations (web.dev).', N + '9', conf='medium')
X('error.double-submit', ER, 'Prevent double submissions', 'Disable or debounce submit after the first click while processing, and show progress; make payment endpoints idempotent.', 'Slow responses lead to repeated clicks and duplicate orders/payments.', 'Does a second click during processing cause a duplicate action?', 'flow', 'critical', 'checkout, forms',
  'GOV.UK Design System: Button (prevent double click); common engineering practice.', N + '5')

# ---------------- MOBILE & TOUCH ----------------
MB = 'Mobile & touch'
X('mobile.zoom-allowed', MB, 'Pinch-zoom is not disabled', 'Do not set user-scalable=no or maximum-scale=1 in the viewport meta tag.', 'Low-vision users need to zoom; disabling it fails WCAG 1.4.4.', 'Does the viewport meta tag allow zooming?', 'deterministic (DOM)', 'major', 'mobile web',
  'WCAG 2.2 SC 1.4.4 Resize Text; axe-core rule meta-viewport.', 'WCAG 1.4.4')
X('mobile.responsive', MB, 'Layout adapts to small screens without horizontal scrolling', 'Content reflows at 320 CSS px width without horizontal scrolling or loss of content.', 'Required by WCAG 1.4.10; core to mobile usability.', 'Does the layout reflow at 320 px without horizontal scrolling?', 'deterministic (viewport test)', 'major', 'web',
  'WCAG 2.2 SC 1.4.10 Reflow.', 'WCAG 1.4.10')
X('mobile.touch-targets', MB, 'Touch targets are large enough and spaced', 'Interactive targets ≥ 44×44 pt / 48×48 dp, or at minimum 24×24 CSS px with spacing.', 'Small targets cause mis-taps, especially for motor-impaired users.', 'Are touch targets large and spaced enough?', 'deterministic (bounding boxes)', 'major', 'mobile',
  'WCAG 2.2 SC 2.5.8 / 2.5.5; Apple HIG; Material Design; Parhi et al. (2006).', 'WCAG 2.5.8', threshold='≥ 24 CSS px (min); 44–48 recommended')
X('mobile.thumb-reach', MB, 'Primary actions within thumb reach', 'Place frequent and primary actions in the lower part of the screen or a sticky bottom bar on mobile.', 'Many users hold phones one-handed; top corners are hard to reach.', 'On mobile, are primary actions reachable without stretching (bottom area or sticky CTA)?', 'screen', 'minor', 'mobile',
  'Hoober (2013); Wroblewski (2012) Mobile First.', 'Fitts', conf='medium')
X('mobile.sticky-cta', MB, 'Key actions remain available while scrolling on long mobile pages', 'On long mobile pages (product pages, menus, landing pages), keep the main action (Buy, Book, Call, Order) accessible via a sticky bar.', 'Users should not have to scroll back to find the action.', 'Is the main action accessible at any scroll position on mobile?', 'screen', 'minor', 'mobile',
  'Baymard Institute mobile e-commerce research; common practice.', N + '7', conf='medium')
X('mobile.no-hover', MB, 'Do not depend on hover', 'Any information or action available on hover must also be available on tap/focus.', 'Touch devices have no hover; WCAG 1.4.13 governs hover content.', 'Is any content or action available only on hover?', 'flow', 'major', 'web',
  'WCAG 2.2 SC 1.4.13; common practice.', 'WCAG 1.4.13')
X('mobile.gestures-alternatives', MB, 'Gestures have simple alternatives', 'Multipoint or path-based gestures (pinch, swipe paths) and dragging have single-pointer alternatives (buttons).', 'Required by WCAG 2.5.1 and 2.5.7; hidden gestures lack signifiers.', 'Can every gesture- or drag-based action be performed with a simple tap?', 'flow', 'major', 'mobile, web',
  'WCAG 2.2 SC 2.5.1 Pointer Gestures, 2.5.7 Dragging Movements.', 'WCAG 2.5.1')
X('mobile.interstitials', MB, 'Avoid intrusive interstitials and pop-ups', 'Do not cover content with pop-ups on arrival (newsletter, app install) especially on mobile; use small banners.', 'Intrusive interstitials harm usability and Google ranking (2017).', 'Does a pop-up or interstitial cover the main content on arrival?', 'screen', 'major', 'mobile web',
  'Google Search Central (2016). Helping users easily access content on mobile (intrusive interstitials); NN/g (2015) The Most Hated Online Advertising Techniques.', N + '8')
X('mobile.orientation', MB, 'Support both orientations', 'Do not lock content to portrait or landscape unless essential.', 'Users with mounted devices cannot rotate them.', 'Does content work in both orientations?', 'deterministic (viewport test)', 'minor', 'mobile',
  'WCAG 2.2 SC 1.3.4 Orientation.', 'WCAG 1.3.4')
X('mobile.tap-to-call', MB, 'Phone numbers and addresses are actionable', 'Mark phone numbers as tel: links and link addresses to maps on mobile.', 'Saves users from copying information manually.', 'Are phone numbers tappable and addresses linked to maps?', 'deterministic (DOM)', 'minor', 'mobile, local business',
  'Common practice; Google local business UX guidance.', N + '7', conf='medium')

# ---------------- ONBOARDING, ACCOUNTS & AUTH ----------------
OB = 'Onboarding & first use'
X('onboard.value-first', OB, 'Show value before asking for signup', 'Let users explore or try core value before requiring an account (gradual engagement / lazy registration).', 'Forced early registration causes abandonment.', 'Can users experience the core value before creating an account?', 'flow', 'major', 'app, SaaS',
  'Wroblewski, L. (2008). Gradual Engagement Boosts Twitter Sign-up; Hoekman, R. (2007).', N + '7', conf='medium')
X('onboard.guest-checkout', OB, 'Offer guest checkout', 'Do not force account creation to purchase; offer account creation after checkout.', 'Forced account creation is consistently among the top reasons for checkout abandonment (about a quarter of abandoners in Baymard surveys).', 'Can users buy without creating an account?', 'flow', 'critical', 'e-commerce',
  'Baymard Institute (ongoing). Reasons for abandonment during checkout; Spool, J. (2009). The $300 Million Button. UIE.', N + '7', conf='medium')
X('onboard.tutorials', OB, 'Prefer contextual help over up-front tutorials', 'Avoid long mandatory tours; teach in context at the moment of need and make tours skippable.', 'Users skip tutorials and forget them; the paradox of the active user.', 'Is onboarding skippable and is guidance provided in context?', 'flow', 'minor', 'app',
  'Carroll & Rosson (1987); Joyce, A. (2020). Mobile-App Onboarding: An Analysis of Components and Techniques. NN/g.', N + '10', conf='medium')
X('onboard.permissions', OB, 'Request permissions in context', 'Ask for notifications, location, camera or contacts at the moment they are needed, explaining the benefit; never on first launch without context.', 'Out-of-context requests get denied and cannot easily be re-asked.', 'Are permission requests made in context with an explanation?', 'flow', 'major', 'mobile app, web',
  'Apple HIG: Requesting permission; Google Android permissions best practices.', N + '2')
X('auth.passkeys', 'Authentication, security & privacy', 'Offer low-friction authentication', 'Offer passkeys, magic links, social or SSO sign-in and OTP autofill; avoid forcing users to memorize or transcribe.', 'Passwords are a major source of friction and lockouts; WCAG 3.3.8 forbids cognitive tests without alternatives.', 'Is there a sign-in method that requires no memorization or transcription?', 'flow', 'major', 'authentication',
  'FIDO Alliance (2022). Passkeys; WCAG 2.2 SC 3.3.8.', 'WCAG 3.3.8', conf='medium')
X('auth.recovery', 'Authentication, security & privacy', 'Account recovery is easy and secure', 'Provide clear "forgot password" links near the password field, send reset links (not reminders), and avoid security questions.', 'Lockouts are a top support cost; security questions are insecure and hard to remember.', 'Is password recovery easy to find and secure (links, no security questions)?', 'flow', 'major', 'authentication',
  'GOV.UK Design System: Passwords pattern; NIST SP 800-63B-4.', N + '9')
X('auth.errors-specific', 'Authentication, security & privacy', 'Sign-in errors help users recover', 'Tell users which field to check where it does not create account enumeration risk, show lockout rules before lockout, and offer recovery.', 'Generic errors leave users stuck.', 'Do sign-in errors offer a recovery path?', 'flow', 'minor', 'authentication', 'GOV.UK Design System: Passwords pattern ("handling incorrect login attempts").', N + '9', conf='medium')

# ---------------- E-COMMERCE & CHECKOUT ----------------
EC = 'E-commerce & checkout'
X('ecom.total-price', EC, 'Show the full price early', 'Show total cost including mandatory fees, taxes (where applicable) and shipping costs as early as possible; never add mandatory fees at the last step.',
  'Unexpected extra costs are the top reported reason for cart abandonment, and drip pricing is regulated (e.g., FTC Rule on Unfair or Deceptive Fees 2025 for live-event tickets and short-term lodging; EU consumer law).', 'Is the full price (incl. mandatory fees) visible before checkout?', 'flow', 'critical', 'e-commerce, booking',
  'Baymard Institute abandonment survey (ongoing); FTC (2024). Trade Regulation Rule on Unfair or Deceptive Fees; EU Consumer Rights Directive 2011/83/EU.', 'Ethics; hidden costs')
X('ecom.shipping-info', EC, 'Shipping cost and delivery date visible on product pages', 'Show delivery cost (or free threshold) and estimated delivery date before checkout.', 'Uncertainty about delivery drives abandonment.', 'Are shipping costs and delivery dates visible before checkout?', 'screen', 'major', 'e-commerce',
  'Baymard Institute product page research.', N + '1', conf='medium')
X('ecom.product-images', EC, 'Product images are large, multiple and zoomable', 'Provide several high-resolution images (including scale/in-use), zoom, and video where helpful.', 'Images are the primary way users evaluate products online.', 'Are there multiple, zoomable product images showing scale?', 'screen', 'major', 'e-commerce',
  'Baymard Institute product page research; NN/g (2014) Photos as Web Content.', N + '2', conf='medium')
X('ecom.reviews', EC, 'Show genuine reviews, including negative ones', 'Display ratings distribution and allow filtering; do not hide negative reviews or fabricate reviews.', 'Users seek negative reviews to judge risk; fake reviews are illegal (FTC 2024 rule on fake reviews).', 'Are reviews genuine, with distribution and negative reviews visible?', 'screen', 'major', 'e-commerce',
  'FTC (2024). Trade Regulation Rule on the Use of Consumer Reviews and Testimonials; Baymard Institute reviews research.', 'Ethics', conf='medium')
X('ecom.cart-persistence', EC, 'Cart persists and is easy to edit', 'Keep cart contents across sessions/devices, allow quantity changes and removal, and show a running total.', 'Users use carts as wish lists and return later.', 'Is the cart persistent and editable with a clear total?', 'flow', 'minor', 'e-commerce', 'Baymard Institute cart research.', N + '3', conf='medium')
X('ecom.trust-payment', EC, 'Reinforce trust at payment', 'Show recognized payment options, security reassurance near card fields, and clear return/refund policies.', 'Concern about card security is a common abandonment reason.', 'Are security cues and return policies visible at payment?', 'screen', 'major', 'e-commerce',
  'Baymard Institute (2016+) perceived security of payment form; Fogg (2002).', 'Credibility', conf='medium')
X('ecom.express-pay', EC, 'Offer express payment options', 'Offer digital wallets (Apple Pay, Google Pay, PayPal) to reduce form filling, especially on mobile.', 'Reduces typing and errors.', 'Are express payment options available?', 'screen', 'minor', 'e-commerce', 'Common practice; Baymard Institute mobile checkout research.', N + '7', conf='medium')
X('ecom.cancel-easy', EC, 'Cancellation is as easy as sign-up', 'Allow online cancellation through a simple path at least as easy as signing up; make terms of auto-renewal clear and send reminders.', 'Hard-to-cancel flows are a deceptive pattern; prohibited under EU DSA Art. 25 and several US state laws (e.g., California automatic renewal law amendments 2024).', 'Can users cancel online with comparable ease to signing up?', 'flow', 'critical', 'subscriptions',
  'EU DSA Art. 25(3)(c); California Bus. & Prof. Code §17602 (amended 2024); FTC enforcement (ROSCA). Note: the FTC "Click-to-Cancel" rule (2024) was vacated by the 8th Circuit in July 2025.', 'Ethics; hard to cancel')
X('ecom.size-guides', EC, 'Provide fit and specification details', 'Provide size guides, dimensions, materials and compatibility information in scannable form.', 'Missing specs drive returns and abandonment.', 'Are key specs and size information easy to find?', 'screen', 'minor', 'e-commerce', 'Baymard Institute product page research.', N + '2', conf='medium')

# ---------------- TRUST, PRIVACY & ETHICS ----------------
TR = 'Trust & credibility'
X('trust.contact', TR, 'Contact information is easy to find', 'Provide phone, email, physical address and support hours in obvious places (header/footer/contact page).', 'Showing a real organization behind the site raises credibility.', 'Can users find contact details within one click?', 'screen', 'major', 'website',
  'Fogg (2002). Stanford Web Credibility Guidelines #2 and #5.', 'Credibility')
X('trust.business-info', TR, 'Key business info is not buried', 'Opening hours, location, prices and availability (for local businesses) are visible on the homepage or one click away.', 'These are top tasks for local businesses.', 'Are hours, address and phone visible without digging (e.g., not only in the footer)?', 'screen', 'major', 'local business',
  'Common practice; Google Business Profile guidance.', N + '6', conf='medium')
X('privacy.cookie-banner', 'Authentication, security & privacy', 'Cookie consent offers a genuine choice', 'Offer "Reject all" with equal prominence to "Accept all" on the first layer; no pre-ticked purposes; consent is as easy to withdraw as to give.', 'Required under GDPR/ePrivacy as interpreted by regulators; asymmetric banners are deceptive design.', 'Is "Reject all" as easy and visible as "Accept all"?', 'screen', 'critical', 'web',
  'EDPB (2023). Report of the Cookie Banner Taskforce; CNIL (2020) Guidelines on cookies; CJEU Planet49 (2019).', 'Ethics; GDPR')
X('privacy.just-in-time', 'Authentication, security & privacy', 'Explain data use at the point of collection', 'Explain why personal data is needed and how it will be used right where it is requested.', 'Transparency builds trust and is required by GDPR Art. 13.', 'Is the purpose of personal data requests explained in context?', 'screen', 'major', 'forms',
  'GDPR Art. 12–13; ICO guidance on the right to be informed.', 'GDPR')
X('ethics.no-dark-patterns', 'Ethics / deceptive patterns', 'No deceptive patterns', 'The interface must not use fake urgency, fake scarcity, confirmshaming, sneaking, preselection, nagging, obstruction or disguised ads.', 'Deceptive patterns harm users and are increasingly illegal.', 'Is the interface free of known deceptive patterns? (see dark pattern taxonomy)', 'screen / flow', 'critical', 'all',
  'Mathur et al. (2019); Gray et al. (2018); EU DSA Art. 25; FTC (2022).', 'Ethics')

# ---------------- ACCESSIBILITY extras ----------------
AC = 'Accessibility'
X('a11y.keyboard', AC, 'Everything works with a keyboard', 'All functionality is operable by keyboard with a logical focus order and no keyboard traps.', 'Essential for keyboard, switch and screen reader users.', 'Can all functionality be reached and operated by keyboard in a logical order?', 'flow', 'critical', 'web',
  'WCAG 2.2 SC 2.1.1, 2.1.2, 2.4.3.', 'WCAG 2.1.1')
X('a11y.focus-visible', AC, 'Focus is always visible and not obscured', 'Keyboard focus has a clearly visible indicator and is not hidden behind sticky headers, cookie banners or chat widgets.', 'Users must see where they are.', 'Is focus clearly visible and never fully hidden?', 'flow', 'major', 'web',
  'WCAG 2.2 SC 2.4.7, 2.4.11.', 'WCAG 2.4.7')
X('a11y.names', AC, 'Controls have accessible names', 'Buttons, links, inputs, icons and frames have programmatic names that match visible labels.', 'Screen reader and voice control users depend on names.', 'Do all interactive elements and iframes have accessible names matching visible labels?', 'deterministic (axe)', 'critical', 'web',
  'WCAG 2.2 SC 4.1.2, 2.5.3; axe-core rules button-name, link-name, frame-title.', 'WCAG 4.1.2')
X('a11y.modals', AC, 'Modals manage focus correctly', 'Opening a dialog moves focus into it, traps focus while open, closes with Escape, and returns focus to the trigger on close.', 'Otherwise keyboard and screen reader users get lost.', 'Do dialogs move, contain and restore focus, and close with Escape?', 'flow', 'major', 'web',
  'WAI-ARIA APG Dialog (Modal) pattern.', 'WCAG 2.4.3')
X('a11y.reduced-motion', AC, 'Respect reduced-motion preferences', 'Honor prefers-reduced-motion; avoid parallax and large motion triggered by interaction, or allow disabling it.', 'Motion can cause vestibular disorders symptoms.', 'Does the site honor prefers-reduced-motion and avoid non-essential motion?', 'deterministic (CSS) + screen', 'minor', 'web',
  'WCAG 2.2 SC 2.3.3 Animation from Interactions; Media Queries Level 5.', 'WCAG 2.3.3')
X('a11y.captions', AC, 'Video has captions and audio has transcripts', 'Provide captions for prerecorded video with audio, transcripts for audio, and audio description where needed.', 'Deaf and hard-of-hearing users, and users in sound-off contexts, need captions.', 'Do videos have accurate captions?', 'screen', 'critical', 'media',
  'WCAG 2.2 SC 1.2.2, 1.2.1, 1.2.5.', 'WCAG 1.2.2')
X('a11y.lang', AC, 'Page language is declared', 'Set the lang attribute on html and on passages in other languages.', 'Screen readers need it to pronounce correctly.', 'Is the page language declared?', 'deterministic (DOM)', 'major', 'web', 'WCAG 2.2 SC 3.1.1, 3.1.2.', 'WCAG 3.1.1')
X('a11y.statement', AC, 'Publish an accessibility statement', 'Provide an accessibility statement with conformance status, known issues and contact for feedback.', 'Required for public sector in EU/UK; builds trust.', 'Is there an accessibility statement?', 'deterministic (links)', 'minor', 'website',
  'EU Web Accessibility Directive 2016/2102; UK PSBAR 2018; W3C WAI Developing an Accessibility Statement.', 'Compliance', conf='medium')

# ---------------- AI & CONVERSATIONAL ----------------
AI = 'AI & automation'
X('ai.disclose', AI, 'Disclose AI involvement', 'Clearly indicate when content or responses are AI-generated and when users are talking to a bot.', 'Users calibrate trust differently for AI; disclosure is required in some jurisdictions (EU AI Act Art. 50 transparency obligations).', 'Is it clear when content or a conversation is AI-generated?', 'screen', 'major', 'AI features',
  'Amershi et al. (2019) G1; EU AI Act (Regulation (EU) 2024/1689) Art. 50.', 'HAX G1')
X('ai.capabilities', AI, 'Set expectations about capabilities and limits', 'Explain what the AI can and cannot do and how accurate it is likely to be, with examples of good requests.', 'Mismatched expectations cause misuse and distrust.', 'Does the AI feature explain its capabilities and limitations?', 'screen', 'major', 'AI features', 'Amershi et al. (2019) G1–G2; Google PAIR (2019).', 'HAX G1–G2')
X('ai.sources', AI, 'Show sources and confidence for AI outputs', 'Cite sources for factual claims, show uncertainty, and make verification easy.', 'Counters automation bias and hallucination risk.', 'Do AI answers show sources or confidence so users can verify?', 'screen', 'major', 'AI features', 'Amershi et al. (2019) G11; Parasuraman & Riley (1997).', 'HAX G11')
X('ai.control', AI, 'Users can edit, regenerate, stop and undo AI actions', 'Provide stop generation, edit prompt, regenerate, and undo for AI-applied changes; require confirmation before AI takes consequential actions.', 'Supports efficient correction and dismissal; keeps humans in control.', 'Can users stop, edit, regenerate and undo AI outputs/actions?', 'flow', 'major', 'AI features', 'Amershi et al. (2019) G7–G9, G17; Bainbridge (1983).', 'HAX G8–G9')
X('ai.feedback', AI, 'Collect granular feedback on AI output', 'Offer lightweight feedback (thumbs, corrections) and explain how it is used.', 'Supports improvement and user agency.', 'Can users give feedback on AI outputs?', 'screen', 'minor', 'AI features', 'Amershi et al. (2019) G15–G16.', 'HAX G15')
X('ai.human-handoff', AI, 'Provide a path to a human', 'Conversational agents offer an escape to human help, especially after repeated failure or for sensitive issues.', 'Users trapped with bots become frustrated.', 'Can users reach a human from the bot?', 'flow', 'major', 'chatbots', 'Langevin et al. (2021); common practice.', 'User control')
X('ai.context', AI, 'Preserve conversation context', 'The agent remembers context within a session (and across sessions where appropriate and disclosed), so users do not repeat themselves.', 'Repetition is a top complaint about chatbots.', 'Does the agent maintain context across turns?', 'flow', 'minor', 'chatbots', 'Langevin et al. (2021) context preservation; Amershi et al. (2019) G12.', 'HAX G12')
X('voice.prompts', AI, 'Voice prompts are short with few options', 'Keep spoken prompts brief, offer about three options at a time, put the most important information last, allow barge-in, and confirm critical inputs.', 'Audio is linear and taxes working memory.', 'Are voice prompts short with limited options and confirmation for critical inputs?', 'flow', 'major', 'voice', 'Cohen, M., Giangola, J., & Balogh, J. (2004). Voice User Interface Design. Addison-Wesley; Baddeley & Hitch (1974).', 'Working memory', conf='medium')

# ---------------- DATA DISPLAY ----------------
DT = 'Data display & tables'
X('data.tables', DT, 'Tables are scannable and accessible', 'Use proper header cells, right-align numbers, keep headers visible on scroll, allow sorting where useful, and avoid tables for layout.', 'Supports comparison and screen readers.', 'Are data tables marked up with headers, numbers right-aligned, and sortable where useful?', 'deterministic (DOM) + screen', 'minor', 'data-heavy UI',
  'WCAG 2.2 SC 1.3.1; Enders, J. (2008) Zebra striping: does it really help? A List Apart; GOV.UK Design System: Table.', 'WCAG 1.3.1', conf='medium')
X('data.charts-zero', DT, 'Charts represent data honestly', 'Bar charts start at zero; axes are labeled; scales are consistent across compared charts; avoid 3D and dual axes that mislead.', 'Misleading charts distort decisions (lie factor).', 'Do charts start bars at zero, label axes and avoid distortion?', 'screen', 'major', 'dashboards',
  'Tufte (1983); Cleveland & McGill (1984).', 'Tufte')
X('data.direct-labels', DT, 'Label data directly and use accessible palettes', 'Prefer direct labels over legends, use color-blind-safe palettes, and provide data tables or text alternatives.', 'Reduces split attention and supports color-blind and screen reader users.', 'Are charts directly labeled, color-blind safe, and accompanied by text alternatives?', 'screen', 'minor', 'dashboards',
  'Chandler & Sweller (1991) split attention; WCAG 1.1.1, 1.4.1; Carbon data visualization guidelines.', 'WCAG 1.4.1')
X('data.dashboard', DT, 'Dashboards answer the key question at a glance', 'Lead with the few most important metrics, show comparison/context (targets, trends), and allow drill-down.', 'Situation awareness requires perception, comprehension and projection.', 'Can users tell from the top of the dashboard whether things are OK and what changed?', 'screen', 'major', 'dashboards',
  'Few, S. (2006). Information Dashboard Design. O\'Reilly; Endsley (1995); Shneiderman (1996).', 'Endsley SA')

# ---------------- PERFORMANCE ----------------
PF = 'Performance'
X('perf.cwv', PF, 'Meet Core Web Vitals', 'LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at the 75th percentile.', 'Slow pages lose users; Google uses CWV as a ranking signal.', 'Does the page meet Core Web Vitals thresholds?', 'deterministic (Lighthouse/CrUX)', 'major', 'web', 'Google web.dev Web Vitals.', N + '1', threshold='LCP ≤ 2.5 s; INP ≤ 200 ms; CLS ≤ 0.1')
X('perf.perceived', PF, 'Optimize perceived performance', 'Show content progressively (skeletons, above-the-fold first), use optimistic updates for low-risk actions, and avoid blank screens.', 'Perceived speed matters as much as measured speed.', 'Does the UI render useful content progressively instead of a blank screen?', 'flow', 'minor', 'all',
  'Nielsen (1993); Harrison et al. (2007); Maister (1985).', N + '1', conf='medium')
X('perf.media-weight', PF, 'Optimize images and media', 'Serve responsive, compressed images in modern formats, lazy-load below-the-fold media, and avoid autoplaying heavy video.', 'Heavy pages are slow on mobile networks and cost users data.', 'Are images responsive, compressed and lazy-loaded?', 'deterministic (Lighthouse)', 'minor', 'web', 'Google Lighthouse audits; web.dev image guidance.', N + '1')

# ---------------- INTERNATIONALIZATION ----------------
IN = 'Internationalization'
X('i18n.language-selector', IN, 'Language selector is findable and uses native names', 'Show languages in their own names (e.g., "Español"), not flags, in a consistent location.', 'Flags represent countries, not languages.', 'Is the language switcher easy to find and labeled with native language names?', 'screen', 'minor', 'multilingual sites',
  'W3C i18n; GOV.UK Design System: Language navigation (Welsh); USWDS: Language selector.', N + '2', conf='medium')
X('i18n.rtl-expansion', IN, 'Layouts handle text expansion and RTL', 'Allow labels and buttons to grow (30–40%+), avoid text in images, and mirror layouts for right-to-left languages.', 'Fixed widths truncate translations.', 'Do layouts tolerate longer translations and RTL scripts?', 'screen', 'minor', 'multilingual', 'W3C i18n guidelines; IBM Globalization guidelines.', 'i18n', conf='medium')

# ---------------- MOTION ----------------
MO = 'Motion & animation'
X('motion.purposeful', MO, 'Motion is purposeful and brief', 'Use animation to show relationships, state changes and continuity, with short durations (~100–500 ms) and easing; never block interaction with animation.', 'Gratuitous motion distracts and delays; purposeful motion aids comprehension.', 'Do animations serve a purpose and complete quickly without blocking?', 'screen', 'minor', 'all',
  'Material Design motion guidance; NN/g (2020) Executing UX Animations: Duration and Motion Characteristics; Disney 12 principles (Thomas & Johnston 1981).', 'Feedback', threshold='~100–500 ms', conf='medium')
X('motion.autoplay', MO, 'No autoplaying audio/video with sound', 'Media does not autoplay with sound; moving content can be paused.', 'Autoplay startles users, interferes with screen readers and consumes data.', 'Does any media autoplay with sound or move without a pause control?', 'deterministic (DOM) + screen', 'major', 'web', 'WCAG 2.2 SC 1.4.2, 2.2.2.', 'WCAG 1.4.2')

# ---------------- FLOW-LEVEL ----------------
FL = 'Flow & task efficiency'
X('flow.steps', FL, 'Minimize steps to complete top tasks', 'Remove unnecessary steps, pages, clicks and decisions from top tasks; each step must be a clear, mindless choice.', 'Each step adds friction and drop-off; clarity of each click matters more than count (Krug).', 'Can top tasks be completed without unnecessary steps or ambiguous choices?', 'flow', 'major', 'all',
  'Krug (2000); Bastien & Scapin (1993) minimal actions; KLM (Card et al. 1980).', N + '7')
X('flow.dead-ends', FL, 'No dead ends', 'Every screen offers a clear next step or way back; confirmation and error pages include onward links.', 'Dead ends stall users and increase abandonment.', 'Does every screen offer a clear next step?', 'flow', 'major', 'all', 'Nielsen #3; common practice.', N + '3')
X('flow.next-step', FL, 'The next step is always clear', 'On each screen, the primary next action is obvious and labeled with what it does.', 'Unclear next steps cause hesitation and drop-off.', 'Is the primary next action obvious on each screen?', 'flow', 'major', 'all', 'Cognitive walkthrough (Wharton et al. 1994).', 'Cognitive walkthrough')
X('flow.context-switching', FL, 'Avoid forcing users across channels or platforms', 'Users can complete a task in one place without being sent to multiple platforms, PDFs or phone calls without guidance.', 'Fragmented journeys increase effort and drop-off (whole-service design).', 'Can users complete the task in one channel, with guidance when they must switch?', 'flow', 'major', 'services',
  'GOV.UK Service Standard points 2–3.', 'Service design')
X('flow.save-resume', FL, 'Long tasks can be saved and resumed', 'Allow saving progress and resuming later (with clear instructions) for long applications and setups.', 'Users get interrupted; the Ovsiankina effect shows they want to resume.', 'Can users save and resume long tasks?', 'flow', 'minor', 'forms, applications', 'GOV.UK Design System: Save and return (pattern work); Ovsiankina (1928).', N + '3', conf='medium')
X('flow.signup-friction', FL, 'Signup asks for the minimum', 'Signup requests only essential fields (often just email and password or SSO), deferring profile details.', 'Each extra field reduces conversion.', 'Does signup ask only for essential information?', 'flow', 'major', 'app, SaaS', 'Wroblewski (2008) Web Form Design; Hoekman (2007).', N + '8', conf='medium')
write('curated_rules', R)
