# Synthesis launch-video plan

A 90–120 second launch/hype film for the idea in this repository, planned the way Cultivarium planned a robot demo video — brief, outline, storylines, shot list, tools, tasks — not as a remake of that demo.

This folder is instructions. No picture is generated until a director pass in `video-tools.md` is approved.

**This is a film plan, not a product announcement.** The repo is explicit: there is no company called Anvil, the domain on the existing end card is `YOUR-DOMAIN.COM`, and every number in the ANVIL overlay is a placeholder. The same rule holds here. Read `context.md` before writing a line of VO.

The silent 46.7 s cut already in `anvil/` is a sibling, not a substitute. Different length, different register (type-only vs sparse VO), different tool stack. Reuse its locked machine look; do not splice its CircuitHub titles over Story-style VO.

## How to use

1. Read [`context.md`](context.md) — what the repo actually claims, who the film is for, what must not be said.
2. Pick a framing in [`storylines.md`](storylines.md) (three alternatives; A is the default behind [`outline.md`](outline.md)).
3. Shoot and generate from [`shotlist.md`](shotlist.md). Real footage first; AI only as a labelled fallback.
4. Assign tools per beat in [`video-tools.md`](video-tools.md). Set a Higgsfield credit cap before anyone generates.
5. Work the open list in [`tasks.md`](tasks.md). Owners are TBD until named.

House style lives in [`references/style-analysis.md`](references/style-analysis.md) (copied from Cultivarium's `ai-summit-2026-demo`; use sections 1–3 only). In one line: poem VO at 30–45 wpm (or explainer at 113–192; pick one), 3–7 word lines, company name late, hinge at 28–60% often with a triplet, low-key teal/amber (warm on people, cool on machines), near-silence that builds then drops under a 5–7 s end card, persistent **simulation** / **generated** tag on any non-documentary shot.

## Hard rules

These extend the ANVIL rules in the root `README.md`. A film about biosecurity should not be sloppy about biosecurity.

- **No real sequence data on screen.** Nucleotide counts only. Never show or describe a specific hazardous sequence, a pathogen, or a misuse path.
- **Safeguards, if shown, are locks not loopholes.** Screening, per-device authorization, signed jobs, audit logs — the NSTM-6 stack, framed as what the machine does. No bypass, no tamper-as-thriller.
- **Do not overstate.** "96 different sequences," "Made in America," "Adherent by design," throughput numbers from IBBIS — all flagged in the outline. If a line needs verification, it stays off-screen or on-screen as qualitative.
- **Label origin.** Generated stills/clips: small `GENERATED` tag. Any simulation: small `SIMULATION` tag, persistent, Zeromatter-style. Do not mix documentary and generated in one shot.
- **No generated text in the picture.** Models garble lettering. Type is composited in post (as ANVIL already does).
- **On-screen name is a decision.** ANVIL is the existing film's placeholder brand. Synthesis is the repo. Do not lock a wordmark until someone picks.

## Layout

```
video/
  README.md                 this file
  context.md                what Synthesis is, from the repo; audience; constraints
  outline.md                recommended 90–120 s cut, beat-by-beat
  storylines.md             three alternative framings with draft VO
  shotlist.md               real capture specs + AI prompts
  video-tools.md            director, generators, music, edit, costs
  tasks.md                  open to-dos (owners TBD)
  references/
    style-analysis.md       Story house style (source: Cultivarium ai-summit-2026-demo)
```

Working media (not committed): `footage/raw/`, `music/`, `out/` — see `.gitignore`.

## What this is not

- Not a reshoot of ANVIL. That film is done at 46.7 s, no people, no VO.
- Not Cultivarium positioning (no Naval line, no PRISM/Zeon, no "intent to action").
- Not a claim that a factory exists, that screening is already in hardware, or that any vendor is a partner.
