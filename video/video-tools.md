# Video tools (per beat)

Method adapted from Cultivarium's robot-demo plan. Different picture, different stack from ANVIL (`anvil/` used GPT Image 2.6 → MiniMax Hailuo 02 → ElevenLabs Music → ffmpeg). This cut prefers the Higgsfield path so a director agent can iterate drafts. **Prices below are notes from that project as of 18 Nov 2026. Check at purchase. Do not treat them as quotes.**

Real footage preferred. AI is a labelled fallback.

## Director / planner

| Role | Tool | Notes |
| --- | --- | --- |
| Shot list, prompts, review | **Claude Fable 5.2** with [Higgsfield MCP](https://mcp.higgsfield.ai/mcp) | Preferred. Writes prompts, calls generators, does not render video itself. |
| Alternate director | **GPT-6.2 Astra** | Higgsfield plugin in ChatGPT (no audio there) or ffmpeg/Remotion in a coding agent. API video output unsupported (as of that note). |

Give the agent `context.md`, `outline.md`, `shotlist.md`, and `references/style-analysis.md` sections 1–3. Constraints in the brief: no vendor logos, no readable text, no sequences, no people unless the shot is tagged REAL, label GENERATED, Higgsfield credit cap (below).

Neither Fable nor Astra generates the picture. They only direct.

## Picture

| Step | Tool | When |
| --- | --- | --- |
| Look-lock stills | **Midjourney** or **Higgsfield** image | New shots in `shotlist.md` section C. Match `anvil/frames/`. |
| Existing machine | **Reuse ANVIL** | `anvil/frames/` + `anvil/clips/` already paid for. |
| Motion, drafts | **Seedance 2.5** via Higgsfield, **480p** | 4–30 s clips; draft then discard. |
| Motion, finals | **Seedance 2.5** 4K, or **Kling 4.0** via Higgsfield | Keepers only. |
| Optional motion | **Wan 3.0** | Optional; not required. |
| Upscale | **SeedVR2** | If a keeper lands below 1080p. |
| Real capture | Camera, 24 fps, 1080p or 4K | `shotlist.md` section A. |

ANVIL's Hailuo 02 clips are already 1080p. Do not re-generate them unless the grade cannot be matched in the new edit.

## Sound and type

| Step | Tool | When |
| --- | --- | --- |
| Score | **Suno Pro** | Instrumental, ~2 min, 100–110 bpm. Brief in `outline.md`. Commercial rights: only while subscribed (per that project's notes) — confirm on Suno's current terms. |
| Alternate score | ANVIL `anvil/audio/score.mp3` | 48 s, too short; loop/extend only if it still falls quiet under the card. Prefer a new 2 min bed. |
| VO record | Real voice, or none | Poem register is sparse enough to record in one pass. Do not generate a celebrity voice. |
| Type / end card | PIL (`anvil/bin/titles.py` as a pattern) or DaVinci titles | Fonts in `anvil/fonts/`. Never generate lettering in-camera. |
| Mix | ffmpeg or DaVinci Resolve | LUFS targets in the pacing map below. |

## Edit

| Tool | Use |
| --- | --- |
| **ffmpeg** | Cuts, tags, loudness (`ebur128`), assemble. ANVIL's `anvil/bin/assemble.sh` is the pattern for a scripted cut. |
| **DaVinci Resolve** | Grade (teal/amber), grain, the trough at the hinge, end-card hold. Prefer Resolve if a person is colouring; ffmpeg if the cut stays in repo. |

Output: 1920×1080 or 3840×2160, 24 fps, ~90–120 s, mix near −16 LUFS integrated (Story explainers; ANVIL was louder, −14.5 measured on its score — pick one and stick to it).

## Tools per beat (110 s cut)

| Beat | Picture | Sound | Type |
| --- | --- | --- | --- |
| V0 0:00–0:08 | ANVIL `03-pumps` or R1 | silence → −35 | none |
| V1 0:08–0:28 | R2/R3 or S-A1 + ANVIL `01-floor` / `05-seat` | Suno fade in | none |
| Hinge 0:28–0:34 | S-A2 or ANVIL `02-arm` | trough −30 | composited route line |
| V2 0:34–1:05 | ANVIL 02, 03, 04, 06, 07 (or R4) | climb to −12 | none (VO only) |
| V3 1:05–1:28 | ANVIL `08-interlock` + S-C4 | dip then hold | NSTM-6, composited |
| V4 + card | ANVIL `09-hero` / `10-scale` | fall to −36 | wordmark, 5–7 s |

Storyline B swaps in S-B1, S-B2, S-B3 and needs more new generation (budget for it). Storyline C swaps in S-C5.

## Cost notes (check at purchase)

Figures from the Cultivarium notes, 18 Nov 2026, plus ANVIL's own stack. **Unverified here. Re-check.**

| Item | Note (as of 18 Nov 2026, not a quote) |
| --- | --- |
| Higgsfield | Paid plan required. Generations consume credits. Third-party list: Ultra ~129 EUR/mo (99 EUR yearly) with 3,000 credits. **No native spend cap** — the agent must be told a number. 72-hour trial mentioned then had expired. |
| Seedance 2.5 / Kling 4.0 / Wan 3.0 | Priced in Higgsfield credits. Kling and some upscalers were unverified in those notes. |
| Per-clip ballpark | One maker ~$1.17–4.40 per 720p clip via evolink (36 clips ~$63). A 4:04 Slopcore piece was **$88.08** all-in (Suno + gpt-image + Seedance + SeedVR2 + Claude). Arithmetic on 6–10 clips: roughly **$7–44** — estimate, not a quote. |
| Suno Pro | $10/mo ($8 annual) / 2,500 credits noted then; Premier $30/mo. Confirm current plan. |
| Fable 5.2 | $8 / $40 per million tokens (Anthropic docs, that note). Small next to generation; plan allowance burns fast. |
| Midjourney | Separate subscription if stills go that way. |
| SeedVR2 | Higgsfield or standalone; confirm. |
| ANVIL reuse | Already paid. `assemble.sh` rebuilds that film at $0. |

**Fewer new shots = lower cost.** Default 110 s cut reuses ten ANVIL clips and adds **2–4** new ones (mailer, branch, audit-log object). Storyline B is the expensive variant.

## Higgsfield credit budget

Higgsfield will not stop you. Put a cap in the director brief, for example:

> Do not spend more than **800 credits** without asking. Draft every new shot at 480p. Re-render at 4K only after a written keep list. Reuse `anvil/clips/` instead of regenerating the machine.

Replace 800 with whatever the live balance and plan allow. Log actual spend in `tasks.md` when it happens.

## Spend rule

Any paid generation needs an explicit yes from the repo owner (Henry). Do not run Higgsfield, Midjourney, Suno, or SeedVR2 on an assumption.
