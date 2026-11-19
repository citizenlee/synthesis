# Context: what this film is about

Sources: this repo's root `README.md`, `anvil/BRIEF.md`, `anvil/SHOTS.md`, and `research/benchtop-synthesis-landscape/`. Quotes from those files are marked. **[inf]** is inference. **[unverified]** is a claim the repo does not back.

## What the repo is

GitHub: `citizenlee/synthesis`. Description on GitHub: a 46.7 s photorealistic launch film for an automated nucleic acid synthesis factory, and the pipeline that built it.

The root README:

> This is a film, not a product announcement. There is no company called Anvil, no machine, no price list and no quote form. The domain on the end card is literally `YOUR-DOMAIN.COM`. Every number and capability claim in the on-screen copy is a placeholder written to carry the edit, not a specification.

**Synthesis** is the repository (and the working name for the idea). **ANVIL** is the film already in `anvil/` — placeholder brand, placeholder CTA, placeholder domain. This plan is a second film: longer, with VO, in Story's house style. It is about the same idea. It is still a film.

## The idea the film is allowed to state

From `anvil/BRIEF.md` and the root README, in that register (plain claims, concrete nouns, understated — CircuitHub's *Unveiling The Grid* transposed):

1. **An automated nucleic acid synthesis factory**, pictured as pumps, reagent lines, robotic arms, 96-well plates, a hall of cells.
2. **Built in the United States.** Overlay: "Nucleic acid synthesis. Made in America." / "Built here." Film copy, not a plant address. **[unverified]** as a manufacturing claim.
3. **High-mix needs routing, not a fixed line.** "Every plate takes its own route, so 96 different sequences run as easily as 96 of one." The "96" is overlay copy. **[unverified]** as a spec.
4. **Screening lives in the machine.** "No verified screen. No synthesis." NSTM-6 · screening enforced in hardware.

That is the whole argument. There is no throughput number, no chemistry named (phosphoramidite vs enzymatic vs array), no customer, no price, no team.

## The policy it is about

Root README, condensed:

- [NSTM-6](https://www.whitehouse.gov/wp-content/uploads/2026/11/NSTM-6-NASS-Policy.pdf), National Policy for Nucleic Acid Synthesis Screening, issued 5 November 2026.
- Replaces supplier self-attestation with NIST-verified screening.
- Conditions federal research funding on buying from HHS-listed Adherent Suppliers.
- **13 July 2027:** synthetic nucleic acids bought with federal funds must come from an adherent supplier.
- **11 October 2027:** benchtop synthesizers must refuse to run without a valid authorisation from a verified Screener.

The film's subject is that last clause. End-card lockup in ANVIL: "Adherent by design." Treat "adherent" as a policy word (HHS list), not a certification this project holds.

IBBIS (Nov 2026 preliminary findings, now in `research/benchtop-synthesis-landscape/`) is the landscape around that clause: ~280 device models since the 1980s; release rate 3.7 → 9.3 models/year; array-based throughput approaching mail-order scale; no international regulatory consensus; a proposed stack of KYC, per-device authorization, signed jobs, tamper lockout, audit logs. Use it as research. Do not put IBBIS's 1.5 billion nucleotides / 4,350,000 sites on screen unless the line is clearly *their* finding, not ours.

## Audience

The repo never names an audience. **[inf]** from register and subject:

| Likely | Why |
| --- | --- |
| Hardware / manufacturing people | CircuitHub register; pumps, plates, routing |
| Biosecurity and policy | NSTM-6 is the film's stated subject |
| Nucleic-acid synthesis practitioners | the machine class IBBIS surveys |

Not: an ARIA demo slot, a Cultivarium summit audience, or a product waitlist. No event is attached to this plan. If a live intro is used, it is optional (see `outline.md`).

## Existing picture

`anvil/` already locks a machine look: polished concrete, brushed aluminum, black anodized metal, one warm amber accent, no people, no lettering. Ten stills and ten 6 s clips are committed. They are **generated**. If reused, they carry a persistent `GENERATED` tag and stay visually in the "machine / cool" half of the Story grade.

ANVIL's hard rule was **no people in any frame** (models break hands; a biosecurity film should not be sloppy). This longer film *may* show people if they are real and consented. Generated people remain a last resort; if used, no faces that could be mistaken for a real team, no readable badges, no sequences.

## What must not be claimed

| Temptation | Repo fact |
| --- | --- |
| "We built a factory" | There is no machine |
| "We are an Adherent Supplier" | End card is a placeholder |
| "96-plex, no changeover" as a spec | Overlay copy |
| A named chemistry or vendor | Not in the repo |
| Throughput matching mail-order providers | IBBIS finding about *the landscape*, not this film |
| Any specific DNA sequence | Forbidden on screen |
| How to bypass screening | Forbidden; frame the lock, not the hole |
| Cultivarium / PRISM / Zeon / Naval | Different project; do not import |

## Tone

Two registers are already in the house:

- **ANVIL / CircuitHub:** type on picture, no VO, industrial, understated claims.
- **Story poem:** 30–45 wpm, 3–7 word lines, air between lines, name late.

The recommended cut in `outline.md` uses the Story poem register *over* the ANVIL machine. It does not mix poem and explainer in one film. If someone talks live over the picture, switch the whole video to explainer (113–192 wpm) and burn in captions — still one register.

## Open decisions (do not fill by guessing)

- On-screen name: ANVIL, Synthesis, or neither until a domain exists.
- Whether people appear.
- Whether the film is silent-with-type (ANVIL, longer) or VO (Story). Default here: VO.
- Real factory / lab access for documentary footage (none is in the repo).
- Higgsfield credit cap (see `video-tools.md`).
