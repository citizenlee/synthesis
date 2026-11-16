# ANVIL — photorealistic launch film

**Deliverable:** ~45 s, 1920x1080, photorealistic generated footage, original score, no people,
no dialogue, no lip sync. Type and the end card composited in post, never generated.

**Subject:** Anvil, an automated nucleic acid synthesis factory built in the United States.
Pumps, reagent lines, robotic arms, and 96-well plates. NSTM-6 screening enforced by the
machine itself: no verified screen, no synthesis.

**Register:** CircuitHub's "Unveiling The Grid" — plain claims, concrete, understated — cut with
launch-film energy. The argument: high-mix synthesis needs routing, not a fixed line. Every
plate takes its own route, so 96 different sequences run as easily as 96 of one. And it is made
here.

**Stack (all keys already present)**
| Step | Tool |
| --- | --- |
| Shot stills (locks the machine's look) | OpenAI GPT Image 2.6 |
| Still -> moving clip | MiniMax Hailuo 02 (image-to-video) |
| Score | ElevenLabs Music |
| Type, end card, assembly | PIL + ImageMagick + ffmpeg |

**Not used:** HyperFrames (dropped by request). slopcore (a music-video pipeline; wrong shape,
and no Seedance key). Codex (a coding agent; it cannot generate video).

**Hard rules**
- No people in any frame. No hands, no operators, no reflections of people.
- No generated text anywhere. Models garble it. Every word on screen is composited.
- No real sequence data on screen. Orders are nucleotide counts only.
- Product claims and numbers are placeholders until verified. Marked as such in the overlay copy.
