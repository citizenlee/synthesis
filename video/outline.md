# Outline: Synthesis launch film (90–120 s)

**Shape:** optional ~60 s live intro, then a **90–120 s** film. Default below is **110 s**, poem register. Spoken draft is ~55 words in 110 s ≈ **30 wpm** (Rangeview 30, SendCutSend 44). Lines 3–7 words.
**Default framing:** Storyline A in `storylines.md` (routing), with the NSTM-6 lock as the second movement. Not the IBBIS landscape film (that's B).
**Rule:** film, not product. Placeholder numbers stay flagged. Generated and simulated shots stay tagged. No sequence data, no misuse.

Legend: **REAL** = capture. **GEN** = AI, labelled `GENERATED`. **ANVIL** = existing generated clips in `anvil/clips/`, still labelled `GENERATED`. **GAP** = not available yet.

---

## Timeline at a glance

| Part | Time | Length | Content |
| --- | --- | --- | --- |
| Optional live intro | before the film | ~60 s | talking points only; Henry's words to write |
| V0 quiet open | 0:00–0:08 | 8 s | one mechanism, near silence |
| V1 catalog / wait | 0:08–0:28 | 20 s | the old way: one order, one queue |
| **Hinge** | 0:28–0:34 | 6 s | music trough; "So every plate takes its own route." |
| V2 high-mix machine | 0:34–1:05 | 31 s | arm, pumps, fill — routing, not a line |
| V3 the lock | 1:05–1:28 | 23 s | interlock; screening in hardware |
| V4 close | 1:28–1:38 | 10 s | "Built here." then fall |
| End card | 1:38–1:50 | 12 s | 5–7 s of near-silent card inside this hold |
| **Film total** | | **110 s** | Limit 90–120. 90 s cut: drop V1 to 12 s and V3 to 16 s |

---

## Optional live intro (~60 s)

Not required. Use only if the film plays after a person in a room. Talking points, not a script to memorize. Rewrite.

| Slot | Time | Picture | Talking points |
| --- | --- | --- | --- |
| 0a | 0:00–0:12 | Still: a 96-well plate, or ANVIL frame 07 (fill), no type | This is a film. The machine does not exist. What it is *about* does. |
| 0b | 0:12–0:28 | NSTM-6 title page, or a plain date card: 5 Nov 2026 | National Policy for Nucleic Acid Synthesis Screening. Federal funds → adherent suppliers by July 2027. Benchtops refuse a run without a verified authorization by October 2027. |
| 0c | 0:28–0:45 | ANVIL frame 01 (hall) or IBBIS device-format figure | High-mix synthesis is a routing problem, not a fixed line. CircuitHub's argument, on plates. |
| 0d | 0:45–1:00 | Holding card: project name TBD, no domain unless real | "What follows is a launch film for a factory that has not been built. Watch it as a film." |

Do not use the live minute to preview VO lines. Do not show sequences. Do not claim adherence.

---

## Beat-by-beat (110 s film)

VO is draft, poem register, 3–7 words per line. Rewrite. Square brackets = do not speak until verified.

| Time | Visual | VO line | Audio | Real vs generated |
| --- | --- | --- | --- | --- |
| 0:00–0:08 | Extreme macro, one peristaltic roller on tubing. Slow. No type. Cool grade. | *(none)* | Near silence, −35 LUFS, room tone / a single click of a roller | **ANVIL** `03-pumps` or **REAL** macro if captured. Tag if generated. |
| 0:08–0:14 | A sealed mailer / cold-pack on a bench, or a queue of identical plates in a hotel. Warm if a hand is real; otherwise cool. | "Orders used to wait." | Music fades in, −28 → −22 | **REAL** preferred (any lab mailer, no vendor logo). **GEN** fallback: `shotlist.md` S-A1. |
| 0:14–0:22 | One plate riding a straight conveyor, one destination. | "One plate. One line." | −22 | **ANVIL** `01-floor` (gantry hall) or **REAL**. |
| 0:22–0:28 | Cut rate up: three plates, same nest, same motion. | "Then a changeover." | −18, slight tension | **ANVIL** `05-seat` repeated / **REAL**. |
| **0:28–0:34 HINGE (31%)** | Cut to black 0.4 s, then a plate choosing a branch — a diverter, a second nest, a second head. Small type (composited): EVERY PLATE TAKES ITS OWN ROUTE. | "Every plate takes its own route." | Dip to ~−30 LUFS for 3–4 s, then lift. Rangeview trough. | **GEN** or **ANVIL** `02-arm` if the arm clearly traverses *across* cells. No readable sequence. |
| 0:34–0:42 | Gantry arm carrying a plate laterally. Cool machine, amber LED only. | *(silence 4–5 s)* | Climb −22 → −18 | **ANVIL** `02-arm`. |
| 0:42–0:46 | Pump bank, fluid in lines. | "Pumps." | −16 | **ANVIL** `03-pumps`. |
| 0:46–0:50 | Macro reagent into a manifold. | "Plates." | −16 | **ANVIL** `04-fluid`. |
| 0:50–0:54 | Eight-channel head descends. | "Routes." | −15 | **ANVIL** `06-head`. |
| 0:54–0:58 | Same head, still descending. | "Different sequences." **[do not say "ninety-six" — ANVIL overlay, unverified as a spec]** | −14 | **ANVIL** `06-head` continued. |
| 0:58–1:02 | Hold on the head, or start of fill. | "No changeover." | −13 | **ANVIL** `06-head` / `07-fill`. |
| 1:02–1:05 | **Payoff:** wells fill column by column. Hold. | *(none)* | Peak-adjacent −12, then hold | **ANVIL** `07-fill` or **REAL** plate-fill (water, not reagents labelled as DNA). |
| 1:05–1:10 | Interlock bolt, amber lamp. Slow push. | "No verified screen." | Brief dip −20 | **ANVIL** `08-interlock`. |
| 1:10–1:16 | Same bolt seated. Optional composited type: NSTM-6 · PER-DEVICE AUTHORIZATION. No crypto jargon on screen. | "No synthesis." | −16 | **ANVIL** `08-interlock` continued. |
| 1:16–1:22 | Quiet UI-less detail: a log line as *motion* (a reel, a light that stays on), not readable sequence text. | "The run leaves a record." | −14 | **GEN** S-C4 (audit-log-as-object). Never show a sequence in the log. |
| 1:22–1:28 | Hero machine, product light. | *(silence)* | −12 | **ANVIL** `09-hero`. |
| 1:28–1:34 | Three machines, service gaps, ordinary ceiling. Pull back. | "Built here." **[unverified as a plant claim; keep as register, or drop]** | Start of fall −12 → −20 | **ANVIL** `10-scale`. |
| 1:34–1:38 | Black. | *(none)* | Hard fall ≤ −30 | — |
| 1:38–1:50 | End card: small letter-spaced wordmark (name TBD), one line "Adherent by design" **or** omit until the word is earned, no fake domain. Hold 5–7 s of the card itself. | *(none)* | Near silence, −36 | Composited plate, as ANVIL `titles/07-endlockup.png` — **replace domain and CTA**. No "Request a quote" until a quote path exists. |

**On-screen type (composited, never generated in-camera)**

| At | Line | Notes |
| --- | --- | --- |
| 0:30 | EVERY PLATE TAKES ITS OWN ROUTE | hinge; ANVIL already has this line |
| 1:08 | NO VERIFIED SCREEN. NO SYNTHESIS. | ANVIL already has this line |
| 1:12 | NSTM-6 | small, mono; policy name only |
| 1:38 | wordmark + one line | name TBD; no `YOUR-DOMAIN.COM` |

Do not put IBBIS statistics on screen. Do not put "1.5 billion nucleotides" anywhere.

---

## 90 s cut

Drop 0:14–0:22. Shorten V3 to interlock + "No verified screen. / No synthesis." (drop the audit-log beat). End card hold 5 s. Keep the hinge at ~0:26 (still ~29% of 90 s).

## Grade, tags, biosecurity

- Master: low-key, mean luma ~0.20–0.29, teal/amber, grain, vignette. Cool on machines; if a real hand appears, warm that shot only.
- Persistent small `GENERATED` on every ANVIL clip and every new AI shot (bottom-left, IBM Plex Mono, Story/Zeromatter precedent).
- If any simulation of software appears: `SIMULATION` on that shot for its full duration.
- No people unless **REAL** and consented. No AI faces.
- No well maps, FASTA, chromatograms, or "order IDs" that look like sequences.
- Screening is a closed bolt and a quiet record — not a hacked cabinet.

## Music

Instrumental, 100–110 bpm, industrial pulse (ANVIL's ElevenLabs brief is a starting point; default for this cut is Suno Pro — see `video-tools.md`). Near-silence open, trough at the hinge, peak under the fill (~1:00), fall under the card. No vocals.

## Honesty pass before export

- [ ] No sequence characters on screen
- [ ] Every generated clip tagged
- [ ] "96" not presented as a measured spec
- [ ] No live domain, no fake quote CTA
- [ ] NSTM-6 dated only if the date is on a card we control
- [ ] Runtime 90–120 s
- [ ] End card 5–7 s, near silent
