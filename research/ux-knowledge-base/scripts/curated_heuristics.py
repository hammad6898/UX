from common import *
R = []; SETS = []
def HS(sid, name, author, year, cite, domain, items, conf='high', cat='Heuristics', layer='screen / flow', url='', note=''):
    SETS.append({'set_id': sid, 'name': name, 'author': author, 'year': str(year), 'items': len(items), 'domain': domain,
                 'citation': cite, 'url': url, 'confidence': conf, 'note': note})
    for i, it in enumerate(items, 1):
        title, desc = it[0], it[1]
        check = it[2] if len(it) > 2 and it[2] else ''
        c = it[3] if len(it) > 3 else categorize(title, desc, default=cat)
        R.append(C(f'{sid}.{i:02d}', f'{name} #{i}: {title}', author, year, desc, '', check, layer, '', cite, c, name,
                   applies=domain, conf=conf, url=url, source_set='Curated: heuristic sets'))

HS('nielsen10', "Nielsen's 10 usability heuristics", 'Jakob Nielsen', '1994 (wording updated 2020)',
   'Nielsen, J. (1994). Enhancing the explanatory power of usability heuristics. CHI \'94, 152–158; Nielsen, J. (1994). Heuristic evaluation. In Nielsen & Mack (Eds.), Usability Inspection Methods. Wiley.',
   'all interactive systems', [
    ('Visibility of system status', 'Keep users informed about what is going on through appropriate feedback within a reasonable time, so they can understand the current state and decide what to do next.', 'Does the interface always show where the user is, what is happening (loading, saving, processing), and the result of each action within ~1 s?', 'Feedback & system status'),
    ('Match between system and the real world', 'Use words, phrases and concepts familiar to the user rather than internal jargon, and follow real-world conventions so information appears in a natural, logical order.', 'Is the language the users’ language (no internal jargon, codes or system terms)? Does information follow a natural order?', 'Content & microcopy'),
    ('User control and freedom', 'Users often act by mistake and need a clearly marked way out (cancel, back, undo, redo) without going through an extended process.', 'Can users undo, cancel, go back and exit any flow easily? Are there dead ends or traps?', 'Errors & recovery'),
    ('Consistency and standards', 'Users should not have to wonder whether different words, situations or actions mean the same thing; follow internal consistency and external platform and industry conventions.', 'Are terms, icons, layouts and behaviors consistent within the product and with platform conventions?', 'Visual design & layout'),
    ('Error prevention', 'Better than good error messages is a design that prevents problems in the first place: remove error-prone conditions (slips) or check for them and ask for confirmation before committing (mistakes).', 'Does the design prevent common errors (constraints, good defaults, confirmations for destructive actions, forgiving formats)?', 'Errors & recovery'),
    ('Recognition rather than recall', 'Minimize memory load by making elements, actions and options visible; users should not have to remember information from one part of the interface to another; help should be visible or easily retrievable.', 'Are options, prior answers and needed information visible when needed rather than requiring users to remember them?', 'General UX'),
    ('Flexibility and efficiency of use', 'Shortcuts and accelerators, hidden from novices, can speed up interaction for experts; allow users to tailor frequent actions.', 'Are there accelerators (keyboard shortcuts, bulk actions, saved preferences, recent items) for frequent tasks?', 'General UX'),
    ('Aesthetic and minimalist design', 'Interfaces should not contain irrelevant or rarely needed information; every extra unit of information competes with the relevant units and reduces their visibility.', 'Is every element on the screen necessary? Is the visual hierarchy focused on the primary task?', 'Visual design & layout'),
    ('Help users recognize, diagnose, and recover from errors', 'Error messages should be in plain language (no codes), precisely indicate the problem, and constructively suggest a solution; use traditional error visuals.', 'Do error messages say what went wrong in plain language, where, and how to fix it? Is user input preserved?', 'Errors & recovery'),
    ('Help and documentation', 'Ideally the system needs no explanation, but help may be necessary; it should be easy to search, focused on the user’s task, list concrete steps, and be available in context.', 'Is task-focused, searchable help available in context where users are likely to need it?', 'Onboarding & first use'),
   ], url='https://www.nngroup.com/articles/ten-usability-heuristics/')
HS('nielsen-molich-1990', 'Nielsen & Molich original heuristics (1990)', 'Jakob Nielsen & Rolf Molich', 1990,
   'Molich, R. & Nielsen, J. (1990). Improving a human-computer dialogue. CACM, 33(3), 338–348; Nielsen, J. & Molich, R. (1990). Heuristic evaluation of user interfaces. CHI \'90, 249–256.',
   'all interactive systems', [
    ('Simple and natural dialogue', 'Dialogues should contain only needed information, in a natural and logical order.'),
    ('Speak the users’ language', 'Use words and concepts familiar to the user, not system-oriented terms.'),
    ('Minimize user memory load', 'Users should not have to remember information between parts of the dialogue; instructions should be visible or easily retrievable.'),
    ('Consistency', 'Users should not have to wonder whether different words, situations or actions mean the same thing.'),
    ('Feedback', 'The system should always keep users informed about what is going on, within reasonable time.'),
    ('Clearly marked exits', 'Users often choose functions by mistake and need a clearly marked emergency exit.'),
    ('Shortcuts', 'Accelerators unseen by novices may speed up interaction for experts.'),
    ('Good error messages', 'Messages should be in plain language, precisely indicate the problem and constructively suggest a solution.'),
    ('Prevent errors', 'Careful design that prevents a problem from occurring is better than a good error message.'),
   ], note='The 10th, "Help and documentation", was added in 1991; the set was refined into the 10 heuristics in 1994.')
HS('shneiderman8', "Shneiderman's Eight Golden Rules of Interface Design", 'Ben Shneiderman', '1986 (rev. 2016)',
   'Shneiderman, B. (1986). Designing the User Interface. Addison-Wesley; Shneiderman, B., Plaisant, C., Cohen, M., Jacobs, S., Elmqvist, N., & Diakopoulos, N. (2016). Designing the User Interface, 6th ed. Pearson.',
   'all interactive systems', [
    ('Strive for consistency', 'Use consistent sequences of actions in similar situations, identical terminology in prompts, menus and help, and consistent color, layout, capitalization and fonts; exceptions should be comprehensible and few.', 'Are action sequences, terminology and visual styles consistent across the product?'),
    ('Seek universal usability', 'Recognize the needs of diverse users (novice to expert, age, disability, international, technology diversity); add explanations for novices and shortcuts for experts.', 'Does the design serve novices and experts, and users with disabilities and different devices?'),
    ('Offer informative feedback', 'For every user action there should be feedback; modest for frequent and minor actions, substantial for infrequent and major ones. Visual presentation of objects of interest makes changes explicit.', 'Is feedback proportional to the importance of each action?'),
    ('Design dialogs to yield closure', 'Organize sequences of actions into groups with a beginning, middle and end; informative feedback at completion gives satisfaction and signals readiness for the next action.', 'Do multi-step tasks clearly signal completion (confirmation page/message)?'),
    ('Prevent errors', 'Design so users cannot make serious errors (e.g., gray out inappropriate menu items, do not allow alphabetic characters in numeric fields); if an error occurs, offer simple, constructive, specific recovery instructions, and leave the state unchanged or give instructions about restoring it.', 'Are invalid inputs prevented and are errors recoverable without losing work?'),
    ('Permit easy reversal of actions', 'As much as possible, actions should be reversible; this relieves anxiety and encourages exploration.', 'Can actions be undone at the appropriate granularity (single action, data entry, group of actions)?'),
    ('Keep users in control', 'Experienced users want to feel in charge: avoid surprises, tedious data entry, difficulty obtaining information and inability to produce the desired result.', 'Do users feel in control (no unexpected changes, auto-advancing, or system-initiated actions)?'),
    ('Reduce short-term memory load', 'Humans’ limited capacity for information processing in short-term memory requires designers to avoid interfaces in which users must remember information from one display and use it on another.', 'Is all information needed for a step visible on that step?'),
   ], url='https://www.cs.umd.edu/users/ben/goldenrules.html', note='Rule 2 was "Enable frequent users to use shortcuts" and rule 7 "Support internal locus of control" in earlier editions.')
HS('tognazzini', "Tognazzini's First Principles of Interaction Design (revised 2014)", 'Bruce Tognazzini', '2003/2014',
   'Tognazzini, B. (2014). First Principles of Interaction Design (Revised & Expanded). AskTog.', 'all interactive systems', [
    ('Aesthetics', 'Visual design matters, but aesthetics must not be bought at the cost of usability (e.g., low-contrast trendy text).'),
    ('Anticipation', 'Anticipate users’ needs and bring all information and tools needed for each step to the user, rather than making them hunt for it.'),
    ('Autonomy', 'Give users control within appropriate boundaries; keep them informed of status so they can make decisions.'),
    ('Color', 'Do not rely on color alone to convey information, since many users have color vision deficiencies; use secondary cues.'),
    ('Consistency', 'Maintain consistency with user expectations; inconsistency should be used only to signal genuinely different behavior.'),
    ('Defaults', 'Defaults should be smart, easy to replace (select-on-focus), and never used where users must make a conscious choice.'),
    ('Discoverability', 'Features and controls must be visible or discoverable; hidden functionality might as well not exist.'),
    ('Efficiency of the user', 'Optimize for the user’s productivity, not the computer’s; keep users occupied, minimize waits, and write clear help.'),
    ('Explorable interfaces', 'Provide clear paths and "ways back"; make actions reversible so users can explore safely.'),
    ("Fitts's law", 'Make targets large and close; use screen edges where possible.'),
    ('Human interface objects', 'Interface objects should be understandable, consistent and stable, behaving like real-world objects where helpful.'),
    ('Latency reduction', 'Reduce latency and acknowledge input immediately; show progress for long operations; make waits less painful.'),
    ('Learnability', 'Limit the learning required; support both novices and experienced users; ease of learning and ease of use are not opposites.'),
    ('Metaphors', 'Choose metaphors that enable users to grasp the conceptual model instantly, but do not let them constrain functionality.'),
    ('Protect users’ work', 'Ensure users never lose their work due to errors, crashes, network issues or other causes (autosave).'),
    ('Readability', 'Text should be high-contrast and in sufficiently large fonts; especially consider older users.'),
    ('Simplicity', 'Simplicity is about efficiency and understanding, not merely reducing the number of features.'),
    ('State', 'Track state so users can leave and return to where they left off, across sessions and devices.'),
    ('Visible navigation', 'Avoid invisible navigation; reduce navigation overall and make the user’s location clear.'),
   ], conf='medium', url='https://asktog.com/atc/principles-of-interaction-design/', note='List compiled from the 2014 revision; verify exact naming against the AskTog article.')
HS('gerhardt-powals', "Gerhardt-Powals' cognitive engineering principles", 'Jill Gerhardt-Powals', 1996,
   'Gerhardt-Powals, J. (1996). Cognitive engineering principles for enhancing human-computer performance. IJHCI, 8(2), 189–211.', 'information-heavy / decision-support systems', [
    ('Automate unwanted workload', 'Free cognitive resources for high-level tasks; eliminate mental calculations, estimations, comparisons and unnecessary thinking.', 'Does the system calculate, compare and summarize for the user instead of asking them to do it mentally?'),
    ('Reduce uncertainty', 'Display data in a manner that is clear and obvious.'),
    ('Fuse data', 'Reduce cognitive load by bringing together lower-level data into a higher-level summary.'),
    ('Present new information with meaningful aids to interpretation', 'Use a familiar framework, making it easier to absorb; use everyday terms, metaphors, etc.'),
    ('Use names that are conceptually related to function', 'Display names and labels should be context-dependent and improve recall and recognition.'),
    ('Group data in consistently meaningful ways', 'Logically group information within a screen and across screens to decrease search time.'),
    ('Limit data-driven tasks', 'Reduce the time spent assimilating raw data; make appropriate use of color and graphics.'),
    ('Include in the displays only that information needed by the user at a given time', 'Allow users to remain focused on critical data; exclude extraneous information.'),
    ('Provide multiple coding of data when appropriate', 'Present data in varying formats and/or levels of detail to promote cognitive flexibility.'),
    ('Practice judicious redundancy', 'Be redundant where it helps resolve possible conflicts, but avoid gratuitous repetition.'),
   ])
HS('bastien-scapin', 'Bastien & Scapin ergonomic criteria', 'J. M. Christian Bastien & Dominique L. Scapin', 1993,
   'Bastien, J. M. C. & Scapin, D. L. (1993). Ergonomic Criteria for the Evaluation of Human-Computer Interfaces. INRIA Technical Report No. 156.', 'all interactive systems', [
    ('Guidance > Prompting', 'Means available to advise, orient, inform and guide users in their interactions (labels, prompts, formats, help).'),
    ('Guidance > Grouping/distinction of items by location', 'Relative positioning of items indicates whether they belong to the same class.'),
    ('Guidance > Grouping/distinction of items by format', 'Graphical features (format, color) indicate whether items belong to the same class.'),
    ('Guidance > Immediate feedback', 'System responses to user actions are immediate, quick and appropriate.'),
    ('Guidance > Legibility', 'Lexical characteristics of information on screen (brightness, contrast, font size, spacing, line length) support reading.'),
    ('Workload > Brevity > Conciseness', 'Reduce perceptual and cognitive load for individual inputs and outputs (short codes, default values).'),
    ('Workload > Brevity > Minimal actions', 'Limit the number of steps users must go through to accomplish a task.'),
    ('Workload > Information density', 'Workload from a perceptual and cognitive point of view relative to the whole set of displayed information should be minimal.'),
    ('Explicit control > Explicit user action', 'The system processes only actions explicitly requested by users, when requested.'),
    ('Explicit control > User control', 'Users should always be in control of system processing (interrupt, cancel, pause, continue).'),
    ('Adaptability > Flexibility', 'Means available to users to customize the interface to their working strategies, habits and task requirements.'),
    ('Adaptability > User’s experience level', 'Means available to take into account the level of user experience (shortcuts for experts, guidance for novices).'),
    ('Error management > Error protection', 'Means available to detect and prevent data entry errors, command errors or actions with destructive consequences.'),
    ('Error management > Quality of error messages', 'Phrasing and content of error messages: relevance, readability, specificity about the nature of errors and the actions needed to correct them.'),
    ('Error management > Error correction', 'Means available for users to correct their errors.'),
    ('Consistency', 'Interface design choices (codes, naming, formats, procedures) are maintained in similar contexts and differ for different contexts.'),
    ('Significance of codes and denominations', 'Adequacy between the object or information displayed or entered and its reference; codes and names are meaningful to users.'),
    ('Compatibility', 'Match between user characteristics (memory, perception, habits, skills, age, expectations) and task characteristics on one hand, and the organization of output, input and dialogue on the other.'),
   ])
HS('iso9241-110-2020', 'ISO 9241-110:2020 Interaction principles', 'ISO TC 159/SC 4', 2020,
   'ISO 9241-110:2020. Ergonomics of human-system interaction — Part 110: Interaction principles.', 'all interactive systems', [
    ('Suitability for the user’s tasks', 'The interactive system supports users in completing their tasks, presenting what is needed and avoiding unnecessary steps.'),
    ('Self-descriptiveness', 'The interactive system presents appropriate information so that its capabilities and use are immediately obvious, without needing to consult help or other external resources.'),
    ('Conformity with user expectations', 'The interactive system behaves predictably based on context and commonly accepted conventions.'),
    ('Learnability', 'The interactive system supports discovery of its capabilities and how to use them, allows exploration, minimizes the need for learning and provides support when learning is needed.'),
    ('Controllability', 'Users can maintain control over the user interface and their interactions, including direction and pace.'),
    ('Use error robustness', 'The system helps users avoid errors, and when errors occur, makes them recognizable and supports recovery.'),
    ('User engagement', 'The system presents functions and information in an inviting and motivating manner that supports continued interaction.'),
   ], note='Replaces the 2006 dialogue principles (suitability for the task, self-descriptiveness, controllability, conformity with user expectations, error tolerance, suitability for individualization, suitability for learning).')
HS('iso9241-112', 'ISO 9241-112:2017 Principles for the presentation of information', 'ISO TC 159/SC 4', 2017,
   'ISO 9241-112:2017. Ergonomics of human-system interaction — Part 112: Principles for the presentation of information.', 'all interactive systems', [
    ('Detectability', 'Information is presented so that it will be recognized as present.'),
    ('Freedom from distraction', 'Required information is perceived without other information interfering.'),
    ('Discriminability', 'Items of information can be distinguished accurately from each other.'),
    ('Interpretability', 'Information is understood as intended.'),
    ('Conciseness', 'Only the information needed for the task is presented.'),
    ('Internal and external consistency', 'Information with similar intent is presented similarly within the system and consistent with users’ expectations from other systems.'),
   ])
HS('iso9241-210', 'ISO 9241-210 Human-centred design principles', 'ISO TC 159/SC 4', '2010 (rev. 2019)',
   'ISO 9241-210:2019. Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems.', 'design process', [
    ('Based on explicit understanding of users, tasks and environments', 'Design is based upon an explicit understanding of users, tasks and environments.'),
    ('Users are involved throughout design and development', 'Users take part in design and development, not only at the end.'),
    ('Driven and refined by user-centred evaluation', 'Design is driven and refined by evaluation with users.'),
    ('The process is iterative', 'Design iterates between understanding, design and evaluation.'),
    ('Addresses the whole user experience', 'The design addresses the whole user experience, not just the screen.'),
    ('Multidisciplinary skills and perspectives', 'The design team includes multidisciplinary skills and perspectives.'),
   ], layer='organizational / research')
HS('weinschenk-barker', 'Weinschenk & Barker classification (20 heuristics)', 'Susan Weinschenk & Dean Barker', 2000,
   'Weinschenk, S. & Barker, D. T. (2000). Designing Effective Speech Interfaces. Wiley.', 'all interactive systems incl. speech', [
    ('User control', 'Heuristics checking whether the user has enough control of the interface.'),
    ('Human limitations', 'The design takes into account human limitations (cognitive, perceptual, motor) to avoid overload.'),
    ('Modal integrity', 'The interface uses the tasks appropriate to each modality (auditory, visual, motor/kinesthetic).'),
    ('Accommodation', 'The design is appropriate to fit the needs of each user group.'),
    ('Linguistic clarity', 'The language used communicates as efficiently as possible.'),
    ('Aesthetic integrity', 'The design is visually attractive and tailored to appeal to the target population.'),
    ('Simplicity', 'The design does not use unnecessary complexity.'),
    ('Predictability', 'Users can form a clear mental model of the system and predict its behavior.'),
    ('Interpretation', 'The system makes reasonable guesses about what the user is trying to do.'),
    ('Accuracy', 'The interface is free from errors.'),
    ('Technical clarity', 'The interface has the highest possible fidelity.'),
    ('Flexibility', 'The design allows users to adjust it for more effective use.'),
    ('Fulfillment', 'The user experience is adequate and satisfying.'),
    ('Cultural propriety', 'The user’s cultural and social expectations are met.'),
    ('Suitable tempo', 'The pace at which users work with the system is adequate.'),
    ('Consistency', 'The system is consistent.'),
    ('User support', 'The design supports learning and provides the required assistance.'),
    ('Precision', 'The system allows users to perform tasks accurately.'),
    ('Forgiveness', 'The user can make mistakes and recover to a workable state.'),
    ('Responsiveness', 'The interface provides enough feedback about status and task completion.'),
   ], conf='medium', note='Synthesis of guidelines from several major providers; descriptions summarized.')
HS('mandel', "Mandel's golden rules", 'Theo Mandel', 1997,
   'Mandel, T. (1997). The Elements of User Interface Design. Wiley.', 'all interactive systems', [
    ('Place users in control', 'Use modes judiciously; allow flexible keyboard and mouse use; allow interruptible and undoable actions; hide technical internals; design for direct interaction.'),
    ('Reduce users’ memory load', 'Relieve short-term memory (undo, copy/paste); rely on recognition; provide visual cues; provide defaults, undo and redo; provide shortcuts; promote object-action syntax; use real-world metaphors; use progressive disclosure.'),
    ('Make the interface consistent', 'Sustain the context of users’ tasks; maintain consistency within and across products; keep interaction results the same; provide aesthetic appeal and integrity; encourage exploration.'),
   ])
HS('hansen1971', "Hansen's user engineering principles", 'Wilfred J. Hansen', 1971,
   'Hansen, W. J. (1971). User engineering principles for interactive systems. AFIPS Fall Joint Computer Conference, 39, 523–532.', 'interactive systems (first published list of UI design principles)', [
    ('Know the user', 'Understand who the users are and design for them.'),
    ('Minimize memorization', 'Select rather than enter; use names, not numbers; ensure predictable behavior; provide ready access to system information.'),
    ('Optimize operations', 'Provide rapid execution of common operations; display inertia (change only what needs changing); muscle memory; reorganize command parameters for common use.'),
    ('Engineer for errors', 'Provide good error messages; engineer out common errors; allow reversible actions; provide redundancy; ensure data structure integrity.'),
   ])
HS('rams10', "Dieter Rams' ten principles for good design", 'Dieter Rams', 'late 1970s–1980s',
   'Rams, D. (c. 1976–1985). Ten principles for good design; see Vitsœ, "Good Design".', 'product & visual design', [
    ('Good design is innovative', 'Innovation develops alongside technology and is never an end in itself.'),
    ('Good design makes a product useful', 'It emphasizes usefulness and disregards anything that could detract from it.'),
    ('Good design is aesthetic', 'Aesthetic quality is integral to usefulness because products affect people’s well-being.'),
    ('Good design makes a product understandable', 'It clarifies the product’s structure; at best, the product is self-explanatory.'),
    ('Good design is unobtrusive', 'Products are tools, neutral and restrained, leaving room for the user’s self-expression.'),
    ('Good design is honest', 'It does not make a product appear more innovative, powerful or valuable than it is, and does not manipulate.'),
    ('Good design is long-lasting', 'It avoids being fashionable and therefore never appears antiquated.'),
    ('Good design is thorough down to the last detail', 'Nothing is arbitrary or left to chance; care shows respect for the user.'),
    ('Good design is environmentally friendly', 'It conserves resources and minimizes pollution throughout the product lifecycle.'),
    ('Good design is as little design as possible', 'Less, but better: concentrate on essential aspects.'),
   ], layer='screen')
HS('universal-design', 'Principles of Universal Design', 'B. R. Connell, M. Jones, R. Mace, J. Mueller, A. Mullick, E. Ostroff, J. Sanford, E. Steinfeld, M. Story & G. Vanderheiden (NC State Center for Universal Design)', 1997,
   'Center for Universal Design (1997). The Principles of Universal Design, Version 2.0. North Carolina State University.', 'products & environments, incl. digital', [
    ('Equitable use', 'The design is useful and marketable to people with diverse abilities; provide the same means of use for all users where possible.'),
    ('Flexibility in use', 'The design accommodates a wide range of individual preferences and abilities (choice in methods, left/right-handed use, pace).'),
    ('Simple and intuitive use', 'Use of the design is easy to understand regardless of experience, knowledge, language skills or concentration level.'),
    ('Perceptible information', 'The design communicates necessary information effectively regardless of ambient conditions or sensory abilities (redundant modes).'),
    ('Tolerance for error', 'The design minimizes hazards and adverse consequences of accidental or unintended actions (warnings, fail-safes).'),
    ('Low physical effort', 'The design can be used efficiently and comfortably with minimum fatigue (minimize repetitive actions and sustained effort).'),
    ('Size and space for approach and use', 'Appropriate size and space is provided for approach, reach, manipulation and use regardless of body size, posture or mobility.'),
   ], cat='Accessibility')
HS('inclusive-design-principles', 'Inclusive Design Principles', 'Henny Swan, Ian Pouncey, Heydon Pickering & Léonie Watson', 2016,
   'Swan, H., Pouncey, I., Pickering, H., & Watson, L. (2016). Inclusive Design Principles. inclusivedesignprinciples.info.', 'web & apps', [
    ('Provide comparable experience', 'Ensure the interface provides a comparable experience for all so people can accomplish tasks in a way that suits their needs without undermining content quality.'),
    ('Consider situation', 'People use interfaces in different situations (noise, light, attention, device); make sure the interface delivers a valuable experience regardless of circumstances.'),
    ('Be consistent', 'Use familiar conventions and apply them consistently.'),
    ('Give control', 'Ensure people are in control: they can access and interact with content in their preferred way (e.g., no forced scroll, no autoplay without control).'),
    ('Offer choice', 'Consider providing different ways for people to complete tasks, especially complex or non-standard ones.'),
    ('Prioritise content', 'Help users focus on core tasks, features and information by prioritising them within content and layout.'),
    ('Add value', 'Consider the value of features and how they improve the experience for different users (e.g., device capabilities like voice, geolocation).'),
   ], cat='Accessibility')
HS('ms-inclusive', 'Microsoft Inclusive Design principles', 'Microsoft (Kat Holmes et al.)', 2016,
   'Microsoft (2016). Inclusive Design Toolkit; Holmes, K. (2018). Mismatch: How Inclusion Shapes Design. MIT Press.', 'products & services', [
    ('Recognize exclusion', 'Exclusion happens when we solve problems using our own biases; identify who is excluded by mismatches between people and designs.'),
    ('Learn from diversity', 'People who adapt to exclusion are experts; design with them from the start.'),
    ('Solve for one, extend to many', 'Designing for people with permanent disabilities benefits people with temporary and situational limitations too (the persona spectrum).'),
   ], cat='Accessibility')
HS('govuk-design-principles', 'GOV.UK Government Design Principles', 'Government Digital Service (UK)', '2012 (11th added 2025)',
   'Government Digital Service (2012, updated 2025). Government Design Principles. gov.uk/guidance/government-design-principles.', 'public services', [
    ('Start with user needs', 'Service design starts with identifying user needs, found through research, not assumptions.'),
    ('Do less', 'Government should only do what only government can do; reuse and share rather than reinvent.'),
    ('Design with data', 'Learn from real-world behavior and data, and build analytics into services.'),
    ('Do the hard work to make it simple', 'Making something look simple is hard, and it is worth it; do not accept complexity as inevitable.'),
    ('Iterate. Then iterate again', 'Start small and iterate wildly; release minimum viable products early and test with real users.'),
    ('This is for everyone', 'Accessible, inclusive design is good design; build for needs, not audiences.'),
    ('Understand context', 'Design for people, not screens: consider where, how and with what devices users access services.'),
    ('Build digital services, not websites', 'A service is something that helps people do something; design the whole service, online and offline.'),
    ('Be consistent, not uniform', 'Use the same language and design patterns wherever possible, while allowing improvement.'),
    ('Make things open: it makes things better', 'Share code, designs, ideas and failures.'),
    ('Minimise environmental impact', 'Building and running digital services uses energy, water and materials; design and build services to reduce their environmental footprint.'),
   ], url='https://www.gov.uk/guidance/government-design-principles', layer='organizational / research', note='License: Open Government Licence v3.0; summarized here.')
HS('govuk-service-standard', 'GOV.UK Service Standard (14 points)', 'Government Digital Service (UK)', 2019,
   'Government Digital Service (2019). The Service Standard. gov.uk/service-manual/service-standard.', 'public services', [
    ('Understand users and their needs', 'Develop a deep understanding of users and the problem you are trying to solve.'),
    ('Solve a whole problem for users', 'Work towards creating a service that solves one whole problem for users, collaborating across organizational boundaries.'),
    ('Provide a joined up experience across all channels', 'Work towards a seamless experience across online, phone, paper and face-to-face channels.'),
    ('Make the service simple to use', 'Build a service that is simple, intuitive and comprehensible, and test it with users.'),
    ('Make sure everyone can use the service', 'Provide a service that everyone can use, including disabled people and people with low digital skills.'),
    ('Have a multidisciplinary team', 'Put in place a sustainable multidisciplinary team that can design, build and operate the service.'),
    ('Use agile ways of working', 'Create the service using agile, iterative and user-centred methods.'),
    ('Iterate and improve frequently', 'Have the capacity, resources and technical flexibility to iterate and improve the service frequently.'),
    ('Create a secure service which protects users’ privacy', 'Evaluate what user data and information the service will be providing or storing and address security risks.'),
    ('Define what success looks like and publish performance data', 'Work out what success looks like and identify metrics that show whether the service is solving the problem.'),
    ('Choose the right tools and technology', 'Choose tools and technology that let you create a high quality service in a cost effective way.'),
    ('Make new source code open', 'Make all new source code open and reusable, and publish it under appropriate licences.'),
    ('Use and contribute to open standards, common components and patterns', 'Build on open standards and common components and patterns from inside and outside government.'),
    ('Operate a reliable service', 'Minimise service downtime and have a plan to deal with it when it does happen.'),
   ], url='https://www.gov.uk/service-manual/service-standard', layer='organizational / research')
HS('hax18', 'Guidelines for Human-AI Interaction (Microsoft HAX)', 'Saleema Amershi et al. (Microsoft)', 2019,
   'Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P. N., Inkpen, K., Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). Guidelines for Human-AI Interaction. CHI \'19, Paper 3.',
   'AI-powered products', [
    ('Make clear what the system can do (initially)', 'Help the user understand what the AI system is capable of doing.', 'Does the product explain what the AI can and cannot do before or at first use?'),
    ('Make clear how well the system can do what it can do (initially)', 'Help the user understand how often the AI system may make mistakes.', 'Are accuracy limits and likelihood of errors communicated?'),
    ('Time services based on context (during interaction)', 'Time when to act or interrupt based on the user’s current task and environment.'),
    ('Show contextually relevant information (during interaction)', 'Display information relevant to the user’s current task and environment.'),
    ('Match relevant social norms (during interaction)', 'Ensure the experience is delivered in a way users would expect, given their social and cultural context.'),
    ('Mitigate social biases (during interaction)', 'Ensure the AI system’s language and behaviors do not reinforce undesirable and unfair stereotypes and biases.'),
    ('Support efficient invocation (when wrong)', 'Make it easy to invoke or request the AI system’s services when needed.'),
    ('Support efficient dismissal (when wrong)', 'Make it easy to dismiss or ignore undesired AI system services.'),
    ('Support efficient correction (when wrong)', 'Make it easy to edit, refine or recover when the AI system is wrong.'),
    ('Scope services when in doubt (when wrong)', 'Engage in disambiguation or gracefully degrade the AI system’s services when uncertain about a user’s goals.'),
    ('Make clear why the system did what it did (when wrong)', 'Enable the user to access an explanation of why the AI system behaved as it did.'),
    ('Remember recent interactions (over time)', 'Maintain short-term memory and allow the user to make efficient references to that memory.'),
    ('Learn from user behavior (over time)', 'Personalize the user’s experience by learning from their actions over time.'),
    ('Update and adapt cautiously (over time)', 'Limit disruptive changes when updating and adapting the AI system’s behaviors.'),
    ('Encourage granular feedback (over time)', 'Enable the user to provide feedback indicating their preferences during regular interaction.'),
    ('Convey the consequences of user actions (over time)', 'Immediately update or convey how user actions will impact future behaviors of the AI system.'),
    ('Provide global controls (over time)', 'Allow the user to globally customize what the AI system monitors and how it behaves.'),
    ('Notify users about changes (over time)', 'Inform the user when the AI system adds or updates its capabilities.'),
   ], cat='AI & automation', url='https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/')
HS('pair', 'Google People + AI Guidebook (PAIR) chapters', 'Google PAIR', '2019 (updated 2021)',
   'Google PAIR (2019/2021). People + AI Guidebook. pair.withgoogle.com/guidebook.', 'AI-powered products', [
    ('User needs + defining success', 'Find where AI genuinely adds value for user needs; decide whether to automate or augment; define success and the reward function, weighing precision vs recall.'),
    ('Data collection + evaluation', 'Translate user needs into data needs; source data responsibly; evaluate for fairness and representativeness.'),
    ('Mental models', 'Set expectations for adaptation; onboard in stages; plan for co-learning; account for user expectations of human-like interaction.'),
    ('Explainability + trust', 'Help users calibrate trust; explain at the right level; show confidence where useful; tie explanations to user actions.'),
    ('Feedback + control', 'Align feedback with model improvement; communicate value and timing of feedback; balance control and automation.'),
    ('Errors + graceful failure', 'Define errors and failure from the user’s perspective; identify error sources; provide paths forward from failure.'),
   ], cat='AI & automation', url='https://pair.withgoogle.com/guidebook/')
HS('apple-hig-classic', 'Apple Human Interface principles (classic and modern)', 'Apple', '1987–2025',
   'Apple Computer (1987). Human Interface Guidelines: The Apple Desktop Interface; Apple (2013–2025). Human Interface Guidelines (iOS, macOS, visionOS).', 'Apple platforms', [
    ('Aesthetic integrity', 'Appearance and behavior integrate with function; a productivity app keeps decoration subtle.'),
    ('Consistency', 'Use system-provided interface elements, icons, standard text styles and uniform terminology so the app behaves as people expect.'),
    ('Direct manipulation', 'People act directly on onscreen content and see immediate, visible results.'),
    ('Feedback', 'Acknowledge actions and show results to keep people informed.'),
    ('Metaphors', 'Virtual objects and actions modeled on familiar experiences help people learn faster.'),
    ('User control', 'People, not apps, are in control; the app suggests and warns but does not take over decisions.'),
    ('Clarity (iOS 7 era)', 'Text is legible at every size, icons are precise and lucid, adornments are subtle, and focus on functionality drives design.'),
    ('Deference (iOS 7 era)', 'Fluid motion and a crisp interface help people understand and interact with content while never competing with it.'),
    ('Depth (iOS 7 era)', 'Distinct visual layers and realistic motion convey hierarchy and facilitate understanding.'),
    ('Hierarchy, harmony, consistency (2025)', 'Controls and interface elements establish clear visual hierarchy and elevate content; designs align with the concentric geometry of hardware and software; designs adopt platform conventions to stay consistent across window sizes and displays.'),
   ], conf='medium', note='Apple HIG text is copyrighted; summarized. 2025 principles introduced with the Liquid Glass design language.')
HS('material', 'Material Design principles', 'Google', '2014/2021/2025',
   'Google (2014). Material Design; Google (2021). Material You (Material 3); Google (2025). Material 3 Expressive.', 'Android, web', [
    ('Material is the metaphor (M1, 2014)', 'A tactile, paper-and-ink-inspired surface model with realistic lighting and elevation grounds the interface in physical reality.'),
    ('Bold, graphic, intentional (M1, 2014)', 'Print-design foundations (typography, grids, space, scale, color, imagery) create hierarchy, meaning and focus.'),
    ('Motion provides meaning (M1, 2014)', 'Motion respects and reinforces the user as prime mover, is meaningful and appropriate, and focuses attention.'),
    ('Personal, adaptive, expressive (M3, 2021)', 'Material You emphasizes personalization (dynamic color from the user’s wallpaper), adaptivity across devices and accessibility.'),
   ], conf='medium')
HS('cognitive-walkthrough', 'Cognitive walkthrough questions', 'C. Wharton, J. Rieman, C. Lewis & P. Polson', '1990/1994',
   'Lewis, C., Polson, P., Wharton, C., & Rieman, J. (1990). Testing a walkthrough methodology for theory-based design of walk-up-and-use interfaces. CHI \'90; Wharton, C., Rieman, J., Lewis, C., & Polson, P. (1994). The cognitive walkthrough method: A practitioner\'s guide. In Nielsen & Mack (Eds.), Usability Inspection Methods.',
   'learnability / walk-up-and-use', [
    ('Will the user try to achieve the right effect?', 'Does the user understand that this step is needed to reach their goal?', 'At each step: will the user know they need to do this?'),
    ('Will the user notice that the correct action is available?', 'Is the control visible and recognizable?', 'At each step: is the needed control visible?'),
    ('Will the user associate the correct action with the effect they are trying to achieve?', 'Does the label or icon clearly connect to the user’s intention?', 'At each step: does the label match the user’s goal?'),
    ('If the correct action is performed, will the user see that progress is being made?', 'Does the feedback confirm progress toward the goal?', 'At each step: is there feedback confirming progress?'),
   ], layer='flow')
HS('streamlined-cw', 'Streamlined cognitive walkthrough', 'Rick Spencer', 2000,
   'Spencer, R. (2000). The streamlined cognitive walkthrough method. CHI \'00, 353–359.', 'learnability', [
    ('Will the user know what to do at this step?', 'Combines the first three classic questions.'),
    ('If the user does the right thing, will they know that they did the right thing and are making progress?', 'Feedback question.'),
   ], layer='flow')
HS('bertini-mobile', 'Mobile usability heuristics (Bertini et al.)', 'E. Bertini, S. Gabrielli & S. Kimani', 2006,
   'Bertini, E., Gabrielli, S., & Kimani, S. (2006). Appropriating and assessing heuristics for mobile computing. AVI \'06, 119–126.', 'mobile', [
    ('Visibility of system status and losability/findability of the device', 'Keep users informed of system status and help them find the device and its state.'),
    ('Match between system and the real world', 'Enable the mobile user to interpret information correctly in context of use.'),
    ('Consistency and mapping', 'Users’ conceptual model of possible function/interaction with the device should be consistent with context.'),
    ('Good ergonomics and minimalist design', 'Devices should be easy and comfortable to hold, carry and use; screen real estate is limited so include only necessary information.'),
    ('Ease of input, screen readability and glanceability', 'Provide easy ways to input data, and content that is readable and navigable at a glance.'),
    ('Flexibility, efficiency of use and personalization', 'Allow users to tailor and personalize, and provide accelerators.'),
    ('Aesthetic, privacy and social conventions', 'Take aesthetic and emotional aspects into account; protect private data; respect social conventions of use in public.'),
    ('Realistic error management', 'Shield users from errors and provide recovery suited to mobile contexts.'),
   ], cat='Mobile & touch', conf='medium')
HS('smash', 'SMASH: SMArtphone usability heuristics', 'R. Inostroza, C. Rusu, S. Roncagliolo, V. Rusu & C. Collazos', '2012/2016',
   'Inostroza, R., Rusu, C., Roncagliolo, S., Rusu, V., & Collazos, C. A. (2016). Developing SMASH: A set of SMArtphone\'s uSability Heuristics. Computer Standards & Interfaces, 43, 40–52.', 'smartphones / touchscreen', [
    ('Visibility of system status', 'The device keeps users informed of what is happening through appropriate feedback.'),
    ('Match between system and the real world', 'The device speaks the users’ language with familiar concepts.'),
    ('User control and freedom', 'The device allows users to undo and redo actions and exit unwanted states.'),
    ('Consistency and standards', 'The device follows established conventions.'),
    ('Error prevention', 'The device prevents errors through careful design.'),
    ('Minimize the user’s memory load', 'Objects, actions and options are visible.'),
    ('Customization and shortcuts', 'The device provides basic and advanced configuration options and shortcuts.'),
    ('Efficiency of use and performance', 'The device performs tasks efficiently and responds quickly.'),
    ('Aesthetic and minimalist design', 'The device avoids irrelevant information.'),
    ('Help users recognize, diagnose and recover from errors', 'Error messages are clear and constructive.'),
    ('Help and documentation', 'The device provides easy-to-find help.'),
    ('Physical interaction and ergonomics', 'The device provides physical buttons/touch areas in positions and sizes users can reach and press comfortably.'),
   ], cat='Mobile & touch', conf='medium')
HS('pinelle-games', 'Heuristic evaluation for games (Pinelle, Wong & Stach)', 'David Pinelle, Nelson Wong & Tadeusz Stach', 2008,
   'Pinelle, D., Wong, N., & Stach, T. (2008). Heuristic evaluation for games: Usability principles for video game design. CHI \'08, 1453–1462.', 'video games', [
    ('Provide consistent responses to the user’s actions', 'Game objects and controls respond predictably and consistently.'),
    ('Allow users to customize video and audio settings, difficulty and game speed', 'Let players adjust settings to their abilities and preferences.'),
    ('Provide predictable and reasonable behavior for computer-controlled units', 'AI-controlled entities behave sensibly.'),
    ('Provide unobstructed views appropriate for the user’s current actions', 'Camera and views support the current task.'),
    ('Allow users to skip non-playable and frequently repeated content', 'Cutscenes and repeated sequences can be skipped.'),
    ('Provide intuitive and customizable input mappings', 'Controls follow conventions and can be remapped.'),
    ('Provide controls that are easy to manage, with appropriate sensitivity and responsiveness', 'Controls are responsive and not overly sensitive.'),
    ('Provide users with information on game status', 'Players know their status, goals and resources.'),
    ('Provide instructions, training and help', 'Players can learn the game.'),
    ('Provide visual representations that are easy to interpret and minimize micromanagement', 'Graphics are clear and reduce unnecessary management.'),
   ], cat='Games')
HS('desurvire-hep', 'Heuristic Evaluation for Playability (HEP) categories', 'Heather Desurvire, Martin Caplan & Jozsef Toth', 2004,
   'Desurvire, H., Caplan, M., & Toth, J. A. (2004). Using heuristics to evaluate the playability of games. CHI \'04 Extended Abstracts, 1509–1512.', 'video games', [
    ('Game play', 'Heuristics about challenge, goals, pacing, rewards and fairness (e.g., the player should not experience fatigue or boredom; challenge should be appropriate).'),
    ('Game story', 'Heuristics about narrative, characters and the player’s emotional engagement with the story world.'),
    ('Mechanics', 'Heuristics about how the game world responds to the player and how the game engine behaves.'),
    ('Usability', 'Heuristics about interface, controls, feedback, status, help and error recovery.'),
   ], cat='Games', note='43 heuristics in 4 categories; categories summarized here.')
HS('langevin-ca', 'Heuristics for conversational agents', 'Raina Langevin, Ross Lordon, Thi Avrahami, Benjamin Cowan, Tad Hirsch & Gary Hsieh', 2021,
   'Langevin, R. et al. (2021). Heuristic Evaluation of Conversational Agents. CHI \'21, Paper 632. (Best Paper)', 'chatbots & voice assistants', [
    ('Visibility of system status', 'The agent keeps users informed (e.g., typing indicators, confirmation of what it understood).'),
    ('Match between system and the real world', 'The agent uses natural language and concepts familiar to the user and follows conversational norms.'),
    ('User control and freedom', 'Users can easily exit, restart, go back, or get to a human.'),
    ('Consistency and standards', 'The agent’s personality, terms and behaviors are consistent.'),
    ('Error prevention', 'The agent prevents misunderstandings (e.g., confirming critical inputs, offering suggested replies).'),
    ('Help and guidance', 'The agent communicates what it can do and how to interact with it.'),
    ('Flexibility and efficiency of use', 'The agent accepts varied phrasing and offers shortcuts for experienced users.'),
    ('Aesthetic, minimalist and engaging design', 'Responses are concise and engaging without irrelevant content.'),
    ('Help users recognize, diagnose and recover from errors', 'When it fails to understand, the agent explains and offers a way forward.'),
    ('Context preservation', 'The agent maintains context across turns and sessions so users do not need to repeat themselves.'),
    ('Trustworthiness', 'The agent is transparent about being a bot, about data use, and about its limitations.'),
   ], cat='AI & automation', conf='medium', note='First five confirmed via author blog; remaining names from memory of the paper; verify against the CHI paper.')
HS('grice', "Grice's maxims of conversation (cooperative principle)", 'H. Paul Grice', 1975,
   'Grice, H. P. (1975). Logic and conversation. In Cole & Morgan (Eds.), Syntax and Semantics 3: Speech Acts, 41–58.', 'conversational UI, microcopy', [
    ('Maxim of quantity', 'Be as informative as required, and no more informative than required.'),
    ('Maxim of quality', 'Do not say what you believe to be false or lack adequate evidence for.'),
    ('Maxim of relation', 'Be relevant.'),
    ('Maxim of manner', 'Be clear: avoid obscurity and ambiguity, be brief and orderly.'),
   ], cat='Content & microcopy')
HS('zhang-medical', 'Heuristics for medical device usability', 'Jiajie Zhang, Todd Johnson, Vimla Patel, Danielle Paige & Tate Kubose', 2003,
   'Zhang, J., Johnson, T. R., Patel, V. L., Paige, D. L., & Kubose, T. (2003). Using usability heuristics to evaluate patient safety of medical devices. Journal of Biomedical Informatics, 36(1–2), 23–30.', 'medical devices & clinical systems', [
    ('Consistency and standards', 'Users should not have to wonder whether different words, situations or actions mean the same thing.'),
    ('Visibility of system state', 'Users should be informed about what is going on through appropriate feedback and display of information.'),
    ('Match between system and world', 'The image of the system should match the image of the task.'),
    ('Minimalist', 'Any extraneous information is a distraction and slows users down.'),
    ('Minimize memory load', 'Users should not be required to memorize a lot of information to carry out tasks.'),
    ('Informative feedback', 'Users should be given prompt and informative feedback about their actions.'),
    ('Flexibility and efficiency', 'Users always learn and differ in expertise; allow customization and shortcuts.'),
    ('Good error messages', 'Messages should be informative enough to let users understand the nature of errors, learn from them and recover.'),
    ('Prevent errors', 'It is better to design interfaces that prevent errors from happening in the first place.'),
    ('Clear closure', 'Every task has a beginning and an end; users should be clearly notified about task completion.'),
    ('Reversible actions', 'Users should be allowed to recover from errors; reversible actions encourage exploratory learning.'),
    ('Use users’ language', 'Language should always be presented in a form understandable by the intended users.'),
    ('Users in control', 'Do not give users the impression that they are controlled by the system.'),
    ('Help and documentation', 'Always provide help when needed.'),
   ], cat='Safety-critical')
HS('vis-mantra', "Shneiderman's visual information-seeking mantra and task taxonomy", 'Ben Shneiderman', 1996,
   'Shneiderman, B. (1996). The eyes have it: A task by data type taxonomy for information visualizations. IEEE Symposium on Visual Languages, 336–343.', 'data visualization & dashboards', [
    ('Overview first', 'Gain an overview of the entire collection.'),
    ('Zoom', 'Zoom in on items of interest.'),
    ('Filter', 'Filter out uninteresting items.'),
    ('Details-on-demand', 'Select an item or group and get details when needed.'),
    ('Relate', 'View relationships among items.'),
    ('History', 'Keep a history of actions to support undo, replay and progressive refinement.'),
    ('Extract', 'Allow extraction of sub-collections and of query parameters.'),
   ], cat='Data display & tables')
HS('tufte', "Tufte's principles of graphical excellence", 'Edward Tufte', 1983,
   'Tufte, E. R. (1983). The Visual Display of Quantitative Information. Graphics Press.', 'data visualization', [
    ('Show the data', 'Above all else, show the data; graphics should induce the viewer to think about the substance.'),
    ('Maximize the data-ink ratio', 'Devote most of the ink in a graphic to data; erase non-data ink and redundant data ink, within reason.'),
    ('Avoid chartjunk', 'Remove decoration, heavy grids, 3D effects and moiré patterns that do not convey information.'),
    ('Graphical integrity (lie factor)', 'Representation of numbers should be directly proportional to the numerical quantities; the lie factor (size of effect in graphic ÷ size of effect in data) should be close to 1.'),
    ('Use small multiples', 'Series of similar small charts using the same scale enable comparison.'),
    ('High data density where appropriate', 'Well-designed graphics can show a lot of data in small space without clutter.'),
   ], cat='Data display & tables')
HS('cleveland-mcgill', 'Cleveland & McGill ranking of graphical perception', 'William Cleveland & Robert McGill', 1984,
   'Cleveland, W. S. & McGill, R. (1984). Graphical perception: Theory, experimentation, and application to the development of graphical methods. JASA, 79(387), 531–554.', 'data visualization', [
    ('Position along a common scale (most accurate)', 'Use aligned positions (bar charts, dot plots) for the most accurate quantitative comparisons.'),
    ('Position along non-aligned scales', 'Next most accurate (small multiples with separate axes).'),
    ('Length, direction, angle', 'Moderately accurate; pie-chart angles are harder to compare than bar lengths.'),
    ('Area', 'Less accurate.'),
    ('Volume, curvature', 'Even less accurate.'),
    ('Shading, color saturation (least accurate)', 'Least accurate for quantitative judgments; use for categories or rough magnitudes.'),
   ], cat='Data display & tables')
HS('forsell-johansson', 'Heuristics for information visualization evaluation', 'Camilla Forsell & Jimmy Johansson', 2010,
   'Forsell, C. & Johansson, J. (2010). An heuristic set for evaluation in information visualization. AVI \'10, 199–206.', 'data visualization', [
    ('Information coding', 'Perception of information depends on the mapping of data elements to visual objects.'),
    ('Minimal actions', 'The number of actions needed to accomplish a goal or task is minimal.'),
    ('Flexibility', 'The number of possible ways to achieve a goal is sufficient; users can customize.'),
    ('Orientation and help', 'Users are supported in controlling level of detail, redoing/undoing, and getting help.'),
    ('Spatial organization', 'Users are oriented within the visualization (layout, locating elements, avoiding occlusion).'),
    ('Consistency', 'Design choices are maintained in similar contexts.'),
    ('Recognition rather than recall', 'Users do not have to memorize information to carry out tasks.'),
    ('Prompting', 'Means are available to guide users toward particular actions.'),
    ('Remove the extraneous', 'Extra information can distract and slow users down.'),
    ('Data set reduction', 'Features are available for reducing a data set to what is relevant.'),
   ], cat='Data display & tables', conf='medium')
HS('stanford-credibility', 'Stanford Web Credibility Guidelines', 'B. J. Fogg (Stanford Persuasive Technology Lab)', 2002,
   'Fogg, B. J. (2002). Stanford Guidelines for Web Credibility. Stanford Persuasive Technology Lab; based on research with 4,500+ participants (Fogg et al. 2001, 2003).', 'websites', [
    ('Make it easy to verify the accuracy of the information on your site', 'Provide citations, references and source material.'),
    ('Show that there is a real organization behind your site', 'Show a physical address, photos of offices, membership details.'),
    ('Highlight the expertise in your organization and in the content and services you provide', 'Show credentials and affiliations; do not link to less credible sites.'),
    ('Show that honest and trustworthy people stand behind your site', 'Show real people with bios.'),
    ('Make it easy to contact you', 'Clear phone, email and address.'),
    ('Design your site so it looks professional (or is appropriate for your purpose)', 'Visual design matters to credibility judgments.'),
    ('Make your site easy to use and useful', 'Usability contributes to credibility.'),
    ('Update your site’s content often (at least show it has been reviewed recently)', 'Show dates of updates.'),
    ('Use restraint with any promotional content (e.g., ads, offers)', 'Avoid ads that are confused with content and pop-ups.'),
    ('Avoid errors of all types, no matter how small they seem', 'Typos and broken links damage credibility.'),
   ], cat='Trust & credibility')
HS('psd', 'Persuasive Systems Design (PSD) principles', 'Harri Oinas-Kukkonen & Marja Harjumaa', 2009,
   'Oinas-Kukkonen, H. & Harjumaa, M. (2009). Persuasive systems design: Key issues, process model, and system features. CAIS, 24, Article 28.', 'behavior change systems', [
    ('Primary task support: Reduction', 'Reduce complex behavior into simple tasks.'), ('Primary task support: Tunneling', 'Guide users through a process step by step.'),
    ('Primary task support: Tailoring', 'Tailor information to user groups.'), ('Primary task support: Personalization', 'Offer personalized content and services.'),
    ('Primary task support: Self-monitoring', 'Let users track their own performance or status.'), ('Primary task support: Simulation', 'Show the cause-and-effect link of behavior.'),
    ('Primary task support: Rehearsal', 'Allow users to rehearse a behavior.'),
    ('Dialogue support: Praise', 'Praise users for target behaviors.'), ('Dialogue support: Rewards', 'Reward target behaviors.'), ('Dialogue support: Reminders', 'Remind users of target behaviors.'),
    ('Dialogue support: Suggestion', 'Offer fitting suggestions.'), ('Dialogue support: Similarity', 'Remind users of themselves in a meaningful way.'), ('Dialogue support: Liking', 'Be visually attractive.'),
    ('Dialogue support: Social role', 'Adopt a social role (e.g., assistant).'),
    ('System credibility: Trustworthiness', 'Provide truthful, fair, unbiased information.'), ('System credibility: Expertise', 'Show knowledge, experience and competence.'),
    ('System credibility: Surface credibility', 'Give a competent look and feel.'), ('System credibility: Real-world feel', 'Show the organization and people behind the content.'),
    ('System credibility: Authority', 'Refer to authoritative people or organizations.'), ('System credibility: Third-party endorsements', 'Show endorsements from respected sources.'),
    ('System credibility: Verifiability', 'Allow verification of content accuracy through outside sources.'),
    ('Social support: Social learning', 'Let users observe others performing the behavior.'), ('Social support: Social comparison', 'Let users compare performance with others.'),
    ('Social support: Normative influence', 'Leverage peer pressure and norms.'), ('Social support: Social facilitation', 'Show that others are performing the behavior.'),
    ('Social support: Cooperation', 'Leverage cooperation.'), ('Social support: Competition', 'Leverage competition.'), ('Social support: Recognition', 'Offer public recognition.'),
   ], cat='Persuasion & behavior change')
HS('privacy-by-design', 'Privacy by Design: 7 foundational principles', 'Ann Cavoukian', 2009,
   'Cavoukian, A. (2009). Privacy by Design: The 7 Foundational Principles. Information and Privacy Commissioner of Ontario.', 'products handling personal data', [
    ('Proactive not reactive; preventative not remedial', 'Anticipate and prevent privacy-invasive events before they happen.'),
    ('Privacy as the default setting', 'Personal data is automatically protected; no action is required by the individual.'),
    ('Privacy embedded into design', 'Privacy is an essential component of core functionality, not a bolt-on.'),
    ('Full functionality: positive-sum, not zero-sum', 'Accommodate all legitimate interests without false trade-offs such as privacy vs security.'),
    ('End-to-end security: full lifecycle protection', 'Data is securely retained and destroyed at the end of the process.'),
    ('Visibility and transparency', 'Operations remain visible and transparent to users and providers.'),
    ('Respect for user privacy: keep it user-centric', 'Strong privacy defaults, appropriate notice and empowering user-friendly options.'),
   ], cat='Authentication, security & privacy')
HS('saltzer-schroeder', 'Saltzer & Schroeder security design principles (usability-relevant)', 'Jerome Saltzer & Michael Schroeder', 1975,
   'Saltzer, J. H. & Schroeder, M. D. (1975). The protection of information in computer systems. Proceedings of the IEEE, 63(9), 1278–1308.', 'security UX', [
    ('Psychological acceptability', 'The human interface must be designed for ease of use so users routinely and automatically apply protection mechanisms correctly; the mental image of protection goals should match the mechanisms.'),
    ('Fail-safe defaults', 'Base access decisions on permission rather than exclusion; default to the safe state.'),
    ('Least privilege', 'Every program and user should operate using the least set of privileges necessary.'),
    ('Economy of mechanism', 'Keep the design as simple and small as possible.'),
   ], cat='Authentication, security & privacy')
HS('whitten-tygar', 'Why Johnny Can’t Encrypt: properties that make security usability hard', 'Alma Whitten & J. D. Tygar', 1999,
   'Whitten, A. & Tygar, J. D. (1999). Why Johnny can\'t encrypt: A usability evaluation of PGP 5.0. USENIX Security Symposium.', 'security UX', [
    ('Unmotivated user property', 'Security is usually a secondary goal; users will not go out of their way to learn it.'),
    ('Abstraction property', 'Security policies are abstract and alien to non-experts.'),
    ('Lack of feedback property', 'It is hard to give good feedback for security because the correct state is complex.'),
    ('Barn door property', 'Once a secret is exposed, it cannot be taken back, so errors must be prevented up front.'),
    ('Weakest link property', 'Security is only as strong as its weakest component, so users must be guided through all aspects.'),
   ], cat='Authentication, security & privacy')
HS('quality-components', "Nielsen's five quality components of usability", 'Jakob Nielsen', '1993/2012',
   'Nielsen, J. (1993). Usability Engineering. Academic Press; Nielsen, J. (2012). Usability 101. NN/g.', 'all', [
    ('Learnability', 'How easy is it for users to accomplish basic tasks the first time they encounter the design?'),
    ('Efficiency', 'Once users have learned the design, how quickly can they perform tasks?'),
    ('Memorability', 'When users return after a period of not using it, how easily can they reestablish proficiency?'),
    ('Errors', 'How many errors do users make, how severe are they, and how easily can they recover?'),
    ('Satisfaction', 'How pleasant is it to use the design?'),
   ], cat='Usability definitions')
HS('iso9241-11', 'ISO 9241-11 definition of usability', 'ISO', '1998 (rev. 2018)',
   'ISO 9241-11:2018. Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts.', 'all', [
    ('Effectiveness', 'Accuracy and completeness with which users achieve specified goals.'),
    ('Efficiency', 'Resources (time, effort, cost) used in relation to the results achieved.'),
    ('Satisfaction', 'The extent to which the user’s physical, cognitive and emotional responses from use meet their needs and expectations.'),
    ('Context of use', 'Usability is always relative to specified users, goals, tasks, resources and environment.'),
   ], cat='Usability definitions')
HS('quesenbery-5e', "Quesenbery's 5Es of usability", 'Whitney Quesenbery', '2001/2004',
   'Quesenbery, W. (2004). Balancing the 5Es of Usability. Cutter IT Journal, 17(2).', 'all', [
    ('Effective', 'The completeness and accuracy with which users achieve their goals.'),
    ('Efficient', 'The speed and accuracy with which users can complete tasks.'),
    ('Engaging', 'The degree to which the interface is pleasant and satisfying to use.'),
    ('Error tolerant', 'How well the design prevents errors and helps users recover.'),
    ('Easy to learn', 'How well the product supports initial orientation and deepening understanding.'),
   ], cat='Usability definitions')
HS('honeycomb', "Morville's user experience honeycomb", 'Peter Morville', 2004,
   'Morville, P. (2004). User Experience Design (the UX honeycomb). Semantic Studios.', 'all', [
    ('Useful', 'Content and functions fill a genuine need.'), ('Usable', 'The system is easy to use.'), ('Desirable', 'Image, identity, brand and design evoke emotion and appreciation.'),
    ('Findable', 'Content is navigable and locatable.'), ('Accessible', 'Usable by people with disabilities.'), ('Credible', 'Users trust and believe what you tell them.'), ('Valuable', 'Delivers value to sponsors and users.'),
   ], cat='Usability definitions')
HS('garrett-elements', "Garrett's Elements of User Experience", 'Jesse James Garrett', 2000,
   'Garrett, J. J. (2000/2002). The Elements of User Experience. New Riders.', 'all', [
    ('Strategy', 'User needs and business objectives.'), ('Scope', 'Functional specifications and content requirements.'),
    ('Structure', 'Interaction design and information architecture.'), ('Skeleton', 'Interface design, navigation design and information design.'), ('Surface', 'Sensory (visual) design.'),
   ], cat='Usability definitions', layer='organizational / research')
HS('krug', "Krug's principles (Don't Make Me Think)", 'Steve Krug', 2000,
   'Krug, S. (2000; 3rd ed. 2014). Don\'t Make Me Think: A Common Sense Approach to Web Usability. New Riders.', 'websites & apps', [
    ('Don’t make me think', 'Pages should be self-evident or at least self-explanatory; every question mark in the user’s head adds cognitive load.'),
    ('Users scan, satisfice and muddle through', 'Design for scanning (clear hierarchy, conventions, defined areas, obvious clickables, low noise).'),
    ('Mindless, unambiguous clicks', 'The number of clicks matters less than whether each click is an easy, unambiguous choice.'),
    ('Omit needless words', 'Get rid of half the words on each page, then get rid of half of what is left.'),
    ('The trunk test', 'On any page, users should be able to tell: what site this is, what page they are on, the major sections, their options at this level, where they are in the scheme, and how to search.'),
    ('The reservoir of goodwill', 'Every friction (hidden information, punishing format rules, unnecessary questions, amateurish design) drains users’ goodwill; helpfulness refills it.'),
   ], url='https://sensible.com/dont-make-me-think/')
HS('dan-brown-ia', "Dan Brown's eight principles of information architecture", 'Dan Brown', 2010,
   'Brown, D. (2010). Eight principles of information architecture. Bulletin of the ASIS&T, 36(6), 30–34.', 'information architecture', [
    ('Principle of objects', 'Treat content as living things with lifecycles, behaviors and attributes.'),
    ('Principle of choices', 'Create pages that offer meaningful choices, keeping the range of choices focused on a particular task.'),
    ('Principle of disclosure', 'Show only enough information to help people understand what they will find as they dig deeper.'),
    ('Principle of exemplars', 'Describe the contents of categories by showing examples.'),
    ('Principle of front doors', 'Assume at least half of visitors come through some page other than the home page.'),
    ('Principle of multiple classification', 'Offer several different classification schemes to browse the content.'),
    ('Principle of focused navigation', 'Do not mix apples and oranges in navigation schemes.'),
    ('Principle of growth', 'Assume the content you have today is a small fraction of what you will have tomorrow.'),
   ], cat='Navigation & IA')
HS('saffer-microinteractions', 'Microinteractions model', 'Dan Saffer', 2013,
   'Saffer, D. (2013). Microinteractions: Designing with Details. O\'Reilly.', 'UI details', [
    ('Triggers', 'What initiates the microinteraction (user-initiated control or system condition); make manual triggers recognizable and in the expected place.'),
    ('Rules', 'What can and cannot happen in the microinteraction; rules should be simple and constraints visible.'),
    ('Feedback', 'How the user knows what is happening; use the least amount of feedback that conveys the message, using existing UI elements.'),
    ('Loops and modes', 'How the microinteraction changes over time or with repeated use; avoid modes where possible.'),
   ])
HS('error-messages', 'Error message guidelines', 'B. Shneiderman; J. Nielsen', '1982/2001',
   'Shneiderman, B. (1982). System message design: Guidelines and experimental results. In Badre & Shneiderman (Eds.), Directions in HCI; Nielsen, J. (2001). Error Message Guidelines. NN/g.', 'all', [
    ('Explicit and visible', 'Indicate clearly that something has gone wrong, with highly visible, redundant cues near the source of the error.'),
    ('Human-readable language', 'Use plain language, not codes or technical jargon.'),
    ('Polite and non-blaming', 'Do not blame the user or imply they are stupid; avoid hostile words (fatal, illegal, abort).'),
    ('Precise', 'Describe exactly what went wrong rather than "an error occurred".'),
    ('Constructive', 'Tell users how to fix the problem.'),
    ('Preserve user input', 'Keep what the user typed so they can correct rather than re-enter.'),
    ('Reduce the work of correction', 'Offer suggestions or the most likely correct values.'),
   ], cat='Errors & recovery')
HS('ui-states', 'Complete set of UI states to design', 'Common practice (e.g., S. Hurff 2015, "UI Stack")', 2015,
   'Hurff, S. (2015). How to fix a bad user interface (the UI Stack: ideal, empty, error, partial, loading states). Scott Hurff blog.', 'all screens', [
    ('Ideal state', 'The screen with typical, complete data.'),
    ('Empty state', 'First use or no data: explain what will appear and how to get started.'),
    ('Loading state', 'What users see while content loads (skeletons, progress).'),
    ('Partial state', 'Sparse data: guide users toward the ideal state.'),
    ('Error state', 'What happens when things go wrong, with recovery paths.'),
   ], cat='Feedback & system status', conf='medium')
HS('value-sensitive-design', 'Value Sensitive Design', 'Batya Friedman', 1996,
   'Friedman, B. (1996). Value-sensitive design. ACM Interactions, 3(6), 16–23; Friedman, B. & Hendry, D. (2019). Value Sensitive Design. MIT Press.', 'ethics', [
    ('Conceptual investigations', 'Identify direct and indirect stakeholders and the values at stake (privacy, autonomy, trust, fairness).'),
    ('Empirical investigations', 'Study how stakeholders experience and prioritize values in context.'),
    ('Technical investigations', 'Examine how technology properties support or hinder values, and design accordingly.'),
   ], cat='Ethics', layer='organizational / research')
HS('pour', 'POUR principles of accessibility', 'W3C WAI', 2008,
   'W3C (2008). WCAG 2.0 principles.', 'web & apps', [
    ('Perceivable', 'Information and UI components must be presentable to users in ways they can perceive.'),
    ('Operable', 'UI components and navigation must be operable.'),
    ('Understandable', 'Information and the operation of the UI must be understandable.'),
    ('Robust', 'Content must be robust enough to be interpreted reliably by a wide variety of user agents, including assistive technologies.'),
   ], cat='Accessibility')
HS('dark-ux-ethics', 'Humane / ethical design questions', 'Center for Humane Technology; ethical design literature', '2018',
   'Center for Humane Technology (2018). Humane design guide; Gray, C. M. & Chivukula, S. S. (2019). Ethical mediation in UX practice. CHI \'19.', 'all', [
    ('Respect attention', 'Does the product respect users’ time and attention, with natural stopping points?'),
    ('Respect autonomy', 'Can users make informed choices free from manipulation?'),
    ('Support well-being', 'Does the product leave users better off, not just more engaged?'),
    ('Be honest about business model', 'Is it clear how the product makes money and how data is used?'),
   ], cat='Ethics', conf='medium')

write('curated_heuristics', R)
with open(OUT + '/heuristic_sets_index.jsonl', 'w') as f:
    for s in SETS: f.write(json.dumps(s, ensure_ascii=False) + '\n')
print('sets', len(SETS))
