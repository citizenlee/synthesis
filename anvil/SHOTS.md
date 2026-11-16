# ANVIL — shot list and prompt book

10 shots. Each: one still from GPT Image, then image-to-video. Durations are target cut lengths,
not generation lengths; generate longer and cut in.

Shots 01 and 10 use a stricter suffix, after the first pair of wides came back incoherent:
> Photorealistic documentary photograph of a real working facility, shot on 35mm. [palette as
> below] Believable engineering, realistic human scale, ordinary industrial ceiling. No people,
> no hands, no text, no lettering, no logos, no signage, no infinite corridor, no endless
> repetition.

Shared style suffix appended to every image prompt:
> Photorealistic, cinematic, 35mm, shallow depth of field. Palette: polished concrete grey,
> brushed aluminum, black anodized metal, one warm amber accent. Cool industrial key light from
> upper left, soft fill, gentle haze. No people, no hands, no text, no logos, no signage.

| # | Cut | Shot | Camera |
| --- | --- | --- | --- |
| 01 | 5.0 s | Wide hall of synthesis cells, overhead gantry rail | slow dolly forward |
| 02 | 4.5 s | Robotic gantry arm gripping a 96-well plate, traversing | lateral track |
| 03 | 4.0 s | Bank of peristaltic pump heads turning, fluid in tubing | slow push in |
| 04 | 3.5 s | Macro: reagent through clear tubing into a steel manifold | locked, micro drift |
| 05 | 4.5 s | Gripper seats a plate onto a machined deck nest | deck-level push |
| 06 | 4.5 s | Eight-channel dispense head descends over the plate | low, follow down |
| 07 | 6.0 s | **PAYOFF** wells fill column by column | top-down macro, slow |
| 08 | 4.0 s | Interlock bolt engages, amber indicator lights | slow push in |
| 09 | 5.0 s | Hero: the whole machine, product-shot lighting | slow orbit |
| 10 | 4.0 s | Pull back: the hall, scale and repetition | pull back |

## Overlay copy (composited, not generated)

| At | Line | Treatment |
| --- | --- | --- |
| 02.0 s | ANVIL | League Gothic caps, 190 px, centre-left |
| 03.4 s | Nucleic acid synthesis. Made in America. | mono 30 px under the wordmark |
| 10.0 s | Every plate takes its own route. | Archivo Black 96 px, two lines |
| 17.5 s | 96 different sequences. No changeover. | Archivo Black 88 px |
| 27.0 s | No verified screen. No synthesis. | Archivo Black 96 px, amber rule under line 2 |
| 28.5 s | NSTM-6 · screening enforced in hardware | mono 28 px |
| 38.0 s | Built here. | Archivo Black 104 px |
| 42.0 s | end card: anvil mark + ANVIL + Adherent by design + CTA | composited plate |

## Image prompts

**01 floor** *(replacement — the first version read as nonsense: sealed cabinets with no loading ports and a gantry over an empty aisle)* — Interior of a working pharmaceutical automation suite. A waist-height stainless steel conveyor track runs through the centre of frame carrying clear 96-well microplates in black carriers. Along the left side, four open-front instrument bays in a brushed aluminum frame, each with a rectangular transfer port where a plate enters the machine. On the right, plate hotel racks loaded with microplates. Overhead cable carrier track and a linear rail with a carriage. Exposed ducting and strip lighting on a normal ceiling.

**02 arm** — Close medium shot of an industrial robotic gantry arm gripping a clear plastic 96-well microplate by its short edges, moving it through a stainless steel automation enclosure. Precise servo joints, black anodized rails, brushed aluminum, a small amber status LED.

**03 pumps** — Extreme close-up of a bank of six peristaltic pump heads in an industrial fluid handling system. Three-roller rotors compress translucent silicone tubing; clear fluid is visible in the lines. Stainless manifold, machined aluminum housing, fine knurled fittings.

**04 fluid** — Extreme macro of clear colourless reagent flowing through transparent tubing into a stainless steel manifold block. Visible meniscus, tiny bubbles, refraction and caustics through the liquid. A precision solenoid valve body beside it. Cold clinical light.

**05 seat** — An industrial robot gripper lowering a clear 96-well microplate onto a machined aluminum deck nest inside an automated instrument. The plate seats precisely into the nest. Cool white interior lighting, visible linear rails.

**06 head** — An eight-channel precision dispense head descending over a clear 96-well microplate inside an automated liquid handling instrument. Eight polished stainless tips align exactly over one column of wells. Machined aluminum, precision linear bearings.

**07 fill** — Extreme macro, near top-down, of a clear 96-well microplate being filled column by column with clear liquid from an eight-channel dispense head. Each well holds a bright meniscus catching the light. Filled columns glisten; empty wells are dry and matte.

**08 interlock** — Close-up of a machined stainless steel interlock on an industrial instrument: a solid steel bolt seated in its receiver, with a round amber indicator lamp beside it in a knurled bezel. Engraved but illegible machine markings, brushed metal, cool light.

**09 hero** — Cinematic product hero shot of a large brushed aluminum automated nucleic acid synthesis machine standing on polished concrete in a clean industrial facility. Dark glass window, precision machined panels, visible reagent bottles and tubing bundles, a robotic arm inside. Dramatic key from upper left, deep soft shadows, one amber accent.

**10 scale** *(replacement — the first version was an infinite corridor of identical machines)* — Three identical brushed aluminum automated synthesis machines standing side by side with clear service gaps between them in a working industrial room. Each has an open loading port with a microplate carrier at it and bundled tubing entering from above. Utility conduit and cable trays run across a normal industrial ceiling. Polished concrete floor, a service trolley to one side, a solid wall behind with electrical panels.

## Music

ElevenLabs Music, ~48 s: tense industrial pulse, low mechanical percussion and a rising
synth bed, restrained through the middle, opening up at the plate fill, resolving clean under
the end card. 100 bpm. No vocals.

## Motion prompts (image-to-video)

Each still is animated with MiniMax Hailuo 02 at 6 s / 1080P. The motion prompt never
introduces new objects — it only says how the camera and the existing mechanism move.
See `bin/gen_clips.py` for all ten and `bin/regen.py` for the two replacements.
