from common import *
R = []
def T(tax_id, tax_name, author, year, cite, items, conf='high', url=''):
    for i, it in enumerate(items, 1):
        name, desc = it[0], it[1]
        check = it[2] if len(it) > 2 else f'Is the interface free of "{name}"?'
        R.append(C(f'dp.{tax_id}.{i:02d}', f'{tax_name}: {name}', author, year, desc,
                   'Deceptive or manipulative design harms users, erodes trust and is increasingly illegal (FTC Act §5, EU DSA Art. 25, EU UCPD, GDPR consent rules, CPRA, India CCPA guidelines 2023).',
                   check, 'screen / flow', '', cite, 'Ethics / deceptive patterns', tax_name, conf=conf, url=url,
                   source_set='Curated: deceptive (dark) pattern taxonomies', sev='critical'))

T('brignull2010', 'Brignull original types (2010)', 'Harry Brignull', 2010, 'Brignull, H. (2010). Dark Patterns: dirty tricks designers use to make people do stuff. darkpatterns.org (now deceptive.design).', [
    ('Trick questions', 'Wording that misleads users into giving an answer they did not intend (e.g., double negatives in opt-out checkboxes).'),
    ('Sneak into basket', 'Adding items to the cart without the user’s explicit consent, often via a pre-checked option on a previous page.'),
    ('Roach motel', 'Easy to get into a situation (subscription) but hard to get out of.'),
    ('Privacy Zuckering', 'Tricking users into publicly sharing more personal information than intended.'),
    ('Price comparison prevention', 'Making it hard to compare prices between items so users cannot make an informed decision.'),
    ('Misdirection', 'Design that purposefully focuses attention on one thing to distract from another.'),
    ('Hidden costs', 'Unexpected charges appear at the last step of checkout.'),
    ('Bait and switch', 'The user sets out to do one thing, but a different, undesirable thing happens instead.'),
    ('Confirmshaming', 'Guilting the user into opting in; the decline option is worded to shame.'),
    ('Disguised ads', 'Ads disguised as content or navigation so users click them.'),
    ('Forced continuity', 'A free trial silently converts to a paid subscription without warning, and cancellation is hard.'),
    ('Friend spam', 'The product asks for contacts or social permissions for a stated reason, then spams the user’s contacts.'),
], url='https://www.deceptive.design/types')
T('deceptive-design-2023', 'Deceptive.design types (2023 revision)', 'Harry Brignull et al.', 2023, 'Brignull, H., Leiser, M., Santos, C., & Doshi, K. (2023). Deceptive patterns – user interfaces designed to trick you. deceptive.design.', [
    ('Comparison prevention', 'Making it hard to compare products by obscuring features or prices.'),
    ('Confirmshaming', 'Using guilt or shame to steer users away from declining an option.'),
    ('Disguised ads', 'Advertisements styled to look like content, navigation or interface elements.'),
    ('Fake scarcity', 'False claims of limited supply to pressure purchase.'),
    ('Fake social proof', 'Fabricated reviews, testimonials or activity notifications.'),
    ('Fake urgency', 'False time pressure, such as countdown timers that reset.'),
    ('Forced action', 'Requiring users to do something unrelated (create account, share data) to get what they want.'),
    ('Hard to cancel', 'Making subscription cancellation deliberately difficult.'),
    ('Hidden costs', 'Revealing extra charges late in the process.'),
    ('Hidden subscription', 'Signing users up for a recurring subscription without making it clear.'),
    ('Nagging', 'Repeatedly interrupting with requests the user has already declined.'),
    ('Obstruction', 'Making a task more difficult than necessary to discourage it.'),
    ('Preselection', 'Pre-selecting options (often paid add-ons or consent) that benefit the business.'),
    ('Sneaking', 'Hiding, disguising or delaying information relevant to the user’s decision.'),
    ('Trick wording', 'Misleading language that causes users to take an action they did not intend.'),
    ('Visual interference', 'Using style and layout to hide or obscure important information or options.'),
], url='https://www.deceptive.design/types')
T('gray2018', 'Gray et al. strategies (2018)', 'Colin M. Gray, Yubo Kou, Bryan Battles, Joseph Hoggatt & Austin Toombs', 2018, 'Gray, C. M., Kou, Y., Battles, B., Hoggatt, J., & Toombs, A. L. (2018). The dark (patterns) side of UX design. CHI \'18, Paper 534.', [
    ('Nagging', 'Redirection of expected functionality that persists beyond one or more interactions.'),
    ('Obstruction', 'Making a process more difficult than it needs to be, with the intent of dissuading certain actions (roach motel, price comparison prevention, intermediate currency).'),
    ('Sneaking', 'Attempting to hide, disguise or delay the divulging of information relevant to the user (forced continuity, hidden costs, sneak into basket, bait and switch).'),
    ('Interface interference', 'Manipulation of the user interface that privileges certain actions over others (hidden information, preselection, aesthetic manipulation, toying with emotion, disguised ads, trick questions).'),
    ('Forced action', 'Requiring the user to perform a certain action to access (or continue to access) certain functionality (social pyramid, privacy Zuckering, gamification).'),
])
T('mathur2019', 'Mathur et al. categories & types (2019)', 'Arunesh Mathur, Gunes Acar, Michael Friedman, Elena Lucherini, Jonathan Mayer, Marshini Chetty & Arvind Narayanan', 2019,
  'Mathur, A. et al. (2019). Dark patterns at scale: Findings from a crawl of 11K shopping websites. Proc. ACM HCI 3(CSCW), Article 81. (1,818 instances, 15 types, 7 categories, found on 11.1% of ~11K sites.)', [
    ('Sneaking > Sneak into basket', 'Adding additional products to users’ shopping carts without their consent.'),
    ('Sneaking > Hidden costs', 'Revealing previously undisclosed charges just before purchase.'),
    ('Sneaking > Hidden subscription', 'Charging a recurring fee under the pretense of a one-time fee or free trial.'),
    ('Urgency > Countdown timers', 'Indicating that a deal will expire soon (timers may be fake or reset).'),
    ('Urgency > Limited-time messages', 'Indicating that a deal will expire soon without specifying a deadline.'),
    ('Misdirection > Confirmshaming', 'Using language and emotion to steer users away from a certain choice.'),
    ('Misdirection > Visual interference', 'Using style and visual presentation to steer users to or away from choices.'),
    ('Misdirection > Trick questions', 'Using confusing language to steer users into making certain choices.'),
    ('Misdirection > Pressured selling', 'Pre-selecting more expensive variations or pressuring the user to accept them.'),
    ('Social proof > Activity messages', 'Informing the user about the activity on the website (purchases, views, visits), which may be fake.'),
    ('Social proof > Testimonials of uncertain origin', 'Testimonials whose origin is unclear.'),
    ('Scarcity > Low-stock messages', 'Indicating to users that limited quantities of a product are available.'),
    ('Scarcity > High-demand messages', 'Indicating to users that a product is in high demand and likely to sell out soon.'),
    ('Obstruction > Hard to cancel', 'Making it easy to sign up but hard to cancel.'),
    ('Forced action > Forced enrollment', 'Coercing users to create accounts or share information to complete tasks.'),
], url='https://webtransparency.cs.princeton.edu/dark-patterns/')
T('mathur2021', 'Mathur, Kshirsagar & Mayer attributes (2021)', 'Arunesh Mathur, Mihir Kshirsagar & Jonathan Mayer', 2021,
  'Mathur, A., Kshirsagar, M., & Mayer, J. (2021). What makes a dark pattern... dark? CHI \'21, Paper 360.', [
    ('Asymmetric', 'Unequal burdens on options available to users (e.g., "accept" prominent, "reject" hidden).'),
    ('Covert', 'The effect of the design is hidden from users.'),
    ('Deceptive', 'Induces false beliefs through affirmative misstatements, misleading statements or omissions.'),
    ('Hides information', 'Obscures or delays the presentation of necessary information.'),
    ('Restrictive', 'Reduces or eliminates the options available to users.'),
    ('Disparate treatment', 'Disadvantages and treats one group of users differently from another.'),
])
T('gray2024', 'Gray et al. ontology high-level patterns (2024)', 'Colin M. Gray, Cristiana Santos, Nataliia Bielova & Thomas Mildner', 2024,
  'Gray, C. M., Santos, C. T., Bielova, N., & Mildner, T. (2024). An ontology of dark patterns knowledge: Foundations, definitions, and a pathway for shared knowledge-building. CHI \'24.', [
    ('Obstruction', 'Impeding a task flow, making an interaction more difficult than inherently needed.'),
    ('Sneaking', 'Hiding, disguising or delaying information relevant to the user’s decision.'),
    ('Interface interference', 'Privileging specific actions over others through the interface, confusing users or limiting discoverability.'),
    ('Forced action', 'Requiring users to perform an additional, tangential action to access functionality.'),
    ('Social engineering', 'Presenting options or information that cause users to be more likely to perform an action due to individual or social cognitive biases.'),
], conf='medium')
T('edpb2022', 'EDPB deceptive design pattern categories in social media (2022/2023)', 'European Data Protection Board', '2022/2023',
  'EDPB (2023). Guidelines 03/2022 on deceptive design patterns in social media platform interfaces: how to recognise and avoid them, v2.0.', [
    ('Overloading', 'Users face a large quantity of requests, information, options or possibilities to push them to share more data (continuous prompting, privacy maze, too many options).'),
    ('Skipping', 'Designing the interface so users forget or do not think about data protection aspects (deceptive snugness, look over there).'),
    ('Stirring', 'Affecting choices by appealing to emotions or visual nudges (emotional steering, hidden in plain sight).'),
    ('Obstructing', 'Hindering or blocking users from getting informed or managing their data (dead end, longer than necessary, misleading action).'),
    ('Fickle', 'Unstable and inconsistent design that makes it hard to navigate privacy controls (lacking hierarchy, decontextualising, inconsistent interface, language discontinuity).'),
    ('Left in the dark', 'Hiding information or privacy controls or leaving users unsure how data is processed (conflicting information, ambiguous wording or information).'),
])
T('ftc2022', 'FTC "Bringing Dark Patterns to Light" categories (2022)', 'U.S. Federal Trade Commission', 2022,
  'FTC Staff Report (2022). Bringing Dark Patterns to Light.', [
    ('Design elements that induce false beliefs', 'False claims, fake countdown timers, fake reviews, disguised ads.'),
    ('Design elements that hide or delay disclosure of material information', 'Drip pricing, hidden fees, burying key terms.'),
    ('Design elements that lead to unauthorized charges', 'Free-to-pay conversions without consent, difficult cancellation (negative option).'),
    ('Design elements that obscure or subvert privacy choices', 'Default data sharing, confusing privacy settings, asymmetric consent choices.'),
])
T('dsa25', 'EU Digital Services Act Article 25 (online interface design)', 'European Union', 2022,
  'Regulation (EU) 2022/2065 (Digital Services Act), Article 25 and Recital 67.', [
    ('Prohibition of deceiving or manipulating interfaces', 'Providers of online platforms shall not design, organise or operate their online interfaces in a way that deceives or manipulates recipients or otherwise materially distorts or impairs their ability to make free and informed decisions.'),
    ('Asymmetric prominence of choices', 'Giving more prominence to certain choices when asking the recipient for a decision (Art. 25(3)(a), guidance area).'),
    ('Repeated requests', 'Repeatedly requesting that the recipient make a choice where that choice has already been made, especially via pop-ups (Art. 25(3)(b)).'),
    ('Harder termination than sign-up', 'Making the procedure for terminating a service more difficult than subscribing to it (Art. 25(3)(c)).'),
])
T('cpra', 'California CPRA / CCPA regulations on dark patterns', 'California Privacy Protection Agency', '2020/2023',
  'Cal. Civ. Code §1798.140(l) (CPRA 2020: consent obtained through dark patterns is not consent); 11 CCR §7004 (2023) requirements for methods for submitting CCPA requests and obtaining consent.', [
    ('Easy to understand', 'Language must be easy to read and understandable; no confusing or misleading wording.'),
    ('Symmetry in choice', 'The path for a more privacy-protective option must not be longer or more difficult than the less protective option (e.g., "Accept all" vs "Decline all").'),
    ('Avoid language or interactive elements that are confusing', 'No double negatives or toggles with unclear states.'),
    ('Avoid choice architecture that impairs or interferes with the ability to make a choice', 'No bundling of consent, no guilt or shame framing, no forced navigation through unrelated screens.'),
    ('Easy to execute', 'The business must not add unnecessary burden or friction to the request process.'),
])
T('india-ccpa-2023', 'India CCPA Guidelines for Prevention and Regulation of Dark Patterns (2023)', 'Central Consumer Protection Authority, India', 2023,
  'Central Consumer Protection Authority (2023). Guidelines for Prevention and Regulation of Dark Patterns, 2023 (notified 30 Nov 2023), Annexure 1.', [
    ('False urgency', 'Falsely stating or implying urgency or scarcity to mislead users into immediate purchase.'),
    ('Basket sneaking', 'Adding items, services or charges at checkout without consent.'),
    ('Confirm shaming', 'Using a phrase, video, audio or other means to create fear, shame, ridicule or guilt to nudge a user.'),
    ('Forced action', 'Forcing a user to take an action requiring them to buy additional goods, subscribe to an unrelated service, or share personal information to buy the intended product.'),
    ('Subscription trap', 'Making cancellation complex, hiding the cancellation option, forcing payment details for a free subscription, or ambiguous instructions.'),
    ('Interface interference', 'Design elements that manipulate the user interface to highlight certain information and obscure other relevant information.'),
    ('Bait and switch', 'Advertising a particular outcome but deceptively serving an alternate outcome.'),
    ('Drip pricing', 'Not revealing elements of prices upfront or revealing them surreptitiously.'),
    ('Disguised advertisement', 'Posing or masking advertisements as other content types such as user-generated content or news.'),
    ('Nagging', 'Overloading users with requests, information, options or interruptions unrelated to the intended purchase.'),
    ('Trick question', 'Deliberately using confusing or vague language to misguide or misdirect a user.'),
    ('SaaS billing', 'Generating and collecting payments on a recurring basis in a software-as-a-service model by exploiting positive acquisition loops in recurring subscriptions as covertly as possible.'),
    ('Rogue malwares', 'Using ransomware or scareware to mislead or trick users into believing there is a virus on their computer, to convince them to pay for a fake malware removal tool.'),
], conf='medium')
T('attention-patterns', 'Attention-capture deceptive patterns', 'Alberto Monge Roffarello, Kai Lukoff & Luigi De Russis', 2023,
  'Monge Roffarello, A., Lukoff, K., & De Russis, L. (2023). Defining and identifying attention capture deceptive designs in digital interfaces. CHI \'23.', [
    ('Infinite scroll', 'Content loads continuously without a natural stopping point.'),
    ('Autoplay', 'The next video or content plays automatically without user action.'),
    ('Pull-to-refresh / variable rewards', 'Slot-machine-like refresh mechanics delivering unpredictable rewards.'),
    ('Guilty pleasure recommendations', 'Recommendations optimized for engagement over user goals.'),
    ('Disguised ads and recommendations', 'Sponsored or recommended content blended into feeds.'),
    ('Time fog', 'Hiding the passage of time (no clocks, no usage indicators).'),
    ('Fake social notifications', 'Notifications that exaggerate social activity to pull users back.'),
], conf='medium')
write('curated_dark_patterns', R)
