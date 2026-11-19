# Shot list

Real footage first. AI only where the real shot cannot be captured, always labelled `GENERATED` (and `SIMULATION` if it is a software sim). ANVIL clips in `anvil/clips/` are already generated — reuse is allowed; they still get the tag.

No readable text in any generated frame. No logos. No sequence characters (A/C/G/T runs, FASTA, chromatograms). No people in generated shots unless a last-resort extra, and then no identifiable face, no badge, no lab notebook with writing. Water in wells, not labelled DNA.

Shared grade for new stills and clips: photorealistic, 35 mm, shallow depth of field, low-key; polished concrete grey, brushed aluminum, black anodized metal, one warm amber accent; cool key from upper left; gentle haze; film grain. Warm only on real hands.

---

## A. Real footage to capture

None of this exists in the repo today. Capture is optional — the 110 s cut can be assembled entirely from ANVIL + new AI — but real material should replace generated B-roll wherever it lands.

| ID | Beat | Shot | Spec | Why |
| --- | --- | --- | --- | --- |
| R1 | V0 / V2 | Peristaltic pump macro | 4K or 1080p, 24 fps, 8–12 s, locked with micro drift. Rollers compressing clear tubing, colourless fluid. No brand name in frame. | Replaces ANVIL `03-pumps` if a real instrument is available. |
| R2 | V1 | Mailer / cold-pack on a bench | Photo min 12 MP and/or 8 s clip. A sealed insulated mailer or plate shipment, no vendor print. Hands optional, consented. Warm practical. | "Orders used to wait." Documentary, not a product shot. |
| R3 | V1 | Plate hotel / queue | Wide, 16:9, chest height. Identical microplates in a rack. Empty hallway OK. | The old line. |
| R4 | V2 payoff | Wells filling | Top-down macro, 24 fps, 10 s. Colourless liquid, column by column if possible. Water is fine. No well labels with sequences. | Real version of ANVIL `07-fill`. |
| R5 | V3 | Interlock / status lamp | Close-up of a real instrument door lock, status LED, or keyed switch. No readable firmware screen. | Real version of ANVIL `08-interlock`. |
| R6 | V4 | Hall / three instruments | Wide of a real automation suite or empty high-bay. Ordinary ceiling. Do not imply it is "our" factory. | Scale without the endless-corridor failure mode ANVIL already hit. |
| R7 | optional live 0a | Single plate still | Photo, 16:9. One 96-well plate, dark bench, no writing on the skirt. | Live-intro still. |
| R8 | any | Consent + scrub | If people appear: written consent; hide unpublished screens, notebook pages, sample IDs. | Biosecurity and privacy. |

Do not film another company's synthesizer and imply it is this project. Generic fluidics and plates are enough.

---

## B. Reuse from ANVIL (already generated)

All 6 s / 1080p, `anvil/clips/`. Tag `GENERATED`. Cut lengths in `anvil/SHOTS.md`.

| Clip | Use in 110 s cut | Notes |
| --- | --- | --- |
| `03-pumps.mp4` | V0 open, V2 | Best quiet open |
| `01-floor.mp4` | V1 line | Second-generation wide; keep |
| `05-seat.mp4` | V1 changeover | |
| `02-arm.mp4` | hinge / V2 | Lateral traverse = routing |
| `04-fluid.mp4` | V2 | Macro reagent; colourless |
| `06-head.mp4` | V2 | Eight-channel |
| `07-fill.mp4` | V2 payoff | |
| `08-interlock.mp4` | V3 | The lock |
| `09-hero.mp4` | V3/V4 | Product light |
| `10-scale.mp4` | V4 | Second-generation; not an infinite corridor |

Stills in `anvil/frames/` are the look-lock. New AI shots should match them, not reinvent the machine.

---

## C. AI-generated shots (gaps)

Director writes final prompts; these are ready to paste into Seedance 2.5 (image-to-video after a still) or Kling 4.0 via Higgsfield. Still first (Midjourney or Higgsfield image), then motion. Draft at 480p, keepers at 4K.

**Negative (append to every prompt):** `no people, no hands, no faces, no text, no lettering, no logos, no signage, no DNA sequence letters, no FASTA, no helix cartoon, no pathogen, no biohazard symbol, no infinite corridor, no endless repetition`

### S-A1 — mailer on a bench (V1 fallback)

**Still (Midjourney / Higgsfield):**
> Photorealistic documentary photograph, 35 mm, of a sealed unbranded insulated lab mailer sitting on a dark epoxy bench. Soft warm practical from the left, rest of the room falling to black. No logos, no labels, no barcodes, no readable text. Low-key, film grain, 16:9.

**Motion (Seedance 2.5 / Kling 4.0, 6 s):**
> Slow 3% push-in on the mailer. Dust in the light. Nothing else moves. Camera locked otherwise.

### S-A2 — plate choosing a branch (hinge)

**Still:**
> Photorealistic industrial photograph of a waist-height stainless conveyor carrying one clear 96-well plate in a black carrier. The track splits: two open instrument bays, brushed aluminum, each with a rectangular transfer port. Ordinary ceiling, cable trays, one amber LED. No people, no text, no logos. Photorealistic, cinematic, 35 mm, shallow depth of field. Palette: polished concrete grey, brushed aluminum, black anodized metal, one warm amber accent.

**Motion:**
> The plate carrier rolls forward and takes the left branch into a transfer port. Slow, precise, no sudden cuts. Camera dollies with it.

### S-B1 — small benchtop synthesizer (storyline B)

**Still:**
> Photorealistic product photograph of a small unbranded benchtop nucleic acid synthesizer on a lab bench, about the size of a microwave, dark glass window, reagent bottles with unmarked frosted glass, bundled tubing. No logos, no screens with text, no people. Low-key teal-amber grade, 35 mm.

**Motion:**
> Slow orbit, 15 degrees. Interior amber LED pulses once. No text on the glass.

### S-B2 — floor-standing cell beside a bench (storyline B)

**Still:**
> Photorealistic documentary photograph of a lab: in the foreground a small benchtop instrument, in the background a tall floor-standing automation cell, same brushed-aluminum language, clear service gap, ordinary industrial ceiling. Shows scale from bench to hall. No people, no text, no logos.

**Motion:**
> Slow pull back until both machines read. No new objects.

### S-B3 — array as many sites, not a sequence (storyline B)

**Still:**
> Extreme macro, photorealistic, of a synthesis array: a grid of tiny wet sites catching light, like a dark microarray under a single cool key. Abstract, no letters, no well IDs, no DNA cartoon. Shallow depth of field, film grain.

**Motion:**
> Micro drift. Highlights crawl across the grid. No text fading in.

### S-C4 — audit log as an object (V3)

Do **not** generate a computer screen of sequences. Make it physical.

**Still:**
> Photorealistic close-up of a small industrial status printer or event recorder in a machine cabinet: a narrow strip of unprinted paper feeding, a single amber lamp, brushed metal bezel, cable gland. No readable characters on the paper. Low-key, 35 mm.

**Motion:**
> The blank strip advances one click. Lamp stays on. Camera locked.

### S-C5 — authorization as a key (storyline C)

**Still:**
> Photorealistic macro of a machined stainless key or cryptographic token seated in a lock on an instrument panel, amber LED beside it in a knurled bezel. Engraved marks illegible. No logos, no text. Cool key light.

**Motion:**
> The token seats. LED eases on. Slow 2% push-in.

### S-X — do not generate

- Any specific oligonucleotide or gene.
- A "blocked" order with a sequence on screen.
- Tamper, screwdriver in a cabinet, bypass.
- A map of China vs USA as a scoreboard.
- People operating a synthesizer (capture real, or omit).
- Vendor-lookalikes (no Twist, IDT, DNA Script, Kilobaser, etc. silhouettes).

---

## D. Type and end card

Composited in post (PIL or Resolve titles), never in-camera. ANVIL fonts are in `anvil/fonts/` (League Gothic, Archivo Black, IBM Plex Mono, OFL). End card: replace `YOUR-DOMAIN.COM` and "Request a quote" with a wordmark and one line, or leave the domain off.

## E. Counts

Target **6–10 new generated clips** if ANVIL is reused; keep about half after the draft pass. If ANVIL is *not* reused, that is a full 10-shot reshoot — budget accordingly (`video-tools.md`).
