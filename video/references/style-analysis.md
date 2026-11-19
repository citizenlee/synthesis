# Story's storytelling style: language, build-up, visuals, pacing

> **Source.** Copied from Cultivarium's `ai-summit-2026-demo` repo (file `docs/references/style-analysis.md` in that project; tarball `style-analysis.md`). House style of Story / storyandscience launch films, measured Nov 2026. Sibling Cultivarium docs (`context.md`, `north-star.md`, `storylines.md`, `tasks.md`, `outline.md`) are **not** copied into this repository.
>
> **How to use it here.** Sections 1–3 are the method (poem vs explainer register, hinge, grade, pacing). Section 4 applies that method to Cultivarium's ARIA robot demo — ignore it for Synthesis VO, shots, and positioning. Charts and `data/` from the source repo are not in this copy; the numbers in the tables still stand.

Reference for a 90–120 s launch film. Original index and caveats lived at [`story-launch-videos.md`](story-launch-videos.md) (not in this repo). Beat structure (secondary): [`storyline-analysis.md`](storyline-analysis.md) (not in this repo).

Tags: **[obs]** observed or measured in the file; **[inf]** my inference. Times are mm:ss in the video. "Story films" means the films in the index; attribution is confirmed for Rangeview, SendCutSend and Zeromatter only (Saronic, fomo, Pioneer, Edison, Turba are from the earlier search and not confirmed in this pass; Turba is a weak stand-in). Read the cross-film patterns with that in mind.

Method in one line: VO from whisper (word times) or YouTube captions (cue times, so +/- 1-2 s), on-screen text via OCR, loudness via ffmpeg `ebur128`, cuts via `scene>0.3`, luma/saturation/hue via 2 fps 96x54 frames in Python. Details and charts are in `data/` and `charts/`.

---

## 1. Headline numbers (all films)

| Film | Len | VO words | Words/min (whole film) | VO share of runtime | Median gap between lines | Cuts/min [obs, approx] | Median shot | Integrated LUFS | LRA (LU) | Mean luma (0-1) | Mean saturation | Near-black pixels | Warm : cool (saturated px) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rangeview | 3:02 | 90 (exact script from the YouTube description) | 30 | ~23 % (est.) | 4.0 s (max 14 s) | 14 | 3.2 s | -13.7 | 13.6 | 0.19 | 0.37 | 48 % | 51 : 46 |
| SendCutSend | 2:00 | ~87 (caption-based) | 44 | ~30 % (est.) | 5.3 s (max 13.5 s) | 45 | 1.0 s | -11.2 | 8.8 | 0.29 | 0.43 | 29 % | 45 : 51 |
| Saronic | 0:45 | 0 (text only) | 0 | - | - | 25 | 2.1 s | -16.9 | 6.8 | 0.33 | 0.29 | 8 % | 2 : 98 |
| fomo | 1:45 | ~107 (caption-based) | 61 | ~39 % (est.) | 7.0 s (max 23 s) | 22 | 1.8 s | -20.2 | 4.5 | 0.20 | 0.33 | 47 % | 59 : 35 |
| Zeromatter | 1:40 | 189 | 113 | 65 % | 1.3 s (max 4.1 s) | 56 (see caveat) | 0.6 s | -17.8 | 7.1 | 0.27 | 0.38 | 37 % | 12 : 72 (+15 green/yellow) |
| Pioneer Labs | 1:28 | 172 | 117 | 72 % | 2.2 s (max 3.9 s) | 22 | 2.4 s | -16.0 | 6.3 | 0.27 | 0.39 | 24 % | 88 : 8 |
| Edison | 1:22 | 262 | 192 | 87 % | 0.5 s (max 1.4 s) | 27 | 1.7 s | -26.1 | 3.9 | 0.21 | 0.33 | 40 % | 51 : 35 |
| Turba (site film) | 1:00 | 0 (text only) | 0 | - | - | 13 | 2.4 s | -16.6 | 16.8 | 0.13 | 0.51 | 54 % | 34 : 59 |

Reading it [obs]: the "poem" films (Rangeview, SendCutSend) speak 30-45 words/min with 4-5 s of air between lines; the "founder explainer" films (Zeromatter, Pioneer, Edison) speak 113-192 words/min with 0.5-2 s gaps. fomo sits between (a spoof newsroom with long gaps). Every film is low-key: mean luma 0.13-0.33 and the 90th percentile of luma never above 0.54, so none is a bright, high-key film.

Caveats: Zeromatter's cut count includes flicker from sim-UI walls; Rangeview's and Turba's are low because of dissolves. VO share for caption films uses an assumed 0.35 s/word, so treat it as an estimate.

---

## 2. Film by film

### 2.1 Rangeview, "Will you answer?" (3:02) -- the "slow, cinematic" template
Story's own words in the BTS (auto-captions, ~6:03-7:20 and 12:19-13:10; wording lightly cleaned): the client "didn't want us to just make another product or a launch video. He wanted this to feel different, slower, cinematic, intentional"; "one of the first times we ever did a proper storyboard", with lots of reference imagery; the idea "built around father speaking to his son"; first shot "a kid shoulder and a hand being placed on it", then the New York skyline; a lot of archival footage; some shots on green screen "for a high degree of control over lighting"; the team wanted "this filmic, dirty, grainy kind of texture" instead of a "clean, safe look". [obs, from BTS captions]

**Language.** Full VO, matching the YouTube description exactly [obs]: "Dear son, / Some time ago, the machines roared. The steel bent to our hands. We built for the stars, for our land, for your future. We went fast, we went far. It made us strong. It united us. / Then the sound faded. Those who knew, grew tired. The hunger to build drifted away. But now the fire, returns. The steel is ready. The country needs you. New boundaries beckon. Who will you be. Where will you take us. The stars are calling. Our future is waiting. So will you answer?"
- 25 lines, longest 6 words, average ~3.7 words. Past tense, concrete nouns (machines, steel, hands, fire), verbs that physical (roared, bent, faded, drifted). [obs]
- Devices [obs]: direct address from the first words ("Dear son"); triple anaphora "for the stars, for our land, for your future" (scale falls from cosmic to personal, ending on "your"); paired parallels "We went fast, we went far" / "It made us strong. It united us."; a "Then ... But now" hinge; a chain of three questions only at the end ("Who will you be. Where will you take us." then "So will you answer?"). Titled after the final question, so the title is the CTA.
- Pronoun arc [obs]: "we/our" (0:09-0:57) -> absence (no VO ~1:09-1:21) -> "the country needs you" at 2:07 (70 % in) -> "you" questions. "We" is heritage, "you" is the ask.
- The company name is **never spoken** and appears only as a small grey letter-spaced wordmark at 2:56 over embers; the CTA URL is only in the YouTube description (rangeview.com/careers). [obs]

**Build-up.** Three waves of music and image, with the turn at 1:05-1:11: the line "Then the sound faded" starts at ~1:06 and is followed by ~12 s with no VO (to ~1:21); the measured loudness drops from about -19 LUFS to a momentary low near -46 LUFS at ~1:09 (4-s averages: -28 at 1:04-1:12) [obs]. The "problem" is shown as decay (derelict plants captioned "Gray Iron Factory, Detroit, MI", "Bethlehem Steel, Lehigh Valley, PA", "Packard Plant, Detroit, MI", then "Precision Grinding, El Segundo, CA 2025" at 1:28-1:36 [obs OCR]). The picture turns before the words do: a furnace glow appears around 1:42 and the line "But now the fire, returns" lands at ~1:47 [obs from sheet + captions]. Final build 1:40-2:30 with line spacing getting longer (9-10 s between the last lines) while loudness peaks at -9 LUFS around 2:32 [obs].

**Visuals.** Lighting: low-key, practical and rim light, silhouettes (father and son against a skyline, two ranchers at dusk, an astronaut, a figure in a dark hall) [obs sheet]. Frames get darker as the film progresses: mean luma by thirds 0.28 -> 0.17 -> 0.13, while saturation rises 0.31 -> 0.38 -> 0.42, because the darkness is filled with orange fire/slag [obs]. 48 % of pixels are near-black. Palette: amber/orange against teal/cyan (51 % warm : 46 % cool of saturated pixels) [obs]. Framing: wide establishing, then extreme close-ups of faces and eyes (1:49), low-angle hero shots (worker in hard hat at 2:04), vintage archival footage in letterboxed/rounded inset (1:27) mixed with new filmic footage [obs sheet]. Motifs: hands on shoulder, people looking up, skylines, furnaces, stars. Grain and film texture are deliberate (BTS). End: black with embers, small wordmark.
Chart: ![](charts/rangeview.png)

**Pacing and audio.** VO 30 words/min; the first line at 0:05; typical gap 4 s; cuts ~14/min but front-loaded (20 of 43 detected cuts in the first third; a 36/min burst at 0:10-0:20) [obs]. Music enters from near silence (about -39 LUFS averaged over the first 4 s), reaches -8 at ~0:45, falls into a trough (1:04-1:12, and a smaller one at 1:28-1:36), and rebuilds in steps to a climax around 2:00-2:32, then decays to -33 at the end (the last ~3 s are near silence) [obs]. Integrated -13.7 LUFS, LRA 13.6 LU, the widest dynamic swing of the narrated films (except Turba).

### 2.2 SendCutSend, "Manufacturing the Future" (2:00) -- kinetic maker montage
**Language.** VO [obs, YouTube auto-captions, with times]: 0:02 "They say the future starts in garages." / 0:18 "It crawls until it walks." / 0:26 "It modifies. And it always pushes the limit." / 0:37 "It starts as a hobby, then it takes off." / 0:43 "In the future, looks like the future." (caption text as auto-transcribed; likely "the future ... looks like the future"; check by ear) / 0:54 "And we believe the future is made in America." / 0:59 "The land of the free and the home of the builder." / 1:11 "But the future has to be built. / 1:15 It has to be flown. / 1:18 It has to be sailed." / 1:24 "Pioneer launched." (auto-caption, suspect) / 1:30 "It's built" ... 1:44 "by you." / 1:51 "Send, cut, send, helping you build the future."
- Devices: a hearsay open ("They say"), then rebuttal-by-demonstration; present-tense "life cycle" verbs (crawls, walks, modifies, takes off); rule of three with an escalating medium (built, flown, sailed); "But" at 59 % marks the turn from proof to claim. The second person arrives only at 1:44 (87 %), by splitting a sentence across a 14 s instrumental gap ("It's built ... by you") so the word "you" lands alone. The brand is named in the last 9 s. [obs]
- Words are 3-11 per line, average ~6; ~44 words/min; median gap 5.3 s. [obs]

**Build-up.** Strictly monotonic music ramp: from -26 LUFS at the start, -14 by 0:04, up to -8 LUFS at 1:04 (on "builder"), a plateau around -10 until 1:40, then a stepped drop to -15, -18, -20 under the sign-off and -36 at the end [obs]. Cut rate climbs 36 -> 42 -> 54 -> 72 -> 66 -> 72 cuts/min through the first minute, then eases to 24/min for the last 30 s (peak load at 0:30-1:00, resolution is slower) [obs]. Picture is escalation by scale: garage tinkering (hands, welding, a robot in a workshop) -> projects on dry lakes, snow and roads -> rocket, spacecraft, a large ship hull and Earth from orbit (~1:12-1:26) -> back to a person in a shop -> black frame with a US flag (1:45) -> logo on a cut part [obs sheet].

**Visuals.** Mixed: dark workshops lit by practical light and sparks vs. sun-bleached desert, snow and sea-level daylight. Mean luma 0.29 (the brightest of the narrated films), saturation 0.43 (highest of them), near-black 29 %. Warm : cool = 45 : 51 [obs]. Lower-third credits (OCR) name each maker project on screen in small text ("K-Scale Labs", "Stanceworks", "Hoonigan", "Texas A&M Rocket Engine Team", "NASA"...). Retro rounded-corner inset frames (about 0:38, 0:48, 0:53) mimic old TV/film for the "heritage" shots. End: logo on a laser-cut part, then sendcutsend.com at 1:55-1:58 [obs].
Chart: ![](charts/sendcutsend.png)

**Pacing and audio.** Loudest film in the set (-11.2 integrated). 1.0 s median shot. VO is sparse against a dense picture: the pictures and the music carry the film [obs].

### 2.3 Saronic, "Corsair" (0:45) -- spec-sheet kinetics, no VO
**Language (on-screen only, OCR) [obs]:** 0:03 "Corsair / AUTONOMOUS SURFACE VESSEL [ASV] / SARONIC TECHNOLOGIES" -> 0:05 "DESIGNED FOR Strategic blue-water operations" -> 0:09 "OPERATE ALONE OR IN Collaborative Swarms" -> 0:12 "READY FOR ANY MISSION Modular Payload Bay + Open Architecture" -> 0:15 "AUTONOMOUSLY Identify, Track, Follow + Intercept Targets" -> 0:17 "P.A.C.E. REDUNDANT COMMUNICATIONS FOR DENIED ENVIRONMENTS" -> 0:22 "Highly Maneuverable / FULL CONTROL AUTHORITY AT TOP SPEED OF 35+ KTS" -> 0:29 "Manufacturing at scale / VERTICALLY INTEGRATED TO UNLOCK HARDWARE + SOFTWARE" -> 0:35 "SEE TARGETS WITHOUT BEING SEEN" -> 0:40 SARONIC wordmark. Pattern: a large sentence-case headline (2-3 words) over a small-caps qualifier line; one claim per 2-4 s; capabilities are written as noun phrases and adjectives, never full sentences. The last text ("See targets without being seen") is the closest to a sentence and works as a paradox-style tagline, placed ~5 s before the logo.

**Build-up.** No arc in words; the escalation is capability by capability, ending on a tagline. Music: -33 LUFS at the start, about -17 by 0:06, a dip to about -27 at 0:15-0:21 (between "Intercept Targets" and "Highly Maneuverable"), back to -15 from 0:30 through 0:39, fall to -32 at the logo [obs].

**Visuals.** Daylight, aerial drone tracking shots of a light-grey/white boat on dark blue sea, white wake as the only bright element; 98 % of saturated pixels are blue/cyan; near-black only 8 %; mean luma 0.33 [obs]. Camera: constant motion (orbit, chase, top-down). One interior shot of a hull in a white fabrication hall (0:29) as the "manufacturing" proof, with a hand wiping a surface (0:31). End: wordmark centred over the boat at distance (0:40-0:45). 19 cuts, 25/min [obs].
Chart: ![](charts/saronic.png)

### 2.4 fomo, "welcome to fomo web" (1:45) -- deadpan spoof of the epic launch
**Language.** VO and dialogue [obs, captions]: 0:04 "This is Houston. T minus 1 minute until full data blackout." / 0:08 "All eyes are on you." / 0:18 "Breaking news, there is an astronaut conducting an emergency repair on a global communication satellite that could go dark at any moment. We have a second angle on this." / 0:26 "Is that guy on FOMO? Oh, yeah. Let me through. Crazy train. Yeah, let's get back to it, everybody." / 0:57 "Opportunity cost is simply this. Every position you take is a position you choose over something else." / 1:09 "This just in. According to the astronaut's FOMO account, highest in the room, the satellite has been restored." / 1:34 "Satellite's up and running. Positions looking good, too." / on-screen 1:33 "the whole web is watching" then "fomo / fomo.family".
- The joke engine: mission-control gravity ("T minus", "full data blackout", "All eyes are on you") undercut by trivia (the astronaut is checking a trading app). A news-anchor register ("Breaking news", "This just in") frames the product as an event. The only second-person line ("All eyes are on you") is in the opening lines. The thesis line is a plain definition ("Opportunity cost is simply this.") delivered deadpan. A laptop tab in frame reads "web app launch video" (OCR 0:35-0:36), a meta wink. [obs]

**Build-up.** Flat. Loudness stays between -19 and -23 LUFS for 100 s (LRA 4.5 LU, the lowest of the music-led films): no swell; tension comes from the premise and the deadpan, not music. Cut peaks at 0:30-0:40 and 1:20-1:30 (30-42/min) [obs].

**Visuals.** High-production cinematic look applied to a trivial subject: Earth limb, astronaut in a helmet with shallow depth of field, offices with warm practicals, a driver in a car, UI overlays composited (ticker, rank list, position chip). Mean luma 0.20, 47 % near-black pixels, warm : cool 59 : 35 [obs]. Ends on an astronaut-with-satellite graphic over Earth with the line "the whole web is watching", then logo and URL [obs].
Chart: ![](charts/fomo.png)

### 2.5 Zeromatter, out of stealth (1:40) -- explainer VO over blueprint visuals
**Language.** Full VO (whisper medium, word times; the CEO "Ian Glow, Founder & CEO" is shown by lower third at 0:15 and on camera at 0:16, 0:56, 1:20; whether the VO is him is [inf]) [obs]:
0:04 "The world is becoming more autonomous." / 0:07 "Cars," / 0:09 "planes," / 0:11 "industrial and home robots." / 0:14 "The increasing embodiment of AI will reshape every aspect of our lives." / 0:21 "Any autonomous system should be tested a billion times over before it's ever trusted to move through our world." / 0:28 "That's why we built Zeromatter." / 0:31 "One platform to build, test, and train anything." / 0:37 "To train a machine, you have to see what it sees." / 0:40 "Cameras, LiDARs, and radars perceive our synthetic environments and react just as they would in the real world." / 0:48 "We can replicate the physics of the most critical moments," / 0:52 "from taking a corner at high speed to a robot installing a delicate part into a vehicle. We build worlds that these machines can inhabit that they cannot tell are different from the physical world. Every scenario can be rehearsed endlessly until the product is provenly safe. Including the scenarios that you could never attempt on our roads," / 1:11 "in our factories," / 1:12 "or in the skies over our towns and cities." / 1:18 "The safer physical intelligence becomes, the sooner that abundance arrives." / 1:25 "Before a machine ever moves through the real world, it has already lived a billion lives" / 1:33 "in Zeromatter." (the on-screen subtitle for "autonomous" is in orange at 0:04.)
- Devices [obs]: a macro-trend cold open in six words; the list "Cars, planes, industrial and home robots" delivered as separate beats 1.2-1.7 s apart (while the picture swaps wireframes); the stake in one number ("a billion times over") that returns as the payoff ("lived a billion lives"); the "That's why we built X" hinge at 28 % with the name only then; a three-part place list ("our roads, ... our factories, ... the skies over our towns and cities") that widens from road to sky; the contrast clause "The safer ..., the sooner ..." as the thesis; the last line puts the company name last, after a 2.5 s pause ("In Zeromatter").
- Pauses [obs]: 4.1 s of silence before "The safer physical intelligence becomes" and 2.8 s before the final sentence; everything else is 0.7-2.8 s.

**Build-up.** Information escalates (problem -> why -> how -> stake -> payoff). Music: -24 LUFS at start, a slow ramp to -15/-16 LUFS between 1:04 and 1:20 (peak about 1:16), then falls to -26 at 1:32 and -36 at the end card [obs].

**Visuals.** Two worlds, deliberately contrasted [obs sheet]: cool cyan blueprint wireframes (aircraft, car, robot arm) and lidar point clouds on black, versus real footage (runway, wet road at night, airliner takeoff) and a warm founder interview shot in profile against a blurred purple-peach dusk background. 72 % of saturated pixels are blue/cyan, 12 % warm; 37 % near-black. Persistent bottom-left label "MADE IN ZEROMATTER" on synthetic shots (OCR from 0:06 through 1:11) so viewers always know what is simulated. Silhouetted people stand in front of wireframes (0:00) and of a curved wall of sim views (1:04, 1:28) (Story's tweet: "Everything on the wall behind them is from their simulation software"). Fisheye/multi-camera tile view with camera names ("fisheye_front", "front_wide") at 0:45. End: icon at 1:32, wordmark at 1:36 [obs].
Chart: ![](charts/zeromatter.png)

### 2.6 Pioneer Labs, "first microbe for Mars" (1:28) -- closest to a biology-science demo
**Language.** Full VO with burned-in captions (OCR confirms; word-by-word, white, bottom centre) [obs]:
0:00 "We have successfully created the first organism designed for Mars." / 0:07 "On Earth, evolution created an entire biosphere that sustains us. Everything life needs to thrive is given to us by nature." / 0:19 "When humanity goes to space, we have to bring nature with us." / 0:26 "Landing a rocket is only the beginning. Once you land, you have to create conditions that make life possible in a very harsh environment. At Pioneer Labs, we're engineering life to make Mars more habitable." / 0:41 "Pioneer Labs Strain 1 uses the nutrients in Martian dirt, water and atmosphere to produce bioplastics, an extremely useful class of materials to make infrastructure, including habitats for people." / 0:57 "Being able to use the materials on site is the huge unlock that actually enables people to go to Mars, to live there, you need to be able to use local resources." / 1:10 "No constant resupply from Earth, no dependence on Earth's supply chains. Instead, we can live off the land and build from what Mars provides." / 1:21 "The future of Mars starts here." Title card at ~1:21: "Where no microbe has gone before."
- Devices [obs]: result-first cold open (the claim before the context); an Earth-to-Mars analogy ("evolution created an entire biosphere" -> "we have to bring nature with us"); "Landing a rocket is only the beginning." (a deflation line at 30 % that redefines the problem); a plain-statement product reveal at 47 %, one sentence with inputs (dirt, water, atmosphere) and output (bioplastics) and use (habitats); a double negation ("No constant resupply ..., no dependence ...") followed by an "Instead, we can ..." resolution; a one-line tagline; a pun title card (Star Trek echo) that carries the only humor, after the sincere ending.
- Voice: the founder/CEO (Erika DeBenedictis, lower third at 0:28) appears on camera; whether the VO is her voice is [inf]. VO blocks between pauses are 11-37 words, conversational; no rhetorical questions. [obs for the text]

**Build-up.** Claim -> world-building -> problem ("harsh environment") -> product -> why it matters -> promise -> pun. The tonal "turn" is the move from cold/dark Mars imagery to lab warmth between 0:26 and 0:50 [obs]. Music is flat at -15 to -19 LUFS from the first second (peak at 0:01); no silence gap [obs].

**Visuals.** The warmest film: 88 % of saturated pixels are orange/red, saturation 0.39; luma by thirds 0.21 -> 0.35 -> 0.26: dark Mars-limb opening, bright warm lab middle, dusky ending [obs]. Motifs [obs sheet]: instrument close-ups (a pressure gauge in the first frame; a bioreactor display "RPM 192 / C 15.0" at 1:06); macro of leaf veins and microorganisms; lab hands in purple nitrile gloves holding a petri dish (1:14); the CEO in an orange striped sweater in a warm lab, off-axis; CG Mars landscapes and a habitat dome; final image: a single yellow flower sprouting from red regolith with a sun flare (1:21-1:24), placed under the wordmark. Cuts 22/min, median shot 2.4 s.
Chart: ![](charts/pioneer.png)

### 2.7 Edison Scientific, Kosmos x Incyte (1:22) -- interview-led, data-visual
**Language.** No narrator. Two interviewees: Samuel Rodriques (Co-founder & CEO, lower third at 0:06) and Patrick Mayes (Chief Scientific Officer, Incyte, 0:43) [obs OCR]. Lines (whisper): 0:01 "The average drug takes more than a decade and over a billion dollars to reach the market. And you have to imagine that, like, every day in that process that the drug is not approved, there are millions of patients who need the medicine who don't have it." / 0:15 "The fundamental thing that pharma companies do is that they get data. These data sets are probably the single highest value and most underutilized data asset that humanity has access to today. One of the key innovations in [Kosmos] is our use of a structured world model ... That virtuous cycle is what makes [Kosmos] really special." / 0:43 "So we believe [Kosmos] has the potential to become embedded directly into the scientific workflow ... At Edison, it's not just AI researchers, we have just a ton of scientists ..." / 1:06 "I think that people have gotten accustomed to the idea that, you know, oh, drugs should just take 30 years to develop and they should just cost billions of dollars and that's just the way the world is and what we're saying is it doesn't have to be that way." (The transcript says "Cosmos"; the on-screen product name is KOSMOS.)
- Devices [obs]: opens on a cost-of-delay statistic, with matching on-screen text "MORE THAN A DECADE / OVER $1 BILLION DOLLARS" at 0:02-0:04 (in sync with the spoken numbers); then mundane human stakes ("millions of patients who need the medicine"); a reframing close ("what we're saying is it doesn't have to be that way") instead of a CTA. Long, run-on, conversational sentences (average ~26 words per speech block, up to 70). The most spoken-word-dense film: 192 words/min, gaps median 0.5 s. [obs]

**Build-up.** Problem (cost of time) -> what the field does -> mechanism -> why it works -> endorsement from a customer -> defiant reframe -> logo. The "turn" to product is visual, at 0:29-0:39, when the orb turns into a diagram titled KOSMOS with orbiting labels MOLECULAR DESIGN, TARGET DISCOVERY, CLINICAL TRIAL DESIGN, COMPETITIVE INTELLIGENCE, BIOMARKER STRATEGY, CLINICAL DATA ANALYSIS [obs OCR]. Loudness is low and flat: -26 LUFS integrated, LRA 3.9 LU, no swell (this X file is quieter than all the others; I did not check by ear whether a music bed exists) [obs].

**Visuals.** Dark opening (luma 0.16 in the first third) with a single glowing pearl on blue -> bright daytime interview in a lab with window light (0.30 in the middle) -> dark ending (0.16). Saturation falls 0.41 -> 0.35 -> 0.23, finishing near monochrome white logo on black (1:20) [obs]. Interview framing: CEO in a red T-shirt, 3/4 profile, shallow depth of field, lab equipment bokeh; Incyte CSO in a white shirt against green outdoor light; cutaways: pipetting, a person at a microscope, a clinical-document UI with counters ("KEY SUMMARY STATISTICS ... Clinical Studies 8 ... 1,952 subjects ... 1.28M data points" at ~1:09; the counters animate, OCR at 1:10 reads 2,067 / 1.36M). Particle clouds (gold dots on black) as "data" shots [obs sheet, OCR].
Chart: ![](charts/edison.png)

### 2.8 Turba Labs site film (1:00; provenance unverified) -- text and imagery, no VO
**Language (on-screen)** [obs OCR]: 0:00-0:04 "Today, most data centers operate at a fraction of their theoretical potential" (typed in) ... 0:52-0:55 "The world's first AI performance platform" -> 0:56 TURBA LABS wordmark. Only two text beats in 60 s.
**Visuals.** The most unusual film: it opens and closes on the **same one-point-perspective shot of a symmetrical server aisle**, in between it cuts to non-technical imagery (desert dusk, observatory telescopes with a red laser, a nebula, a CT scan of a head, a stopwatch, a person in a rocky canyon) [obs sheet]. 79 % of frames have mean luma < 0.15, saturation the highest at 0.51, with red and cyan accents. Music: -33 at the start, a dip to -37 at 0:18, a build to -13 at 0:48, then a drop to -50 at the logo [obs].
Use it only for the bookend trick (same image first and last) and for how little text it uses. [inf]
Chart: ![](charts/turba-site.png)

### 2.9 S3 docs and the Rangeview BTS (transcript level, secondary)
[obs from captions] The S3 host-led documentaries open by naming the claim or the stakes in the first sentence: Multiply Labs: "... we're going to unveil the world's first robotic system that's modular for manufacturing cell therapies"; Varda opens with the founders' joke hook "we're building the world's first bioreactor with a gravity off switch and unfortunately we've got to go to space to do it"; Orchid opens with a statistic then a personal motive ("because of my mom ... what if instead of rolling the dice ... parents had the opportunity to mitigate risk"). Signature sign-off (Multiply, Orchid, BTS): "keep on building the future / keep on building". In the Varda episode the host says the show's goal is "that we don't explain things in the videos so they're more inspirational and exciting and like get you pumped", with detail pushed to linked clips and the blog. [obs] That is the clearest statement of Story's preference for emotion first and explanation elsewhere. [inf: it is the host's S3 policy, not necessarily the policy for commissioned films]

---

## 3. Cross-film synthesis: the "Story house style" [inf from the above, with the measured support]

### 3.1 Language
1. **Open with a short concrete line, not the company.** First VO lines: "Dear son," (Rangeview), "They say the future starts in garages." (SCS), "The world is becoming more autonomous." (Zeromatter), "This is Houston." (fomo), "We have successfully created the first organism designed for Mars." (Pioneer), "The average drug takes more than a decade and over a billion dollars to reach the market." (Edison). Each opener is one sentence of 2-17 words (Edison's is the longest). [obs]
2. **Name the company late and once.** Rangeview: never spoken (wordmark at 2:56). SendCutSend: at 1:51 of 2:00. Zeromatter: first at 0:28 then the last words at 1:33. Pioneer: "At Pioneer Labs" at 0:34 (a title lockup appears at ~0:06). Edison: lower-third "Edison Scientific" at 0:06, product Kosmos at ~0:25, logo at 1:20. fomo: end card. [obs]
3. **Short declaratives with parallel structure** (Rangeview lines are 3-6 words; SCS 3-11). Repetition does the work: "for the stars, for our land, for your future"; "It has to be built. It has to be flown. It has to be sailed."; "no constant resupply, no dependence"; "our roads, our factories, ... our towns". Lists are in threes. [obs]
4. **One number or one image that returns**: "a billion times" -> "a billion lives" (Zeromatter); "the sound faded" -> loudness dip (Rangeview); the same server aisle open and close (Turba). [obs]
5. **A hinge word at 30-60 %**: "Then" (36 %) / "But now" (59 %) in Rangeview; "But" (59 %) in SCS; "That's why we built" (28 %) in Zeromatter; "Landing a rocket is only the beginning" (30 %) in Pioneer. [obs] Before the hinge: a world/heritage/problem. After: the product or the ask.
6. **We -> you.** "We/our" through the film; "you" appears only at the end as the ask or the final address (Rangeview 2:07+, SCS 1:44, fomo's "All eyes are on you" is the exception, up front). Questions are reserved for the last ~20 % of the runtime (Rangeview: three in a row from 2:20). [obs]
7. **Understate the tech, overstate the stakes.** No feature lists in VO except the spec film (Saronic) and the explainer (Zeromatter); the product is given one plain sentence (Pioneer 0:41; Zeromatter 0:31). [obs]
8. **Humor, when used, is deadpan and comes from scale mismatch**: fomo's mission control vs. a trading app; Pioneer's "Where no microbe has gone before" after a sincere ending; Varda's "unfortunately we've got to go to space". [obs]

### 3.2 Build-up
- Two shapes seen. **Heritage -> decay -> return -> ask** (Rangeview; SCS in a shorter form), turn visible in both sound and picture. **Claim -> world -> problem -> product -> promise** (Pioneer, Zeromatter, Edison), the turn mostly in the words. [obs]
- The escalation is carried by **music loudness and cut rate rising together, then a drop**: SCS climbs 18 LU in 60 s and 36 -> 72 cuts/min; Rangeview climbs in three waves to -9 LUFS; Zeromatter ramps ~9 LU. Then all end with a hard fall in the last 3-4 s to <= -30 LUFS under the logo (Rangeview -33, SCS -36, Zeromatter -36, fomo -34, Saronic -32, Turba -50). [obs]
- All films begin from near silence (loudness averaged over the first 4 s: Rangeview -39, Turba -33, Saronic -33, fomo -28, SCS -26, Zeromatter -26 LUFS) [obs]; Pioneer and Edison start already in speech.
- A **deliberate trough** is used as the turn in the most "poetic" film (Rangeview 1:04-1:12: 4-s average drops ~9 LU, momentary low -46 LUFS at 1:09, and no VO for ~12 s) [obs].

### 3.3 Visuals: lighting, grade, framing, camera
- **Low-key by default.** Mean luma 0.13-0.33; 24-54 % of pixels near-black in seven of eight films (Saronic 8 %); p90 luma at most 0.54. Faces are lit from the side or rim, backgrounds fall to black. [obs]
- **Complementary warm/cool split.** Warm:cool of saturated pixels is 51:46 (Rangeview), 45:51 (SCS), 59:35 (fomo), 51:35 (Edison) = a teal-and-amber look; Pioneer is almost entirely warm (88 %), Zeromatter/Saronic/Turba mostly cool (72 / 98 / 59 %). Mean saturation 0.29-0.51 (0-1 HSV), i.e. moderately saturated, not pastel. [obs] Warm = people and fire; cool = machines, space, simulation (Zeromatter's founder is warm against dusk; his sim imagery is cyan) [obs sheet].
- **Interview look**: 3/4 profile, off-axis, shallow depth of field, practical bokeh, lower third in small type with name and role (Zeromatter 0:15, Edison 0:06, Pioneer 0:28). [obs]
- **Camera**: slow push-ins and dollies on people, drone chase/orbit on vehicles, macro on process, silhouettes and low-angle hero shots; rarely handheld. [obs sheet] Film grain is intentional in Rangeview (BTS). Archival footage and a "location, year" caption for the past (Rangeview). [obs]
- **Motifs** recurring across films [obs sheet]: hands (shoulder, gloves, wiping a hull), people looking up, silhouettes against skylines/screens, fire/glow, gauges and instruments, Earth/planet limbs, wireframes/point clouds, macro/microscope.
- **Label what is synthetic**: Zeromatter keeps "MADE IN ZEROMATTER" on every sim shot (0:06-1:11). [obs]
- **End card**: black or one hero image, a small wordmark, held ~2-6 s (Edison 2 s, Zeromatter 4 s, Saronic 4.5 s, SCS ~5 s, fomo 6 s, Rangeview 6.5 s, Pioneer ~7 s including the tagline), near-silent audio. [obs]

### 3.4 Pacing through words and audio
- Two speech registers: **poem** (30-45 words/min, 3-7-word lines, 4-5 s median gap, VO ~25-30 % of the runtime) and **explainer** (110-190 words/min, 0.5-2 s gaps, 65-87 % of the runtime). Pick one; none of these films mixes them. [obs for these films; whether it is a Story rule is [inf]]
- Pauses sit **before the key line**: Zeromatter 4.1 s before the thesis and 2.8 s before the final sentence; Rangeview spacing grows to 9-10 s before the last two lines; SCS 14 s before "by you". [obs]
- Cut rate **peaks early/mid and relaxes at the end**: Zeromatter 120 cuts/min in the first 10 s, SCS 72/min at 0:30-1:00 then 24/min; Rangeview peak 36/min at 0:10-0:20. The highest sustained rate is SendCutSend's 66-72/min for ~30 s (0:30-1:00); Zeromatter's 120/min lasts only the first 10 s. [obs]
- Music: cinematic build/hit/release, mastered loud when the film is a hype piece (SCS -11, Rangeview -14) and moderate for explainers (-16 to -18); interview-led Edison is quiet (-26). [obs]

---

## 4. Applying the house style to Henry's outline

Assumptions [inf]: the video plays after Henry's live ~1 min; the video's V1-V4 timeline from `docs/outline.md` (115 s) is kept; sound is undecided (open question 3). All VO lines below are **drafts in Story's register, for Henry to rewrite**. Square brackets are placeholders for true numbers. Claims must stay within `docs/outline.md` rules (no "state of the art" claim about Zeon, simulation labelled "simulation").

### 4.1 Choose the register
- If there is VO in the video: **poem register** (about 30-45 words/min, i.e. ~60-85 words in 115 s, lines of 3-7 words, 4-5 s gaps). It leaves room for the montage count and the step counter to carry information. If Henry talks live over the video instead, use the **explainer register** (110-120 words/min, Pioneer-style) but then add burned-in captions to the key lines as Pioneer does. [inf]
- Because the opening beat is Henry live (stills, wry "this is state of the art research"), the video should not repeat the setup; it should start with the "sound" going quiet then coming back. [inf]

### 4.2 Beat 0 (live, stills): borrow without adding length
- **Pipetting + off robot (0a)**: hold this still **in near-silence** for 2-3 s before Henry speaks (Rangeview's trough, the "sound faded" beat; Story's films begin from silence: -26 to -39 LUFS). Frame wide with the people in the foreground and the robot dark in the back half, low-key light: practicals only, the robot's deck falling into shadow (mean luma ~0.2, p10 ~0.05). The wryness matches fomo's/Varda's deadpan-undercut-of-grandeur: say it flat. [inf]
- **Coal-mine cage (0b)**: treat like Rangeview's archival images: slow push-in (a few percent over 12 s) on the cage photo, warm-tinted, a "place, year" caption in small letter-spaced type bottom-left ("Bethlehem Steel, Lehigh Valley, PA" style) **only if the source and licence are established** (rights are still unknown per the outline). Keep the line short, e.g. a single declarative with no explanation (Story: "we don't explain things ... so they're more inspirational"). [inf]
- **Handoff (0e)**: a held title still, then music fades up from near silence into V1 (Story's openings). [inf]

### 4.3 Suggested VO phrasing (drafts)
| Video time | Beat | Draft VO (poem register) | Notes |
|---|---|---|---|
| 0:04 | V1 | "Every protocol starts with a pair of hands." | 8 words; concrete noun first; no brand |
| 0:13 | V1 | "[N] videos." | the true count only; read flat, then silence |
| 0:19 | V1 | "[N] ways of doing it." *(optional)* | only if true; else omit |
| 0:25-0:29 | turn | *(no VO; music trough)* | Rangeview-style dip, 4 s |
| 0:29 | V2 | "Same protocol. Nine steps." | verify against the 9 steps |
| 0:37 | V2 | "On the left, hands." | pause 5 s |
| 0:43 | V2 | "On the right, a robot, in simulation." | the label is spoken *and* shown |
| 0:55-1:05 | V2 | *(no VO; let step 9 land; step counter on screen)* | silence before the key moment |
| 1:07 | V3 | "Record it." | triplet, 3 s apart (built/flown/sailed pattern) |
| 1:10 | V3 | "Translate it." | |
| 1:13 | V3 | "Run it." | |
| 1:20 | V3 | "Primitives, not workflows." | from the outline's platform thinking; 3 words |
| 1:33 | V3 | "Every pair of hands, teaching the next." | bookend of the opening "hands" and of Henry's "what if the lab could learn from every pair of hands?" |
| 1:40 | V4 | *(silence 2 s)* then card | |
| 1:45 | V4 | optional tag line: "Next: Vault." | on-screen only is safer |
About 55 spoken words in 115 s = ~29 words/min (Rangeview 30, SCS 44). [inf]

### 4.4 Lighting and grade direction
- **Master grade**: low-key, teal-amber split, grainy. Targets from the film set [obs]: mean luma 0.20-0.29, p10 ~0.05-0.10, p90 ~0.35-0.50, mean HSV saturation 0.33-0.43, 25-45 % near-black pixels. Add film grain and a gentle vignette (Rangeview's "filmic, dirty, grainy" texture), not clean/bright "corporate" lab footage. [inf]
- **Colour-code human vs robot**, as Zeromatter does for the real world vs the sim: left panel (PRISM, humans, hands) **warm amber**, right panel (Zeon sim) **cool cyan** with a persistent small label "ZEON (SIMULATION)" bottom-left for the whole clip, mirroring "MADE IN ZEROMATTER". When real robot footage arrives, change the label and keep the cool grade. [inf]
- **Lab footage lighting**: side/rim light on hands and pipettes, backgrounds falling off to near-black; practical lights visible. Avoid evenly lit white lab walls (high-key). Consider a shallow depth of field and a slow push-in on hands. [inf]
- **AI-generated shots (V3)**: ask the generator for "low-key, single warm practical, cyan fill, 35 mm film grain, shallow depth of field, silhouette against screens" to match; label them as AI-generated as the outline requires. [inf]
- **End card**: black, small wordmark/title in light letter-spaced type, no motion except a slow fade. [obs-derived]

### 4.5 Pacing map for the 115 s cut (and the 90 s cut)
Music levels are short-term LUFS targets relative to a master of about -16 LUFS integrated (Pioneer -16.0, Saronic -16.9, Zeromatter -17.8; SCS and Rangeview are louder at -11 to -14, measured on platform transcodes). Cut rates are from the observed ranges.

| Time | Beat | Cuts/min | Music (short-term LUFS) | VO | Picture |
|---|---|---|---|---|---|
| 0:00-0:04 | V1 open | 0-6 | fade up from -35 to -24 | none | one slow clip of hands (Rangeview opens on a single gesture) |
| 0:04-0:14 | V1 | ramp 30 -> 72 | -22 -> -16 | "Every protocol..." at 0:04 | montage builds; count starts |
| 0:14-0:25 | V1 | 60-72 (SendCutSend sustains 66-72/min for ~30 s; 120/min appears only in Zeromatter's first 10 s) | -16 -> -13 | "[N] videos." at 0:13 | count overlay reaches [N] |
| 0:25-0:29 | turn | 0 | dip to about -28 for 3-4 s | none | black / freeze; title "Same protocol. Twice." in small type |
| 0:29-0:55 | V2 | 12-18 (cuts on step changes; Rangeview 14) | -22 -> -18 | 3 lines at 0:29, 0:37, 0:43 (5-6 s gaps) | split screen warm/cool; step counter 1-9; speed-ramped sim |
| 0:55-1:05 | V2 end | 6-12 | -18, hold | silence | step 9 lands, hold the final frame 2 s |
| 1:05-1:25 | V3 | climb 20 -> 45 | -20 -> -14 | triplet at 1:07/1:10/1:13, then 1:20 | PRISM screens, workflow canvas, AI fills; "N videos -> N protocols" |
| 1:25-1:40 | V3 climax | 36-45 -> 12 | peak -12 to -10 around 1:33, then cut | 1:33 closing line | wall of pages/videos feeding a robot arm (AI-labelled) |
| 1:40-1:42 | drop | 0 | hard fall to <= -30 | none | black |
| 1:42-1:55 | V4 | 0 | silence -> faint tail | optional tag | title card "From Intent to Action: Robotomation", cultivarium.org; hold the wordmark 5-7 s (observed 2-7 s) |
For a **90 s** cut: shorten V1 to ~18 s (drop the 0:14-0:25 plateau), V3 to ~20 s (drop the climax, keep the triplet), end card hold 5 s. [inf]

### 4.6 Top five moves to copy [inf]
1. Start from near-silence, end on near-silence; use one deliberate **trough** at the V1 -> V2 turn.
2. VO of 3-7 words per line with 4-5 s gaps, a triplet in V3, and the second person only at the end.
3. Persistent small "simulation" tag on every sim shot (Zeromatter's `MADE IN ZEROMATTER` precedent).
4. Warm-human vs cool-machine colour code across the side-by-side.
5. Bookend: hands at the start, hands at the end (Zeromatter's "a billion times" -> "a billion lives" and Turba's same-aisle bookend are the precedents).
