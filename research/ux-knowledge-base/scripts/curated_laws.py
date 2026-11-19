from common import *
P = 'Perception & attention'; M = 'Memory & cognition'; MO = 'Motor control & input'; D = 'Decision-making & behavior'
T = 'Time & performance perception'; S = 'Systems & design laws'; E = 'Error & human factors'; EM = 'Emotion & aesthetics'
I = 'Interaction models'; L = 'Learning & skill'; ME = 'Measurement & research'
SS = 'Curated: laws & principles'
R = []
def add(*a, **k): R.append(C(*a, source_set=SS, **k))

# ---------------- Perception & attention ----------------
add('law.weber-fechner', "Weber's law / Weber–Fechner law", 'E. H. Weber; G. T. Fechner', '1834/1860',
    'The smallest noticeable difference in a stimulus (size, brightness, weight) is a constant proportion of the original stimulus, so perceived intensity grows roughly with the logarithm of physical intensity.',
    'Differences in size, weight, color or spacing that are meant to signal hierarchy must be proportionally large enough to be noticed; tiny increments between heading levels or states read as identical.',
    'Are differences between hierarchy levels and states (heading sizes, active vs inactive, selected vs unselected) large enough to be noticed at a glance?', 'screen', 'JND is a constant ratio (e.g., ~2% for brightness in lab conditions); use clearly distinct steps such as a type scale ratio of 1.2 or more.',
    'Fechner, G. T. (1860). Elemente der Psychophysik. Precursor to the 1900–present period, still foundational.', P, 'Psychophysics', conf='high')
add('law.stevens-power', "Stevens' power law", 'S. S. Stevens', 1957,
    'Perceived magnitude grows as a power function of physical magnitude, with a different exponent per sense; perceived area grows more slowly than actual area.',
    'Area-based encodings (bubble charts, icon sizes) are systematically underestimated; prefer length/position encodings for quantitative comparison.',
    'Do charts encode quantities with position or length rather than area or volume when accurate comparison matters?', 'screen', 'Exponent ~0.7 for area, ~1.0 for length, ~3.5 for electric shock.',
    'Stevens, S. S. (1957). On the psychophysical law. Psychological Review, 64(3), 153–181.', P, 'Psychophysics')
add('gestalt.pragnanz', 'Law of Prägnanz (simplicity / good figure)', 'M. Wertheimer; K. Koffka; W. Köhler', '1923/1935',
    'People perceive ambiguous or complex images in the simplest form possible, because that interpretation needs the least cognitive effort.',
    'Simple, regular shapes and layouts are processed faster; visually complex compositions get mentally simplified, sometimes wrongly.',
    'Can the layout be understood as a few simple groups and shapes, or does it require effort to parse?', 'screen', '',
    'Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt II. Psychologische Forschung, 4, 301–350; Koffka, K. (1935). Principles of Gestalt Psychology.', P, 'Gestalt')
add('gestalt.proximity', 'Law of proximity', 'M. Wertheimer', 1923,
    'Objects that are near each other are perceived as a group.',
    'Spacing is the primary tool for grouping: labels must be closer to their own field than to neighbouring fields; related controls should sit together and unrelated ones apart.',
    'Is each label, caption and helper text closer to the element it describes than to any other element? Is spacing between groups larger than spacing within groups?', 'deterministic (partial) + screen',
    'Inter-group spacing should be noticeably larger than intra-group spacing (commonly ≥ 2×).', 'Wertheimer (1923), Psychologische Forschung 4.', P, 'Gestalt')
add('gestalt.similarity', 'Law of similarity', 'M. Wertheimer', 1923,
    'Elements that share visual characteristics (color, shape, size, orientation) are perceived as related or as having the same function.',
    'Things that look the same must behave the same; links, buttons and interactive states need consistent styling, and non-interactive elements must not mimic interactive styling.',
    'Do all elements with the same function share the same visual treatment, and do elements with different functions look different?', 'screen', '',
    'Wertheimer (1923).', P, 'Gestalt')
add('gestalt.closure', 'Law of closure', 'Gestalt psychologists', '1920s',
    'People mentally complete incomplete shapes and perceive a whole even when parts are missing.',
    'Icons and logos can be minimal; also explains why partially visible content (a cut-off card) signals that more content can be scrolled.',
    'Where horizontal scrolling or more content exists, is part of the next item visible to signal continuation?', 'screen', '',
    'Koffka (1935). Principles of Gestalt Psychology.', P, 'Gestalt')
add('gestalt.continuity', 'Law of continuity (good continuation)', 'M. Wertheimer', 1923,
    'Elements arranged on a line or curve are perceived as more related than elements not on the line.',
    'Align items on clear axes; carousels, timelines, and step indicators rely on continuity to show sequence.',
    'Are related items aligned along a common axis so the eye follows them in order?', 'screen', '', 'Wertheimer (1923).', P, 'Gestalt')
add('gestalt.common-fate', 'Law of common fate', 'M. Wertheimer', 1923,
    'Elements that move together in the same direction are perceived as a group.',
    'Animate related elements together; elements that move independently are read as separate.',
    'When items animate, do grouped items move together and unrelated items move separately?', 'screen', '', 'Wertheimer (1923).', P, 'Gestalt')
add('gestalt.figure-ground', 'Figure–ground', 'E. Rubin', 1915,
    'People instinctively separate a visual field into a figure (foreground object) and ground (background).',
    'Modals, menus and popovers need clear separation (scrim, shadow, contrast) from the background; low contrast between figure and ground causes ambiguity.',
    'Are overlays, dialogs and cards clearly separated from the background (scrim, elevation, border or contrast)?', 'screen', '',
    'Rubin, E. (1915). Synsoplevede Figurer.', P, 'Gestalt')
add('gestalt.symmetry', 'Law of symmetry and order', 'Gestalt psychologists', '1920s',
    'Symmetrical elements are perceived as belonging together and as a stable, coherent whole.',
    'Symmetric compositions feel orderly and calm; asymmetry can be used deliberately to draw attention.',
    'Is symmetry or deliberate asymmetry used purposefully rather than accidentally?', 'screen', '', 'Koffka (1935).', P, 'Gestalt', sev='minor')
add('gestalt.common-region', 'Law of common region', 'S. E. Palmer', 1992,
    'Elements located within the same bounded area (a box, card or background) are perceived as a group, even overriding proximity.',
    'Cards, panels, and shaded sections are strong grouping tools; misplaced borders create false groups.',
    'Do containers (cards, panels, backgrounds) enclose exactly the elements that belong together?', 'screen', '',
    'Palmer, S. E. (1992). Common region: A new principle of perceptual grouping. Cognitive Psychology, 24(3), 436–447.', P, 'Gestalt')
add('gestalt.uniform-connectedness', 'Law of uniform connectedness', 'S. E. Palmer & I. Rock', 1994,
    'Elements that are visually connected (by lines, arrows or shared color regions) are perceived as more related than elements without a connection.',
    'Connectors in steppers, flow diagrams and timelines strongly communicate relationship and sequence.',
    'Are relationships that matter (steps, hierarchy, links between items) shown with visual connectors where appropriate?', 'screen', '',
    'Palmer, S. & Rock, I. (1994). Rethinking perceptual organization: The role of uniform connectedness. Psychonomic Bulletin & Review, 1(1), 29–55.', P, 'Gestalt')
add('law.von-restorff', 'Von Restorff effect (isolation effect)', 'H. von Restorff', 1933,
    'When multiple similar items are present, the one that differs from the rest is most likely to be noticed and remembered.',
    'Make the primary action or key information visually distinct; but if many things are emphasized, nothing stands out. Do not rely on color alone to make the difference.',
    'Is there exactly one visually dominant primary action per view, distinct from secondary actions by more than color alone?', 'screen', '',
    'von Restorff, H. (1933). Über die Wirkung von Bereichsbildungen im Spurenfeld. Psychologische Forschung, 18, 299–342.', P, 'Attention')
add('law.preattentive', 'Preattentive processing / feature integration theory', 'A. Treisman & G. Gelade', 1980,
    'Some visual features (color hue, size, orientation, motion, enclosure) are detected in parallel in under ~250 ms without focused attention; conjunctions of features require slower serial search.',
    'Use a single distinctive preattentive feature to make critical items (errors, alerts, selected state) pop out; combinations of features do not pop out.',
    'Can critical status (errors, alerts, selection) be spotted within a glance because it differs in one strong visual feature?', 'screen', 'Preattentive detection typically < 200–250 ms.',
    'Treisman, A. & Gelade, G. (1980). A feature-integration theory of attention. Cognitive Psychology, 12(1), 97–136.', P, 'Attention')
add('law.inattentional-blindness', 'Inattentional blindness', 'A. Mack & I. Rock; D. Simons & C. Chabris', '1998/1999',
    'People engaged in a task often fail to notice unexpected, clearly visible objects outside their focus of attention.',
    'Messages placed away from where the user is working (e.g., a status message in a corner while the user is typing in a form) are frequently missed; place feedback at the locus of attention.',
    'Is feedback shown where the user is looking (next to the triggering control) rather than in a distant region?', 'screen', '',
    'Simons, D. J. & Chabris, C. F. (1999). Gorillas in our midst. Perception, 28(9), 1059–1074; Mack & Rock (1998). Inattentional Blindness. MIT Press.', P, 'Attention')
add('law.change-blindness', 'Change blindness', 'R. Rensink, J. K. O\'Regan & J. Clark', 1997,
    'People often fail to notice large changes to a scene when the change coincides with a visual disruption such as a page reload, flicker or scroll.',
    'Content that changes after a reload or during a transition (prices, cart counts, validation messages) may go unnoticed; animate or highlight changes and announce them to assistive technology.',
    'When content updates (cart count, totals, inline messages), is the change made noticeable (highlight, motion, focus or live region)?', 'flow', '',
    'Rensink, R. A., O\'Regan, J. K., & Clark, J. J. (1997). To see or not to see: The need for attention to perceive changes in scenes. Psychological Science, 8(5), 368–373.', P, 'Attention')
add('law.banner-blindness', 'Banner blindness', 'J. P. Benway & D. M. Lane', 1998,
    'Users tend to ignore page elements that look like advertisements or that sit in locations where ads usually appear, even when they contain useful information.',
    'Do not style important content or calls to action like ads (boxed, animated, flashy, in right rail or top banner positions).',
    'Is any important information or CTA styled or positioned in a way that resembles advertising?', 'screen', '',
    'Benway, J. P. & Lane, D. M. (1998). Banner blindness: Web searchers often miss "obvious" links. Internetworking, ITG Newsletter.', P, 'Attention')
add('law.f-pattern', 'F-shaped scanning pattern (and other scanning patterns)', 'J. Nielsen; K. Pernice (NN/g)', '2006/2017',
    'Eye-tracking shows that on text-heavy pages without strong formatting, users scan in an F-shape: across the top, then a shorter horizontal sweep, then down the left side. Other patterns include layer-cake (scanning headings), spotted, marking and commitment patterns.',
    'Front-load headings, links and bullet points with the most informative words; use clear subheadings so users can layer-cake scan instead of F-scan.',
    'Do headings, list items and link texts start with the information-carrying words? Is text broken up with descriptive subheadings?', 'screen', '',
    'Nielsen, J. (2006). F-Shaped Pattern for Reading Web Content. NN/g; Pernice, K. (2017). F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant. NN/g.', P, 'Visual scanning', conf='high')
add('law.gutenberg', 'Gutenberg diagram (reading gravity)', 'Attributed to E. Arnold', '1950s–1960s',
    'For evenly distributed, text-heavy layouts in left-to-right languages, the eye tends to move from the top-left (primary optical area) to the bottom-right (terminal area), with weaker attention to the other two quadrants.',
    'Place the final call to action where the reading path ends; mirror for right-to-left languages. Weaker than F-pattern evidence; treat as heuristic.',
    'In dense layouts, does the primary action sit where the reading path naturally terminates?', 'screen', '', 'Attributed to Edmund C. Arnold, newspaper design (mid-20th century).', P, 'Visual scanning', sev='minor', conf='medium')
add('law.cocktail-party', 'Selective attention / cocktail party effect', 'E. C. Cherry; D. Broadbent', '1953/1958',
    'People can focus on one stream of information while filtering others, but salient, personally relevant signals (such as one’s own name) break through the filter.',
    'Personalised or highly salient cues capture attention; use them sparingly for important events, not for marketing noise.',
    'Are attention-grabbing cues (name, sound, motion, badges) reserved for events that genuinely need attention?', 'screen', '',
    'Cherry, E. C. (1953). Some experiments on the recognition of speech, with one and with two ears. JASA, 25(5), 975–979; Broadbent, D. (1958). Perception and Communication.', P, 'Attention', sev='minor')
add('law.multiple-resources', 'Multiple resource theory', 'C. D. Wickens', '1984/2002',
    'People have separate pools of attentional resources (visual vs auditory, spatial vs verbal, perception vs response); tasks that compete for the same resource interfere more than tasks using different resources.',
    'In multitasking contexts (driving, monitoring, voice + screen), distribute information across modalities; avoid asking users to read while also reading.',
    'In contexts where the user is busy (driving, cooking, operating equipment), is information delivered through a modality that is not already occupied?', 'flow', '',
    'Wickens, C. D. (2002). Multiple resources and performance prediction. Theoretical Issues in Ergonomics Science, 3(2), 159–177.', P, 'Attention')
add('law.situation-awareness', 'Situation awareness (3 levels)', 'M. R. Endsley', 1995,
    'Situation awareness has three levels: perception of elements in the environment, comprehension of their meaning, and projection of their future status.',
    'Dashboards and monitoring tools should support all three levels: show current state, explain what it means, and indicate trends or predictions.',
    'Does the dashboard or status view show what is happening, what it means, and what is likely to happen next?', 'screen', '',
    'Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. Human Factors, 37(1), 32–64.', P, 'Monitoring')

# ---------------- Memory & cognition ----------------
add('law.miller', "Miller's law (7 ± 2)", 'G. A. Miller', 1956,
    'The span of immediate memory is limited to roughly seven (plus or minus two) chunks of information; later research (Cowan 2001) suggests closer to four chunks.',
    'Do not require users to hold many items in memory across steps; chunk information (phone numbers, codes) and keep critical information visible. Do NOT misuse it to cap menu lengths: menus are recognized, not memorized.',
    'Does any step require remembering information shown on a previous screen? Are long codes and numbers chunked?', 'flow', '7 ± 2 chunks (Miller 1956); ~4 ± 1 chunks (Cowan 2001).',
    'Miller, G. A. (1956). The magical number seven, plus or minus two. Psychological Review, 63(2), 81–97.', M, 'Working memory')
add('law.cowan', 'Working memory capacity of ~4 chunks', 'N. Cowan', 2001,
    'When rehearsal and chunking are prevented, adults hold about 3–5 meaningful chunks in working memory.',
    'Design for a working memory limit of around four items: comparisons, multi-step instructions, and options to remember should be kept small or kept on screen.',
    'Does any task require comparing or remembering more than ~4 items without them being visible together?', 'flow', '~4 ± 1 chunks',
    'Cowan, N. (2001). The magical number 4 in short-term memory. Behavioral and Brain Sciences, 24(1), 87–114.', M, 'Working memory')
add('law.chunking', 'Chunking', 'G. A. Miller; W. Chase & H. Simon', '1956/1973',
    'Grouping individual pieces of information into larger meaningful units increases how much can be held and processed.',
    'Format long numbers and codes in groups (e.g., 4-4-4-4 for card numbers), split long forms into logical sections, and group content under headings.',
    'Are long strings (card numbers, IBANs, phone numbers, codes) displayed and accepted in chunked format? Are long forms and pages divided into labeled groups?', 'screen', '',
    'Chase, W. G. & Simon, H. A. (1973). Perception in chess. Cognitive Psychology, 4(1), 55–81.', M, 'Working memory')
add('law.working-memory-model', 'Working memory model', 'A. Baddeley & G. Hitch', 1974,
    'Working memory consists of a central executive, a phonological loop (verbal), a visuospatial sketchpad and (added 2000) an episodic buffer, each with limited capacity.',
    'Verbal and visual information can be processed partly in parallel; overloading one channel (e.g., long spoken instructions in voice UIs) quickly exceeds capacity.',
    'In voice and audio interfaces, are spoken lists and instructions short enough to be held in the phonological loop (about 3–5 items)?', 'flow', '',
    'Baddeley, A. D. & Hitch, G. (1974). Working memory. Psychology of Learning and Motivation, 8, 47–89.', M, 'Working memory')
add('law.cognitive-load', 'Cognitive load theory', 'J. Sweller', 1988,
    'Learning and task performance suffer when total cognitive load exceeds working memory capacity. Load is intrinsic (task complexity), extraneous (caused by poor presentation) and germane (useful effort).',
    'Remove extraneous load: unnecessary decoration, split attention between distant related items, redundant text, unclear navigation.',
    'Is there content, decoration or interaction that adds effort without helping the user complete their task?', 'screen', '',
    'Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. Cognitive Science, 12(2), 257–285.', M, 'Cognitive load')
add('law.split-attention', 'Split-attention effect', 'P. Chandler & J. Sweller', 1991,
    'When people must mentally integrate information from separate sources (a diagram and its distant legend), cognitive load rises and performance drops.',
    'Put labels directly on charts, place help text beside the field it explains, and keep error messages next to the input in error.',
    'Are legends, help texts and error messages placed adjacent to the items they refer to?', 'screen', '',
    'Chandler, P. & Sweller, J. (1991). Cognitive load theory and the format of instruction. Cognition and Instruction, 8(4), 293–332.', M, 'Cognitive load')
add('law.recognition-over-recall', 'Recognition is easier than recall', 'Memory research (e.g., Shepard 1967; Standing 1973)', '1967/1973',
    'People are far better at recognizing previously seen information than at recalling it unaided; recognition memory for pictures is extremely large.',
    'Show options, recent items, examples and visible menus instead of requiring users to remember commands, codes or prior answers.',
    'Can users choose from visible options (menus, suggestions, recent items) rather than having to remember and type values?', 'screen', '',
    'Shepard, R. N. (1967). Recognition memory for words, sentences, and pictures. JVLVB, 6(1), 156–163; Standing, L. (1973). Learning 10,000 pictures. QJEP, 25(2), 207–222.', M, 'Long-term memory')
add('law.picture-superiority', 'Picture superiority effect / dual coding', 'A. Paivio', 1971,
    'Information presented as pictures (or pictures plus words) is remembered better than words alone, because it is encoded both verbally and visually.',
    'Pair icons with text labels; use illustrations for key concepts. Icons alone are often ambiguous, but icon + label beats either alone.',
    'Are icons accompanied by visible text labels, especially for less common actions?', 'screen', '',
    'Paivio, A. (1971). Imagery and Verbal Processes. Holt, Rinehart & Winston.', M, 'Long-term memory')
add('law.serial-position', 'Serial position effect (primacy & recency)', 'H. Ebbinghaus; B. Murdock', '1885/1962',
    'Items at the beginning (primacy) and end (recency) of a list are remembered best; middle items are most easily forgotten.',
    'Place the most important navigation items and options first and last; avoid burying key items in the middle of long lists.',
    'Are the most important items placed at the start or end of navigation bars and lists?', 'screen', '',
    'Murdock, B. B. (1962). The serial position effect of free recall. Journal of Experimental Psychology, 64(5), 482–488.', M, 'Long-term memory')
add('law.zeigarnik', 'Zeigarnik effect', 'B. Zeigarnik', 1927,
    'People remember uncompleted or interrupted tasks better than completed ones.',
    'Progress indicators and incomplete-profile prompts motivate completion; ethically, do not weaponize open loops (endless badges, artificial incompleteness).',
    'Do multi-step tasks show progress and remaining steps, and is "unfinished" status used honestly?', 'flow', '',
    'Zeigarnik, B. (1927). Das Behalten erledigter und unerledigter Handlungen. Psychologische Forschung, 9, 1–85.', M, 'Motivation & memory')
add('law.ovsiankina', 'Ovsiankina effect', 'M. Ovsiankina', 1928,
    'People feel a tendency to resume an interrupted task.',
    'Let users save progress and resume where they left off; show a clear "continue where you left off" entry point.',
    'Can users leave a long task and resume it later without losing work, and is the resume path obvious?', 'flow', '',
    'Ovsiankina, M. (1928). Die Wiederaufnahme unterbrochener Handlungen. Psychologische Forschung, 11, 302–379.', M, 'Motivation & memory')
add('law.forgetting-curve', 'Forgetting curve & spacing effect', 'H. Ebbinghaus', 1885,
    'Memory for new information decays rapidly without reinforcement; spaced repetition slows forgetting.',
    'Do not assume users remember onboarding tips or settings explained once; surface guidance contextually at the moment of need.',
    'Is guidance available in context when needed, rather than only in a one-time onboarding tour?', 'flow', '',
    'Ebbinghaus, H. (1885). Über das Gedächtnis. Precursor to the 1900–present period.', M, 'Long-term memory', sev='minor')
add('law.mental-models', 'Mental models', 'K. Craik; P. Johnson-Laird; D. Norman', '1943/1983',
    'People form internal, simplified models of how a system works and use them to predict behavior; mismatches between the user’s model and the system’s model cause errors.',
    'Match the system image to users’ existing models (real-world metaphors, conventions); reveal how things work through feedback and clear structure.',
    'Does the interface behave the way a first-time user would predict? Where it does not, is the actual behavior explained?', 'flow', '',
    'Craik, K. (1943). The Nature of Explanation; Norman, D. A. (1983). Some observations on mental models. In Gentner & Stevens (Eds.), Mental Models.', M, 'Mental models')
add('law.information-foraging', 'Information foraging theory & information scent', 'P. Pirolli & S. Card', 1999,
    'People seeking information behave like animals foraging for food: they follow cues (information scent) and leave a patch when the expected gain drops below the cost of moving on.',
    'Links, labels and navigation must carry strong scent: specific, predictable words that tell users what they will find. Weak scent (vague labels like "Solutions", "Learn more") causes pogo-sticking and abandonment.',
    'Do navigation labels and link texts clearly predict the content behind them? Would a user know which link to choose for their goal?', 'screen', '',
    'Pirolli, P. & Card, S. (1999). Information foraging. Psychological Review, 106(4), 643–675.', M, 'Information seeking')
add('law.satisficing', 'Satisficing', 'H. A. Simon', 1956,
    'People choose the first option that seems good enough rather than searching for the optimal one.',
    'Users click the first plausible link instead of reading all options (Krug 2000); make the right choice the most obviously plausible one.',
    'Would a user scanning quickly pick the correct option first, or is a plausible-but-wrong option more prominent?', 'screen', '',
    'Simon, H. A. (1956). Rational choice and the structure of the environment. Psychological Review, 63(2), 129–138.', D, 'Bounded rationality')
add('law.generation-effect', 'Generation effect', 'N. Slamecka & P. Graf', 1978,
    'Information people generate themselves is remembered better than information they only read.',
    'For learning products, let users actively produce answers; for task tools, do not make users generate information the system already knows.',
    'Does the product ask users to produce information it could pre-fill (bad), or ask learners to recall information to reinforce it (good, in learning contexts)?', 'flow', '',
    'Slamecka, N. J. & Graf, P. (1978). The generation effect. JEP: Human Learning and Memory, 4(6), 592–604.', M, 'Long-term memory', sev='minor')

# ---------------- Motor control & input ----------------
add('law.fitts', "Fitts's law", 'P. M. Fitts', 1954,
    'The time to move to a target is a function of the distance to and the size of the target: MT = a + b·log2(2D/W) (Shannon formulation: MT = a + b·log2(D/W + 1)).',
    'Make frequent and important targets large and close to where the pointer or thumb already is; use screen edges and corners (effectively infinite targets on desktop); keep destructive actions away from common ones.',
    'Are primary actions large and close to the user’s current focus? Are small targets avoided for frequent actions? Are destructive actions not adjacent to frequent actions?', 'deterministic (target size) + screen',
    'MT = a + b·log2(D/W + 1); see also WCAG 2.5.8 (24×24 CSS px min) and 2.5.5 (44×44).',
    'Fitts, P. M. (1954). The information capacity of the human motor system in controlling the amplitude of movement. JEP, 47(6), 381–391; MacKenzie, I. S. (1992). Fitts\' law as a research and design tool in HCI. HCI, 7(1), 91–139.', MO, 'Pointing')
add('law.hick-hyman', 'Hick–Hyman law', 'W. E. Hick; R. Hyman', '1952/1953',
    'Decision time increases logarithmically with the number and (equally likely) complexity of choices: RT = a + b·log2(n + 1).',
    'Reduce the number of simultaneous choices for time-critical or novice decisions; highlight recommended options; break complex choices into steps. Does not apply well to searching unfamiliar lists, which is linear.',
    'At key decision points (pricing, onboarding, main navigation), is the number of options minimized and is a recommended choice indicated?', 'screen', 'RT = a + b·log2(n+1)',
    'Hick, W. E. (1952). On the rate of gain of information. QJEP, 4(1), 11–26; Hyman, R. (1953). Stimulus information as a determinant of reaction time. JEP, 45(3), 188–196.', D, 'Choice')
add('law.steering', 'Steering law', 'J. Accot & S. Zhai', 1997,
    'The time to move a pointer through a tunnel (such as a cascading menu path) is proportional to the tunnel’s length divided by its width.',
    'Long, narrow hover paths (nested flyout menus) are slow and error-prone; widen paths, add hover-intent delays/triangles, or avoid deep cascades.',
    'Do nested menus require the user to steer through narrow paths without closing accidentally?', 'flow', 'T = a + b·(A/W) for straight tunnels',
    'Accot, J. & Zhai, S. (1997). Beyond Fitts\' law: Models for trajectory-based HCI tasks. CHI \'97, 295–302.', MO, 'Pointing')
add('law.klm', 'Keystroke-Level Model (KLM)', 'S. Card, T. Moran & A. Newell', 1980,
    'Expert, error-free task time can be predicted by summing standard operator times: K (keystroke), P (point), B (button press), H (home hands), M (mental preparation), R (system response).',
    'Use KLM to compare design alternatives for efficiency (e.g., number of field switches, pointing vs keyboard).',
    'For frequent expert tasks, has the number of operators (clicks, field switches, mental decisions) been minimized?', 'flow',
    'K ≈ 0.2 s (avg skilled typist; 0.08–1.2 s range), P ≈ 1.1 s, B ≈ 0.1 s, H ≈ 0.4 s, M ≈ 1.35 s.',
    'Card, S. K., Moran, T. P., & Newell, A. (1980). The keystroke-level model for user performance time with interactive systems. CACM, 23(7), 396–410.', MO, 'Performance modelling')
add('law.mhp', 'Model Human Processor', 'S. Card, T. Moran & A. Newell', 1983,
    'Human information processing can be approximated as perceptual, cognitive and motor processors with characteristic cycle times and memories with characteristic capacities and decay.',
    'Explains why ~100 ms feels instantaneous and gives engineering estimates for reaction times.',
    'Are interface reactions within perceptual "instantaneous" range (~100 ms) for direct manipulation?', 'deterministic (timing)',
    'Perceptual ≈ 100 ms [50–200], cognitive ≈ 70 ms [25–170], motor ≈ 70 ms [30–100].',
    'Card, S. K., Moran, T. P., & Newell, A. (1983). The Psychology of Human-Computer Interaction. Lawrence Erlbaum.', MO, 'Performance modelling')
add('law.goms', 'GOMS (Goals, Operators, Methods, Selection rules)', 'S. Card, T. Moran & A. Newell', 1983,
    'Skilled behavior can be described as goals achieved through methods composed of operators, with selection rules for choosing methods.',
    'Useful for analyzing and predicting expert efficiency and learning time of procedural interfaces.',
    'For expert workflows, are there efficient methods (shortcuts, bulk actions) and are selection rules simple?', 'flow', '',
    'Card, Moran & Newell (1983); John, B. E. & Kieras, D. E. (1996). The GOMS family of user interface analysis techniques. ACM TOCHI, 3(4), 320–351.', MO, 'Performance modelling', sev='minor')
add('law.thumb-zone', 'Thumb zone / one-handed mobile use', 'S. Hoober', 2013,
    'Observation of 1,333 people using phones found about 49% held the phone in one hand with thumb input; reach is easiest in the lower-middle area of the screen and hardest at the top corners.',
    'Place frequent mobile actions within easy thumb reach (bottom area); avoid placing primary actions only in top corners on tall phones.',
    'On mobile, are frequent and primary actions reachable in the bottom/middle area of the screen?', 'screen', '~49% one-handed, 36% cradled, 15% two-handed (Hoober 2013).',
    'Hoober, S. (2013). How Do Users Really Hold Mobile Devices? UXmatters.', MO, 'Touch', conf='high')
add('law.touch-target-research', 'Finger and touch target size research', 'Parhi, Karlson & Bederson; MIT Touch Lab', '2003/2006',
    'Average adult finger pads are about 10–14 mm wide and fingertips 8–10 mm; one-handed thumb tapping error rates drop substantially for targets of about 9.2–9.6 mm and larger.',
    'Make touch targets at least ~9 mm (≈ 44–48 px/pt/dp) with spacing between adjacent targets.',
    'Are touch targets at least 44×44 pt (iOS) / 48×48 dp (Android) or have equivalent spacing?', 'deterministic',
    '≥ 9.6 mm (Parhi et al. 2006); 44 pt Apple HIG; 48 dp Material; WCAG 2.5.8 ≥ 24 CSS px; WCAG 2.5.5 ≥ 44 CSS px.',
    'Parhi, P., Karlson, A. K., & Bederson, B. B. (2006). Target size study for one-handed thumb use on small touchscreen devices. MobileHCI \'06, 203–210; Dandekar, K., Raju, B., & Srinivasan, M. (2003). 3-D finite-element models of human and monkey fingertips. J. Biomech. Eng.', MO, 'Touch')

# ---------------- Time & performance ----------------
add('law.response-time-limits', 'Response time limits (0.1 s / 1 s / 10 s)', 'R. B. Miller; S. Card et al.; J. Nielsen', '1968/1991/1993',
    'About 0.1 s feels instantaneous; about 1 s keeps the user’s flow of thought uninterrupted though the delay is noticed; about 10 s is the limit for keeping attention on the dialogue.',
    'Give immediate feedback within 0.1 s for direct manipulation; show progress indicators for anything over ~1 s; show percent-done progress and allow cancel for anything over ~10 s.',
    'Does every action give visible feedback within 100 ms? Are operations over 1 s accompanied by a loading indicator and over 10 s by a progress bar with cancel?', 'deterministic (timing) + flow',
    '0.1 s instantaneous; 1 s flow; 10 s attention.',
    'Miller, R. B. (1968). Response time in man-computer conversational transactions. AFIPS Fall Joint Computer Conference, 267–277; Card, S. K., Robertson, G. G., & Mackinlay, J. D. (1991). The information visualizer. CHI \'91; Nielsen, J. (1993). Usability Engineering, ch. 5.', T, 'Latency')
add('law.doherty', 'Doherty threshold', 'W. J. Doherty & A. J. Thadani', 1982,
    'Productivity rises sharply when system response time drops below about 400 ms, because users and computer interact at a pace where neither waits on the other.',
    'Aim for interaction responses under 400 ms; use optimistic UI, skeletons and perceived-performance techniques when real work takes longer.',
    'Do routine interactions complete (or appear to complete) in under 400 ms?', 'deterministic (timing)', '< 400 ms',
    'Doherty, W. J. & Thadani, A. J. (1982). The Economic Value of Rapid Response Time. IBM technical report GE20-0752-0.', T, 'Latency')
add('law.rail', 'RAIL performance model', 'Google Chrome team', 2015,
    'Response: process user input within 50 ms so visible response occurs within 100 ms; Animation: produce a frame in 10 ms (16 ms budget for 60 fps); Idle: work in ≤ 50 ms chunks; Load: deliver content and become interactive within ~5 s on mid-range mobile on slow networks (and subsequent loads within 2 s).',
    'Gives engineering budgets aligned to perception limits.',
    'Do interactions respond within 100 ms and animations run at 60 fps without jank?', 'deterministic (timing)', '100 ms response, 16 ms/frame, 50 ms idle chunks, ≤ 5 s load',
    'Google (2015). Measure performance with the RAIL model. web.dev.', T, 'Latency')
add('law.labor-illusion', 'Labor illusion', 'R. Buell & M. Norton', 2011,
    'People value a service more, and tolerate waiting better, when the system visibly shows the work being done on their behalf.',
    'For unavoidable waits (search, quotes, AI generation), show meaningful progress steps. Do not add fake delays to manipulate perception.',
    'During long operations, does the UI show what is being done (meaningful steps) rather than a blank spinner?', 'flow', '',
    'Buell, R. W. & Norton, M. I. (2011). The labor illusion: How operational transparency increases perceived value. Management Science, 57(9), 1564–1579.', T, 'Waiting', sev='minor')
add('law.waiting-psychology', 'Psychology of waiting lines', 'D. Maister', 1985,
    'Occupied time feels shorter than unoccupied time; uncertain and unexplained waits feel longer; anxious waits feel longer; unfair waits feel longer.',
    'Tell users how long they will wait and why; keep them occupied with useful content; show queue position.',
    'Do waits show an estimated duration or position, and an explanation?', 'flow', '',
    'Maister, D. H. (1985). The psychology of waiting lines. In Czepiel, Solomon & Surprenant (Eds.), The Service Encounter.', T, 'Waiting', sev='minor')
add('law.progress-bar-perception', 'Progress bar perception', 'C. Harrison, B. Amento, S. Kuznetsov & R. Bell', 2007,
    'Progress bars that accelerate toward the end, or show backward-moving ribbing, are perceived as faster than linear ones, even when total duration is the same.',
    'Avoid progress bars that stall near 100%; front-load uncertainty.',
    'Do progress indicators avoid stalling near completion?', 'flow', '',
    'Harrison, C. et al. (2007). Rethinking the progress bar. UIST \'07, 115–118.', T, 'Waiting', sev='minor')

# ---------------- Decision-making & behavior ----------------
add('law.choice-overload', 'Choice overload', 'S. Iyengar & M. Lepper', 2000,
    'Offering too many options can reduce the likelihood of choosing at all and lower satisfaction with the choice (24 vs 6 jam varieties study). Effect size varies by context (Scheibehenne et al. 2010 meta-analysis found mean effect near zero but with moderators).',
    'Curate options, provide defaults and recommendations, and offer filtering for large catalogs.',
    'Where users must choose (plans, products, settings), are options limited, compared clearly, and is a recommended option highlighted?', 'screen', '',
    'Iyengar, S. S. & Lepper, M. R. (2000). When choice is demotivating. JPSP, 79(6), 995–1006; Scheibehenne, B., Greifeneder, R., & Todd, P. M. (2010). Can there ever be too many options? JCR, 37(3), 409–425.', D, 'Choice')
add('law.prospect-theory', 'Prospect theory & loss aversion', 'D. Kahneman & A. Tversky', 1979,
    'People evaluate outcomes as gains or losses relative to a reference point, and losses loom larger than equivalent gains (roughly 2×).',
    'Framing in terms of what users would lose can motivate, but becomes manipulative when used to pressure (e.g., confirmshaming). Use honestly.',
    'Is loss framing used honestly and without pressure tactics?', 'screen', 'Loss aversion coefficient λ ≈ 2.25 (Tversky & Kahneman 1992).',
    'Kahneman, D. & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263–291.', D, 'Behavioral economics')
add('law.framing', 'Framing effect', 'A. Tversky & D. Kahneman', 1981,
    'Logically equivalent choices presented differently (e.g., "90% survive" vs "10% die") lead to different decisions.',
    'Wording of consent, pricing and risk information shapes decisions; present information neutrally where users make consequential choices.',
    'Are consequential choices (consent, cancellations, risk) framed neutrally and clearly?', 'screen', '',
    'Tversky, A. & Kahneman, D. (1981). The framing of decisions and the psychology of choice. Science, 211(4481), 453–458.', D, 'Behavioral economics')
add('law.anchoring', 'Anchoring', 'A. Tversky & D. Kahneman', 1974,
    'People rely heavily on the first piece of information offered (the anchor) when making judgments.',
    'The first price, number or option shown sets expectations; showing a fake "was" price is deceptive.',
    'Are reference prices and anchors genuine (not fabricated "was" prices)?', 'screen', '',
    'Tversky, A. & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124–1131.', D, 'Behavioral economics')
add('law.default-effect', 'Default effect', 'E. Johnson & D. Goldstein', 2003,
    'People disproportionately stick with pre-selected defaults (organ donor consent rates differed hugely between opt-in and opt-out countries).',
    'Set defaults that serve the user’s interest; never pre-select paid add-ons, marketing consent or data sharing (also prohibited under GDPR for consent).',
    'Are all defaults in the user’s interest? Are paid extras, marketing and data-sharing options unchecked by default?', 'deterministic (pre-checked boxes) + screen', '',
    'Johnson, E. J. & Goldstein, D. (2003). Do defaults save lives? Science, 302(5649), 1338–1339.', D, 'Behavioral economics')
add('law.decoy', 'Decoy effect (asymmetric dominance)', 'J. Huber, J. Payne & C. Puto', 1982,
    'Adding a third, clearly inferior option shifts preference toward the option that dominates it.',
    'Common in pricing tables; ethical when it clarifies value, manipulative when the decoy exists only to steer.',
    'Does each pricing option exist for a genuine user segment, rather than only to steer choice?', 'screen', '',
    'Huber, J., Payne, J. W., & Puto, C. (1982). Adding asymmetrically dominated alternatives. JCR, 9(1), 90–98.', D, 'Behavioral economics', sev='minor')
add('law.goal-gradient', 'Goal-gradient effect', 'C. Hull; R. Kivetz, O. Urminsky & Y. Zheng', '1932/2006',
    'Motivation and effort increase as people get closer to a goal.',
    'Show progress and remaining steps; give a head start (endowed progress) where honest.',
    'Do multi-step flows show progress toward completion?', 'flow', '',
    'Hull, C. L. (1932). The goal-gradient hypothesis and maze learning. Psychological Review, 39(1), 25–43; Kivetz, R., Urminsky, O., & Zheng, Y. (2006). The goal-gradient hypothesis resurrected. JMR, 43(1), 39–58.', D, 'Motivation')
add('law.endowed-progress', 'Endowed progress effect', 'J. Nunes & X. Drèze', 2006,
    'People given artificial advancement toward a goal (e.g., a loyalty card with 2 of 10 stamps already filled) are more likely to complete it.',
    'Starting progress bars from a non-zero state for already-completed steps (account created, email confirmed) increases completion.',
    'Do onboarding checklists reflect steps the user has already completed?', 'flow', '',
    'Nunes, J. C. & Drèze, X. (2006). The endowed progress effect. JCR, 32(4), 504–512.', D, 'Motivation', sev='minor')
add('law.peak-end', 'Peak–end rule', 'D. Kahneman, B. Fredrickson, C. Schreiber & D. Redelmeier', 1993,
    'People judge an experience largely by how it felt at its most intense point and at its end, rather than by the average.',
    'Design the emotional peaks (moments of success) and endings (confirmation pages, cancellation, offboarding) with care; a painful final step colors the whole experience.',
    'Are the final steps of key journeys (confirmation, cancellation, errors at the end) positive, clear and reassuring?', 'flow', '',
    'Kahneman, D., Fredrickson, B. L., Schreiber, C. A., & Redelmeier, D. A. (1993). When more pain is preferred to less: Adding a better end. Psychological Science, 4(6), 401–405.', EM, 'Experience memory')
add('law.yerkes-dodson', 'Yerkes–Dodson law', 'R. Yerkes & J. Dodson', 1908,
    'Performance increases with arousal up to an optimal point, then decreases; the optimum is lower for complex tasks.',
    'Avoid adding stress (timers, alarming colors, urgency messaging) to complex tasks like forms, payments or medical decisions.',
    'Are complex tasks free of artificial pressure (countdown timers, alarming language)?', 'screen', '',
    'Yerkes, R. M. & Dodson, J. D. (1908). The relation of strength of stimulus to rapidity of habit-formation. J. Comparative Neurology and Psychology, 18(5), 459–482.', D, 'Stress')
add('law.fogg-bm', 'Fogg Behavior Model (B = MAP)', 'B. J. Fogg', 2009,
    'A behavior happens when Motivation, Ability and a Prompt converge at the same moment; if a behavior does not happen, at least one is missing.',
    'Increase ability (make it simpler) before trying to increase motivation; prompt at the moment when motivation and ability are present.',
    'For the key conversion behavior, is the action simple enough (ability) and is there a clear prompt at the right moment?', 'flow', '',
    'Fogg, B. J. (2009). A behavior model for persuasive design. Persuasive \'09, Article 40.', D, 'Persuasion')
add('law.tam', 'Technology Acceptance Model', 'F. Davis', 1989,
    'Intention to use a technology is driven mainly by perceived usefulness and perceived ease of use.',
    'Adoption requires demonstrating usefulness early (value before effort) as well as reducing friction.',
    'Does the product communicate its usefulness before asking for effort (signup, setup)?', 'flow', '',
    'Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319–340.', D, 'Adoption')
add('law.utaut', 'Unified Theory of Acceptance and Use of Technology (UTAUT)', 'V. Venkatesh, M. Morris, G. Davis & F. Davis', 2003,
    'Use intention is predicted by performance expectancy, effort expectancy, social influence and facilitating conditions, moderated by gender, age, experience and voluntariness.',
    'Adoption also depends on social proof and on support/infrastructure, not only on the interface.',
    'Are support resources and social proof available for new users?', 'organizational / research', '',
    'Venkatesh, V. et al. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425–478.', D, 'Adoption', sev='minor')
add('law.diffusion', 'Diffusion of innovations', 'E. Rogers', 1962,
    'Adoption spreads through innovators, early adopters, early majority, late majority and laggards; relative advantage, compatibility, complexity, trialability and observability drive adoption speed.',
    'Trialability (free trials, demo modes) and observability (visible results) speed adoption; complexity slows it.',
    'Can users try the product before committing, and see results quickly?', 'flow', '',
    'Rogers, E. M. (1962). Diffusion of Innovations. Free Press.', D, 'Adoption', sev='minor')
add('law.sdt', 'Self-determination theory', 'E. Deci & R. Ryan', 1985,
    'Intrinsic motivation and well-being depend on satisfying three needs: autonomy, competence and relatedness.',
    'Give users meaningful control and choices, help them feel competent (clear feedback, appropriate challenge), and support connection where relevant.',
    'Does the product give users control, build their sense of competence, and avoid controlling or coercive patterns?', 'flow', '',
    'Deci, E. L. & Ryan, R. M. (1985). Intrinsic Motivation and Self-Determination in Human Behavior. Plenum.', D, 'Motivation')
add('law.flow', 'Flow', 'M. Csikszentmihalyi', '1975/1990',
    'Optimal experience occurs when challenge matches skill, goals are clear, and feedback is immediate; too much challenge causes anxiety, too little causes boredom.',
    'Remove interruptions during focused work, give immediate feedback, and match difficulty to skill (progressive complexity).',
    'During focused tasks, are interruptions (modals, prompts, notifications) avoided?', 'flow', '',
    'Csikszentmihalyi, M. (1990). Flow: The Psychology of Optimal Experience. Harper & Row.', EM, 'Engagement')
add('law.dual-process', 'Dual-process theory (System 1 / System 2)', 'K. Stanovich & R. West; D. Kahneman', '2000/2011',
    'Thinking runs on a fast, automatic, intuitive system and a slow, effortful, deliberate system; most interface use relies on the fast system.',
    'Design for fast intuitive use (conventions, clear signifiers) and deliberately slow users down only where consequences are serious (confirmation of irreversible actions).',
    'Are routine tasks executable on autopilot, and are high-stakes, irreversible actions deliberately slowed (review step, explicit confirmation)?', 'flow', '',
    'Stanovich, K. E. & West, R. F. (2000). Individual differences in reasoning. BBS, 23(5), 645–665; Kahneman, D. (2011). Thinking, Fast and Slow.', D, 'Cognition')
add('law.cialdini', "Cialdini's principles of influence", 'R. Cialdini', '1984/2016',
    'Reciprocity, commitment & consistency, social proof, authority, liking, scarcity, and (2016) unity drive compliance.',
    'These levers are powerful and must be used truthfully: fake scarcity, fake social proof and fake authority are deceptive patterns and may be illegal.',
    'Are scarcity, social proof, and authority claims truthful and verifiable?', 'screen', '',
    'Cialdini, R. B. (1984). Influence: The Psychology of Persuasion; Cialdini (2016). Pre-Suasion.', D, 'Persuasion')
add('law.nudge', 'Nudge / choice architecture', 'R. Thaler & C. Sunstein', 2008,
    'How choices are presented (defaults, ordering, framing, salience) predictably influences decisions without restricting options; nudges should be transparent and easy to opt out of.',
    'Use choice architecture to help users act in their own interest (e.g., saving), and avoid "sludge" that makes beneficial actions harder.',
    'Does the choice architecture help users act in their own interest, with easy opt-out? Is there sludge making beneficial actions (cancel, opt-out, claim) harder than harmful ones?', 'flow', '',
    'Thaler, R. H. & Sunstein, C. R. (2008). Nudge. Yale University Press; Sunstein, C. (2020). Sludge audits. Behavioural Public Policy.', D, 'Choice architecture')
add('law.east', 'EAST framework', 'Behavioural Insights Team', 2014,
    'To encourage a behavior, make it Easy, Attractive, Social and Timely.',
    'Practical checklist for designing interventions in services.',
    'Is the desired behavior easy (defaults, fewer steps), attractive (salient, rewarding), social (norms), and timely (prompted at the right moment)?', 'flow', '',
    'Behavioural Insights Team (2014). EAST: Four simple ways to apply behavioural insights.', D, 'Choice architecture', sev='minor')
add('law.com-b', 'COM-B model / Behaviour Change Wheel', 'S. Michie, M. van Stralen & R. West', 2011,
    'Behavior results from Capability, Opportunity and Motivation interacting.',
    'Diagnose why users do not perform a behavior before designing interventions.',
    'Has the team diagnosed whether non-completion is due to capability, opportunity or motivation?', 'organizational / research', '',
    'Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel. Implementation Science, 6, 42.', D, 'Behavior change', sev='minor')
add('law.hooked', 'Hook model', 'N. Eyal', 2014,
    'Habit-forming products cycle users through trigger → action → variable reward → investment.',
    'Understand it to recognize compulsive loops; variable rewards and infinite feeds can harm well-being. Audit for manipulative engagement loops.',
    'Do engagement loops serve the user’s goals, and can users easily stop (no infinite autoplay without control, clear stopping cues)?', 'flow', '',
    'Eyal, N. (2014). Hooked: How to Build Habit-Forming Products.', D, 'Engagement', conf='high')
add('law.ikea', 'IKEA effect', 'M. Norton, D. Mochon & D. Ariely', 2012,
    'People place disproportionately high value on things they partially created themselves.',
    'Light customization and setup investment can increase attachment; but required effort should not become a lock-in tactic.',
    'Is user investment (customization, content) portable and not used as lock-in?', 'flow', '',
    'Norton, M. I., Mochon, D., & Ariely, D. (2012). The IKEA effect: When labor leads to love. JCP, 22(3), 453–460.', D, 'Behavioral economics', sev='minor')
add('law.mere-exposure', 'Mere-exposure effect', 'R. Zajonc', 1968,
    'People develop a preference for things merely because they are familiar with them.',
    'Familiar conventions feel better and are trusted more; radical redesigns often meet initial resistance regardless of quality.',
    'Does the interface use familiar conventions where possible?', 'screen', '',
    'Zajonc, R. B. (1968). Attitudinal effects of mere exposure. JPSP, 9(2, Pt.2), 1–27.', D, 'Familiarity', sev='minor')
add('law.jakob', "Jakob's law", 'J. Nielsen', 2000,
    'Users spend most of their time on other sites, so they prefer your site to work the same way as all the other sites they already know.',
    'Follow established conventions for navigation, forms, carts, search and controls; innovate where it adds real value.',
    'Does the interface follow platform and industry conventions (logo top-left links home, cart top-right, standard form controls)?', 'screen', '',
    'Nielsen, J. (2000). End of Web Design. Alertbox, July 23, 2000.', S, 'Conventions')
add('law.tesler', "Tesler's law (law of conservation of complexity)", 'L. Tesler', '1980s',
    'Every application has an inherent amount of complexity that cannot be removed; it can only be shifted between the system and the user.',
    'The system (and its designers/developers) should absorb complexity rather than pushing it onto users (e.g., auto-detect card type, parse addresses, infer time zones).',
    'Is complexity that the system could handle (formatting, inference, defaults) being pushed onto the user?', 'flow', '',
    'Saffer, D. (2009). Designing for Interaction (interview with Larry Tesler); originally articulated at Xerox PARC in the mid-1980s.', S, 'Complexity', conf='medium')
add('law.postel', "Postel's law (robustness principle)", 'J. Postel', 1980,
    'Be conservative in what you do, be liberal in what you accept from others.',
    'Accept user input in many formats (spaces in phone numbers, dashes in card numbers, varied date formats) and normalize it; output consistent, clean formats.',
    'Do form fields accept common variations (spaces, dashes, capitalization, leading/trailing whitespace) instead of rejecting them?', 'deterministic (input testing) + flow', '',
    'Postel, J. (1980). RFC 760: DoD Standard Internet Protocol; restated in RFC 793 (1981).', S, 'Input tolerance')
add('law.occam', "Occam's razor", 'William of Ockham', '14th century',
    'Among competing hypotheses or solutions that work equally well, the one with the fewest assumptions or elements should be selected.',
    'Remove any element that does not contribute to the user’s goal.',
    'Can any element be removed without hurting the user’s ability to complete their task?', 'screen', '', 'Principle predating the period; widely applied in design.', S, 'Simplicity', sev='minor')
add('law.pareto', 'Pareto principle (80/20 rule)', 'V. Pareto; J. Juran', '1896/1941',
    'Roughly 80% of effects come from 20% of causes.',
    'A small subset of features and tasks accounts for most use; optimize the top tasks first and avoid letting rare tasks clutter the main interface.',
    'Are the most frequent tasks the most prominent and efficient?', 'screen', '', 'Juran, J. M. (1951). Quality Control Handbook (popularized "vital few").', S, 'Prioritization')
add('law.parkinson', "Parkinson's law", 'C. N. Parkinson', 1955,
    'Work expands to fill the time available for its completion.',
    'Short, well-defined tasks (with sensible estimates of time required) feel achievable; autofill and defaults reduce time-to-complete.',
    'Do forms and tasks indicate expected time and avoid unnecessary steps?', 'flow', '',
    'Parkinson, C. N. (1955). Parkinson\'s law. The Economist, November 19, 1955.', S, 'Time', sev='minor')
add('law.conway', "Conway's law", 'M. Conway', 1968,
    'Organizations design systems that mirror their own communication structures.',
    'Navigation and products often reflect org charts rather than user tasks; audit IA for organization-centric labels and silos.',
    'Is the navigation organized around user tasks rather than internal departments or product teams?', 'screen', '',
    'Conway, M. E. (1968). How do committees invent? Datamation, 14(4), 28–31.', S, 'Organization')
add('law.goodhart', "Goodhart's law", 'C. Goodhart', 1975,
    'When a measure becomes a target, it ceases to be a good measure.',
    'Optimizing a single UX metric (time on site, clicks, NPS) leads to gaming and worse experiences; use balanced metrics (e.g., HEART) and qualitative evidence.',
    'Are success metrics balanced so that optimizing one does not harm users (e.g., engagement vs. task success)?', 'organizational / research', '',
    'Goodhart, C. (1975). Problems of monetary management: The U.K. experience; Strathern, M. (1997) phrasing.', ME, 'Metrics', sev='minor')
add('law.murphy', "Murphy's law", 'E. A. Murphy Jr.', 1949,
    'Anything that can go wrong will go wrong.',
    'Design every flow for error states, edge cases, empty states, offline states and misuse.',
    'Have error, empty, loading, offline and edge-case states been designed for every key screen?', 'flow', '', 'Attributed to Edward A. Murphy Jr., Edwards Air Force Base (1949).', E, 'Error')
add('law.kiss', 'KISS (keep it simple)', 'Attributed to K. Johnson', '1960s',
    'Most systems work best if they are kept simple rather than made complicated.',
    'Simplicity should be a design goal; unnecessary complexity should be avoided.',
    'Is the solution the simplest one that meets user needs?', 'screen', '', 'Attributed to Kelly Johnson, Lockheed Skunk Works (c. 1960).', S, 'Simplicity', sev='minor', conf='medium')
add('law.least-astonishment', 'Principle of least astonishment (POLA)', 'Programming & UI design folklore', '1970s',
    'A component of a system should behave in the way most users expect it to behave; it should not astonish or surprise users.',
    'If a design surprises users, change the design, not the users.',
    'Does any control behave differently from what its appearance and label suggest?', 'flow', '', 'Commonly cited in PL/I and UI literature from the early 1970s (e.g., James, 1987, The Tao of Programming).', S, 'Predictability', conf='medium')
add('law.aesthetic-usability', 'Aesthetic–usability effect', 'M. Kurosu & K. Kashimura; N. Tractinsky', '1995/1997',
    'Users perceive more aesthetically pleasing designs as easier to use, and are more tolerant of minor usability issues in them.',
    'Visual polish improves perceived usability and trust, but can mask real usability problems in testing; measure task performance, not just opinions.',
    'Is visual quality consistent and professional? In testing, are performance metrics used alongside satisfaction ratings?', 'screen', '',
    'Kurosu, M. & Kashimura, K. (1995). Apparent usability vs. inherent usability. CHI \'95 Conference Companion, 292–293; Tractinsky, N. (1997). Aesthetics and apparent usability. CHI \'97.', EM, 'Aesthetics')
add('law.what-is-beautiful-is-usable', 'What is beautiful is usable', 'N. Tractinsky, A. Katz & D. Ikar', 2000,
    'Perceived aesthetics of an interface correlated strongly with perceived usability both before and after use, even when actual usability was manipulated.',
    'First impressions of visual design shape credibility and willingness to continue.',
    'Does the first view look credible and well-crafted?', 'screen', '',
    'Tractinsky, N., Katz, A. S., & Ikar, D. (2000). What is beautiful is usable. Interacting with Computers, 13(2), 127–145.', EM, 'Aesthetics')
add('law.first-impressions-50ms', 'First impressions in 50 milliseconds', 'G. Lindgaard, G. Fernandes, C. Dudek & J. Brown', 2006,
    'People form stable judgments of a web page’s visual appeal within about 50 ms of exposure.',
    'Above-the-fold visual quality and clarity heavily influence whether users stay.',
    'Does the initial viewport communicate quality and purpose at a glance?', 'screen', '≈ 50 ms',
    'Lindgaard, G. et al. (2006). Attention web designers: You have 50 milliseconds to make a good first impression! BIT, 25(2), 115–126.', EM, 'Aesthetics')
add('law.visual-complexity', 'Visual complexity and prototypicality', 'K. Reinecke et al.; A. Tuch et al.', '2012/2013',
    'Websites with low visual complexity and high prototypicality (looking like a typical site of their category) are judged most appealing in first impressions.',
    'Keep visual complexity low and follow category conventions for landing pages.',
    'Is the visual complexity of key pages low, and does the page look like a typical member of its category?', 'screen', '',
    'Tuch, A. N. et al. (2012). The role of visual complexity and prototypicality regarding first impression of websites. IJHCS, 70(11), 794–811; Reinecke, K. et al. (2013). Predicting users\' first impressions of website aesthetics. CHI \'13.', EM, 'Aesthetics')
add('law.uncanny-valley', 'Uncanny valley', 'M. Mori', 1970,
    'As an artificial character becomes more human-like, affinity rises until a point where near-human but imperfect likeness causes discomfort.',
    'Avatars, voice assistants and AI agents that try too hard to appear human can feel unsettling; be clear that the system is a machine.',
    'Does the AI or avatar clearly present itself as a system rather than imperfectly imitating a human?', 'screen', '',
    'Mori, M. (1970). Bukimi no tani (The uncanny valley). Energy, 7(4), 33–35.', EM, 'Anthropomorphism', sev='minor')
add('law.emotional-design', 'Three levels of emotional design', 'D. Norman', 2004,
    'Products affect people at visceral (appearance), behavioral (use and performance) and reflective (meaning, self-image) levels.',
    'Address all three: look appealing, work well, and support the user’s identity and values.',
    'Does the product work well (behavioral) as well as look good (visceral) and fit users’ values (reflective)?', 'screen', '',
    'Norman, D. A. (2004). Emotional Design. Basic Books.', EM, 'Emotion')
add('law.ux-hierarchy', 'Hierarchy of user needs', 'A. Walter (after A. Maslow)', '2011 (Maslow 1943)',
    'Design must first be functional, then reliable, then usable, then pleasurable; delight is not possible if the lower levels fail.',
    'Fix functional and reliability issues before investing in delight.',
    'Are there functional bugs or reliability issues that undermine everything else?', 'flow', '',
    'Walter, A. (2011). Designing for Emotion. A Book Apart; Maslow, A. H. (1943). A theory of human motivation. Psychological Review, 50(4), 370–396.', EM, 'Emotion')
add('law.halo', 'Halo effect', 'E. L. Thorndike', 1920,
    'An overall positive impression in one area (e.g., attractiveness) colors judgments in other areas.',
    'Good visual design raises perceived credibility and quality; one glaring flaw (typos, broken images) can create a negative halo.',
    'Are there visible quality flaws (typos, broken images, misalignment) that could damage overall credibility?', 'screen', '',
    'Thorndike, E. L. (1920). A constant error in psychological ratings. Journal of Applied Psychology, 4(1), 25–29.', EM, 'Credibility')

# ---------------- Interaction models ----------------
add('model.affordances', 'Affordances', 'J. J. Gibson; D. Norman', '1977/1988',
    'An affordance is a relationship between an object’s properties and an agent’s capabilities that determines how the object could be used.',
    'Interactive elements must look interactive and non-interactive elements must not; flat designs often lose perceived affordance.',
    'Do interactive elements look clickable/tappable and do static elements avoid looking interactive?', 'screen', '',
    'Gibson, J. J. (1977). The theory of affordances. In Shaw & Bransford (Eds.), Perceiving, Acting, and Knowing; Norman, D. A. (1988). The Psychology of Everyday Things.', I, 'Norman')
add('model.signifiers', 'Signifiers', 'D. Norman', '2008/2013',
    'Signifiers are perceivable cues that communicate where and how to act (labels, underlines, arrows, shadows, cursor changes).',
    'Every action needs a visible signifier; hidden gestures and hover-only controls lack signifiers.',
    'Does every available action have a visible signifier (not only hover, gesture or long-press)?', 'screen', '',
    'Norman, D. A. (2008). Signifiers, not affordances. ACM Interactions, 15(6), 18–19; Norman (2013). The Design of Everyday Things, revised ed.', I, 'Norman')
add('model.mapping', 'Natural mapping', 'D. Norman', 1988,
    'The relationship between controls and their effects should be obvious, using spatial analogy and cultural standards.',
    'Place controls near what they control and arrange them in the same spatial layout as the things they affect.',
    'Are controls positioned near and spatially consistent with the objects they affect?', 'screen', '', 'Norman (1988). The Psychology of Everyday Things.', I, 'Norman')
add('model.constraints', 'Constraints', 'D. Norman', 1988,
    'Physical, cultural, semantic and logical constraints limit possible actions and guide users toward correct ones.',
    'Prevent invalid input with appropriate controls (date pickers, steppers, disabled impossible options with explanations).',
    'Do controls constrain input to valid values where possible?', 'screen', '', 'Norman (1988).', I, 'Norman')
add('model.feedback', 'Feedback', 'D. Norman', 1988,
    'Every action should produce immediate, informative, and proportionate feedback about its result.',
    'Acknowledge every action; tell users what happened, not just that something happened.',
    'Does every user action produce immediate, specific feedback?', 'flow', '', 'Norman (1988).', I, 'Norman')
add('model.conceptual-model', 'Conceptual model & system image', 'D. Norman', 1988,
    'The designer’s model is communicated to the user only through the system image (the interface, documentation, behavior); if the system image is unclear, users form wrong models.',
    'The interface itself must explain how it works; structure, labels and feedback build the user’s model.',
    'Could a new user describe correctly how the system is organized and what will happen when they act?', 'flow', '', 'Norman (1988).', I, 'Norman')
add('model.gulfs', 'Gulfs of execution and evaluation', 'E. Hutchins, J. Hollan & D. Norman', '1985/1986',
    'The gulf of execution is the gap between what users want to do and what the system lets them do; the gulf of evaluation is the gap between the system state and users’ ability to perceive and interpret it.',
    'Bridge execution with discoverable actions in users’ language; bridge evaluation with clear feedback and visible state.',
    'Is it obvious how to perform each key task (execution) and is it obvious whether it worked (evaluation)?', 'flow', '',
    'Hutchins, E. L., Hollan, J. D., & Norman, D. A. (1985). Direct manipulation interfaces. Human–Computer Interaction, 1(4), 311–338.', I, 'Norman')
add('model.seven-stages', 'Seven stages of action', 'D. Norman', 1986,
    'Goal → plan → specify → perform (execution); perceive → interpret → compare (evaluation).',
    'Use as a walkthrough lens: at each stage, ask what could fail.',
    'For each key task, can users form a plan, find the action, perform it, perceive the result, interpret it and know whether their goal is met?', 'flow', '',
    'Norman, D. A. (1986). Cognitive engineering. In Norman & Draper (Eds.), User Centered System Design, 31–61.', I, 'Norman')
add('model.direct-manipulation', 'Direct manipulation', 'B. Shneiderman', 1983,
    'Interfaces should offer continuous representation of objects of interest, physical actions instead of complex syntax, and rapid, incremental, reversible operations with immediately visible impact.',
    'Let users act on visible objects (drag, resize, edit in place) and see results immediately, with undo.',
    'Where appropriate, can users act directly on objects with immediate visual results and easy reversal?', 'flow', '',
    'Shneiderman, B. (1983). Direct manipulation: A step beyond programming languages. IEEE Computer, 16(8), 57–69.', I, 'Interaction styles')
add('model.progressive-disclosure', 'Progressive disclosure', 'Xerox Star team; J. Nielsen', '1981/2006',
    'Show only the most important options initially, and reveal advanced or rarely used options on request.',
    'Reduces complexity for novices while retaining power for experts; the split between basic and advanced must be right and the path to advanced features clear.',
    'Are advanced/rare options hidden behind a clear, discoverable control while common options are immediately visible?', 'screen', '',
    'Smith, D. C. et al. (1982). Designing the Star user interface. Byte, 7(4); Nielsen, J. (2006). Progressive Disclosure. NN/g.', I, 'Complexity management')
add('model.paradox-active-user', 'Paradox of the active user', 'J. Carroll & M. B. Rosson', 1987,
    'Users rarely read manuals or tutorials; they start using software immediately to get tasks done, even if learning first would make them more efficient in the long run.',
    'Design for learning-by-doing: contextual help, sensible defaults, and discoverability rather than up-front tutorials.',
    'Can a first-time user accomplish the core task without reading instructions?', 'flow', '',
    'Carroll, J. M. & Rosson, M. B. (1987). Paradox of the active user. In Carroll (Ed.), Interfacing Thought, MIT Press.', I, 'Learning')
add('model.minimalist-instruction', 'Minimalist instruction', 'J. Carroll', 1990,
    'Instructional material should let users act immediately on real tasks, minimize reading, support error recognition and recovery, and be modular.',
    'Help content should be task-oriented, brief and focused on getting users unstuck.',
    'Is help content task-oriented, short, and does it include recovery from common errors?', 'screen', '',
    'Carroll, J. M. (1990). The Nurnberg Funnel: Designing Minimalist Instruction for Practical Computer Skill. MIT Press.', I, 'Learning', sev='minor')
add('model.modes', 'Modes are a source of errors', 'L. Tesler; J. Raskin', '1981/2000',
    'A mode is a state in which the same user action has different effects; users frequently lose track of the current mode, causing mode errors.',
    'Avoid modes; if unavoidable, make the mode highly visible and use quasimodes (held keys) or spring-loaded modes.',
    'Does the same action ever produce different results depending on a hidden state? Is the current mode always clearly visible?', 'flow', '',
    'Tesler, L. (1981). The Smalltalk environment. Byte, 6(8); Raskin, J. (2000). The Humane Interface. Addison-Wesley.', E, 'Modes')
add('model.raskin-laws', "Raskin's laws of interface design", 'J. Raskin', 2000,
    'First: a computer shall not harm your work or, through inaction, allow your work to come to harm. Second: a computer shall not waste your time or require you to do more work than is strictly necessary.',
    'Autosave, undo and data preservation are baseline requirements; every unnecessary step is a defect.',
    'Is user work protected automatically (autosave, draft recovery, undo)? Are there unnecessary steps?', 'flow', '',
    'Raskin, J. (2000). The Humane Interface. Addison-Wesley.', E, 'Protect work')
add('model.locus-of-attention', 'Locus of attention & habituation', 'J. Raskin', 2000,
    'People can attend to only one thing at a time, and any frequently repeated action becomes habitual, so confirmation dialogs become ignored and clicked automatically.',
    'Prefer undo to confirmation dialogs; confirmations for routine actions are habituated away and offer little protection.',
    'Are confirmation dialogs reserved for truly irreversible, rare actions, with undo used for routine ones?', 'flow', '',
    'Raskin, J. (2000). The Humane Interface.', E, 'Errors')
add('model.wimp', 'WIMP and the desktop metaphor', 'Xerox PARC; Apple', '1973–1984',
    'Windows, icons, menus and pointer, combined with a desktop metaphor, made computing learnable through recognition and direct manipulation.',
    'Metaphors aid learning when they fit, but break down when stretched; do not let a metaphor constrain useful functionality.',
    'Do any metaphors confuse rather than help (e.g., skeuomorphic controls that behave differently than their real-world counterparts)?', 'screen', '',
    'Smith, D. C., Irby, C., Kimball, R., Verplank, B., & Harslem, E. (1982). Designing the Star user interface. Byte, 7(4), 242–282.', I, 'Interaction styles', sev='minor')
add('model.calm-technology', 'Calm technology', 'M. Weiser & J. S. Brown; A. Case', '1995/2015',
    'Technology should inform without demanding attention, moving between the periphery and the center of attention as needed.',
    'Notifications and status should be ambient and low-urgency by default, escalating only when necessary.',
    'Are notifications proportionate to importance, and can low-priority information stay peripheral?', 'flow', '',
    'Weiser, M. & Brown, J. S. (1995). Designing calm technology. Xerox PARC; Case, A. (2015). Calm Technology. O\'Reilly.', I, 'Attention economy')

# ---------------- Error & human factors ----------------
add('err.slips-mistakes', 'Slips vs. mistakes', 'D. Norman; J. Reason', '1981/1990',
    'Slips occur when the intention is correct but the action is wrong (often due to inattention); mistakes occur when the goal or plan is wrong (wrong mental model). Lapses are memory failures.',
    'Prevent slips with constraints, spacing, undo and confirmation for destructive actions; prevent mistakes with clear models, feedback and help.',
    'Are destructive actions separated from common ones and reversible? Does the interface explain consequences before users commit?', 'flow', '',
    'Norman, D. A. (1981). Categorization of action slips. Psychological Review, 88(1), 1–15; Reason, J. (1990). Human Error. Cambridge University Press.', E, 'Error')
add('err.swiss-cheese', 'Swiss cheese model of accident causation', 'J. Reason', 1990,
    'Accidents happen when holes in multiple layers of defense line up; errors are rarely a single person’s fault.',
    'Build multiple layers of protection for high-stakes tasks (constraints, confirmation, review, undo, audit trails).',
    'Do high-risk operations have layered defenses (validation, review, confirmation, undo)?', 'flow', '', 'Reason, J. (1990). Human Error.', E, 'Safety')
add('err.srk', 'Skill-, rule- and knowledge-based behavior (SRK)', 'J. Rasmussen', 1983,
    'People operate at skill-based (automatic), rule-based (if-then), or knowledge-based (problem solving) levels, and errors differ at each level.',
    'Support experts with skill-based shortcuts and novices with knowledge-level support (explanations, examples).',
    'Does the interface support both automatic expert use and problem-solving novices?', 'flow', '',
    'Rasmussen, J. (1983). Skills, rules, and knowledge. IEEE Trans. SMC, 13(3), 257–266.', E, 'Error')
add('err.poka-yoke', 'Poka-yoke (mistake-proofing)', 'S. Shingo', '1960s',
    'Design processes so mistakes are impossible or immediately detected.',
    'Use input masks, constrained controls, disabling impossible combinations, and smart defaults.',
    'Are common user errors made impossible by design rather than caught afterwards?', 'flow', '',
    'Shingo, S. (1986). Zero Quality Control: Source Inspection and the Poka-Yoke System.', E, 'Error prevention')
add('err.ironies-automation', 'Ironies of automation', 'L. Bainbridge', 1983,
    'Automating the easy parts leaves humans the hardest parts, while reducing their practice and situation awareness, so they are less able to take over when automation fails.',
    'For AI and automated features, keep users informed of what the automation is doing and make takeover smooth.',
    'When automation (including AI) acts on the user’s behalf, can the user see what it did and take over easily?', 'flow', '',
    'Bainbridge, L. (1983). Ironies of automation. Automatica, 19(6), 775–779.', E, 'Automation')
add('err.levels-automation', 'Levels of automation', 'T. Sheridan & W. Verplank; R. Parasuraman, T. Sheridan & C. Wickens', '1978/2000',
    'Automation ranges from the computer offering no assistance to fully autonomous action; it can apply separately to information acquisition, analysis, decision and action.',
    'Choose the automation level per task based on risk; high-risk decisions should keep humans in the loop with veto ability.',
    'For each automated action, is the level of autonomy appropriate to its risk, and can users veto or undo?', 'flow', '',
    'Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. IEEE Trans. SMC-A, 30(3), 286–297.', E, 'Automation')
add('err.automation-bias', 'Automation bias & complacency', 'K. Mosier & L. Skitka; R. Parasuraman & V. Riley', '1996/1997',
    'People over-rely on automated aids, failing to notice automation errors (omission) or following incorrect advice (commission).',
    'Show AI/automation confidence and sources, encourage verification for consequential outputs, and avoid presenting suggestions as facts.',
    'Do AI or automated recommendations show uncertainty and supporting evidence so users can verify them?', 'screen', '',
    'Parasuraman, R. & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. Human Factors, 39(2), 230–253.', E, 'Automation')
add('err.maba-maba', 'Fitts list (MABA-MABA)', 'P. Fitts (ed.)', 1951,
    'Allocates functions between humans and machines based on what each does better ("Men Are Better At / Machines Are Better At").',
    'Assign memory, calculation and consistency to the system and judgment, context and exceptions to people.',
    'Does the system take over tasks machines do better (remembering, calculating, checking) rather than leaving them to the user?', 'flow', '',
    'Fitts, P. M. (Ed.) (1951). Human Engineering for an Effective Air-Navigation and Traffic-Control System. National Research Council.', E, 'Function allocation')
add('err.fitts-jones', 'Pilot error as design error', 'P. Fitts & R. Jones', 1947,
    'Analysis of 460 "pilot error" incidents found that most were caused by poorly designed controls and displays (e.g., similar-looking levers), founding human factors engineering.',
    'When users make repeated errors, treat it as a design problem: differentiate controls by shape, position and labeling.',
    'Are controls with very different effects visually and spatially distinct?', 'screen', '',
    'Fitts, P. M. & Jones, R. E. (1947). Analysis of factors contributing to 460 "pilot-error" experiences in operating aircraft controls. Air Materiel Command Report TSEAA-694-12.', E, 'Human factors history')
add('err.signal-detection', 'Signal detection theory', 'W. Tanner & J. Swets; D. Green & J. Swets', '1954/1966',
    'Detecting a signal in noise depends on sensitivity and the decision criterion; reducing misses increases false alarms and vice versa.',
    'Alerting systems must balance false alarms and misses; too many false alarms cause alarm fatigue and ignored alerts.',
    'Is the alert/notification threshold tuned to avoid alarm fatigue while catching important events?', 'flow', '',
    'Green, D. M. & Swets, J. A. (1966). Signal Detection Theory and Psychophysics. Wiley.', E, 'Alerts')
add('err.alarm-fatigue', 'Alarm fatigue / cry-wolf effect', 'S. Breznitz', 1984,
    'Frequent false alarms reduce trust and response to subsequent alarms.',
    'Too many warnings, badges and notifications train users to ignore them, including the important ones.',
    'Are warnings rare enough that users still take them seriously?', 'flow', '', 'Breznitz, S. (1984). Cry Wolf: The Psychology of False Alarms. Lawrence Erlbaum.', E, 'Alerts')

# ---------------- Learning & skill ----------------
add('learn.power-law-practice', 'Power law of practice', 'A. Snoddy; A. Newell & P. Rosenbloom', '1926/1981',
    'Time to perform a task decreases as a power function of the number of practice trials: fast improvement early, slower later.',
    'Most learning happens in the first uses; first-run experience and early consistency matter most.',
    'Is the first-use experience optimized, since most learning happens early?', 'flow', 'T = a·N^(-b)',
    'Newell, A. & Rosenbloom, P. S. (1981). Mechanisms of skill acquisition and the law of practice. In Anderson (Ed.), Cognitive Skills and Their Acquisition.', L, 'Skill acquisition')
add('learn.perpetual-intermediates', 'Perpetual intermediates', 'A. Cooper', 1995,
    'Most users are neither beginners nor experts; they quickly become intermediates and stay there.',
    'Optimize for intermediates: fast access to common functions, help on demand, and shortcuts without forcing expert syntax.',
    'Is the interface optimized for intermediate users (not only first-run novices or power users)?', 'screen', '',
    'Cooper, A. (1995). About Face: The Essentials of User Interface Design. IDG.', L, 'User expertise')
add('learn.baby-duck', 'Baby duck syndrome (imprinting)', 'Usability folklore', '1990s',
    'Users tend to prefer the first system they learned and judge others by their similarity to it.',
    'Redesigns of established products should preserve familiar paths or provide transition help.',
    'After a redesign, are familiar paths preserved or is transition help provided?', 'flow', '', 'Widely cited usability folklore; related to Zajonc (1968) mere exposure.', L, 'Familiarity', sev='minor', conf='medium')
add('learn.carroll-training-wheels', 'Training wheels interfaces', 'J. Carroll & C. Carrithers', 1984,
    'Blocking advanced, error-prone functions for beginners lets them learn faster and make fewer errors.',
    'Staged feature exposure can help novices; unlock complexity as skills grow.',
    'For complex tools, are novices protected from advanced error-prone functions until needed?', 'flow', '',
    'Carroll, J. M. & Carrithers, C. (1984). Training wheels in a user interface. CACM, 27(8), 800–806.', L, 'Learning', sev='minor')

# ---------------- Measurement & research laws ----------------
add('meas.five-users', 'Testing with 5 users (problem discovery model)', 'J. Nielsen & T. Landauer; R. Virzi', '1992/1993/2000',
    'The proportion of usability problems found with n users follows 1 − (1 − p)^n; with p ≈ 0.31, five users find about 85% of problems. Iterative small tests beat one big test. Low-frequency problems and diverse user groups need more participants.',
    'Run small, frequent qualitative tests; test each distinct user group separately; do not use 5 users for quantitative benchmarks.',
    'Is usability testing iterative with small samples per user group, and quantitative claims based on larger samples?', 'organizational / research', 'Found = 1 − (1 − p)^n; p ≈ 0.31 → n=5 ≈ 85%',
    'Nielsen, J. & Landauer, T. K. (1993). A mathematical model of the finding of usability problems. INTERCHI \'93, 206–213; Virzi, R. A. (1992). Refining the test phase of usability evaluation: How many subjects is enough? Human Factors, 34(4), 457–468; Faulkner, L. (2003). Beyond the five-user assumption. BRMIC, 35(3), 379–383.', ME, 'Sample size')
add('meas.hawthorne', 'Hawthorne effect / observer effect', 'Western Electric studies; H. Landsberger', '1924–1932/1958',
    'People may change their behavior when they know they are being observed.',
    'Usability test participants try harder and are more polite than real users; triangulate lab findings with analytics and field research.',
    'Are lab findings validated against real-world behavior data?', 'organizational / research', '',
    'Landsberger, H. A. (1958). Hawthorne Revisited. Cornell University.', ME, 'Research bias', sev='minor')
add('meas.evaluator-effect', 'Evaluator effect', 'M. Hertzum & N. Jacobsen', 2001,
    'Different evaluators analyzing the same usability sessions or doing heuristic evaluation identify substantially different sets of problems.',
    'Use multiple evaluators (Nielsen recommends 3–5 for heuristic evaluation) and aggregate findings.',
    'Is the audit performed or reviewed by more than one evaluator, with findings aggregated?', 'organizational / research', 'Average any-two agreement often 5–65%.',
    'Hertzum, M. & Jacobsen, N. E. (2001). The evaluator effect: A chilling fact about usability evaluation methods. IJHCI, 13(4), 421–443.', ME, 'Evaluation reliability')
add('meas.he-evaluators', 'Number of evaluators for heuristic evaluation', 'J. Nielsen & R. Molich; J. Nielsen', '1990/1992',
    'Single evaluators find about 35% of problems; aggregating 3–5 evaluators finds about 75%.',
    'Automated or single-expert audits should be presented as partial; combine with more evaluators or user testing.',
    'Is the confidence of a single-evaluator audit communicated honestly?', 'organizational / research', '1 evaluator ≈ 35%; 5 ≈ 75%',
    'Nielsen, J. (1992). Finding usability problems through heuristic evaluation. CHI \'92, 373–380.', ME, 'Evaluation reliability')

write('curated_laws', R)
