# Synthesis

This repository holds a nucleic-acid-synthesis idea explored as a film, not as a company. What exists today is **ANVIL**: a 46.7-second photorealistic launch film for a machine that does not exist, plus the generative pipeline that built it.

Also in this repo:

- [Benchtop nucleic acid synthesis device landscape (IBBIS, Nov 2026)](research/benchtop-synthesis-landscape/) — whitepaper, text extraction, thread figures, and notes from [Tessa Alexanian's X thread](https://x.com/tessafyi/status/2122982286085800338).
- [Launch-video plan](video/) — a 90–120 s Story-style cut with VO, distinct from the silent ANVIL film.

---

# ANVIL

A 46.7-second photorealistic launch film for a machine that does not exist.

`anvil/out/anvil.mp4` — 1920×1080, 24 fps, 27 MB.

**This is a film, not a product announcement.** There is no company called Anvil, no
machine, no price list and no quote form. The domain on the end card is literally
`YOUR-DOMAIN.COM`. Every number and capability claim in the on-screen copy is a
placeholder written to carry the edit, not a specification. Read it as a film.

---

## What it is

An automated nucleic acid synthesis factory, built in the United States, that enforces
screening in hardware: no verified screen, no synthesis. Pumps, reagent lines, robotic
arms, 96-well plates. No people in any frame, no dialogue, no narration.

The register is borrowed from CircuitHub's
[Unveiling The Grid](https://www.circuithub.com/post/unveiling-the-grid) — plain claims,
concrete nouns, understated — cut with launch-film pacing. The argument it makes is
CircuitHub's argument transposed: high-mix production needs routing, not a fixed line.
Every plate takes its own route, so 96 different sequences run as easily as 96 of one.

### The policy it is about

[NSTM-6](https://www.whitehouse.gov/wp-content/uploads/2026/11/NSTM-6-NASS-Policy.pdf),
the National Policy for Nucleic Acid Synthesis Screening, was issued 5 November 2026. It
replaces supplier self-attestation with NIST-verified screening and conditions federal
research funding on buying from HHS-listed Adherent Suppliers. By 13 July 2027 all
synthetic nucleic acids bought with federal funds must come from an adherent supplier; by
11 October 2027 benchtop synthesisers must refuse to run without a valid authorisation
from a verified Screener. That last clause is the film's subject: screening that lives in
the machine rather than in a checkbox.

---

## Pipeline

| Step | Tool | Script |
| --- | --- | --- |
| Shot stills — locks the machine's look | OpenAI GPT Image 2.6 | `bin/gen_plates.py`, `bin/gen_wides.py` |
| Still → moving clip | MiniMax Hailuo 02 (image-to-video, 6 s, 1080P) | `bin/gen_clips.py`, `bin/regen.py` |
| Score | ElevenLabs Music | `bin/gen_music.py` |
| Type and end card | Python + PIL | `bin/titles.py` |
| Edit and mix | ffmpeg | `bin/assemble.sh` |

Each shot is generated as a still first, then animated from that still. The still is where
the machine's design gets decided and corrected; the video step only adds motion. That
split is what makes a bad shot cheap to fix — reword one prompt in `SHOTS.md`, regenerate
one still, regenerate one clip, re-run the assembly.

### Reproducing it

```sh
export OPENAI_API_KEY=...        # stills
export MINIMAX_API_KEY=...       # image-to-video
export ELEVENLABS_API_KEY=...    # score

cd anvil
python3 bin/gen_plates.py        # 10 stills  -> plates/
python3 bin/gen_clips.py         # 10 clips   -> clips/
python3 bin/gen_music.py         # 48 s score -> audio/score.mp3
python3 bin/titles.py            # 7 overlays -> titles/
bash  bin/assemble.sh            # cut + type + mix -> out/anvil.mp4
```

The generation scripts cache by output filename, so a re-run only fills gaps. Image
generation costs real money per call; the committed `frames/`, `clips/` and `audio/` let
you re-cut the film without spending any.

`bin/assemble.sh` alone rebuilds the edit from what is already committed.

---

## Rules the film holds to

These exist because generative models break them by default, and because a film about
biosecurity should not be sloppy about biosecurity.

- **No people in any frame.** No hands, no operators, no reflections of people.
- **No generated text anywhere.** Models garble lettering. Every word on screen is
  composited in `bin/titles.py` over footage that contains none.
- **No real sequence data on screen.** Orders are nucleotide counts only.
- **No invented specifications.** Where the copy needs a claim it stays qualitative, and
  the end card's domain and call to action are left visibly as placeholders.

## Layout

```
anvil/
  BRIEF.md      the film's brief: subject, register, stack, hard rules
  SHOTS.md      10 shots, cut lengths, the full image prompt for each, overlay copy, music prompt
  bin/          the pipeline, one script per step
  frames/       the 10 selected stills, as fed to the video model
  clips/        the 10 generated clips, 6 s each at 1080P
  titles/       composited type overlays, transparent PNG
  audio/        the score
  fonts/        League Gothic, Archivo Black, IBM Plex Mono (OFL)
  out/anvil.mp4 the film
```

`SHOTS.md` is the single source for any shot. Changing a shot means changing its prompt
there first.

## Known open items

- The domain and the "Request a quote" call to action are placeholders.
- The score was generated and measured at −14.5 LUFS integrated, not auditioned.
- Shots 01 and 10 are on their second generation. The first pair read as nonsense —
  sealed cabinets with no loading ports, a gantry over an empty aisle, an endless
  corridor. Both prompts in `SHOTS.md` are now the mechanically specific replacements.
