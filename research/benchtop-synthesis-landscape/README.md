# Benchtop nucleic acid synthesis device landscape (IBBIS, Nov 2026)

Source thread: [Tessa Alexanian (@tessafyi), Nov 18, 2026](https://x.com/tessafyi/status/2122982286085800338)
Whitepaper: ["The Benchtop Nucleic Acid Synthesis Device Landscape: Preliminary Findings"](https://ibbis.bio/wp-content/uploads/2026/11/benchtop_synthesis_landscape.pdf), v1.0, 13 Nov 2026. Authors: Ivet A. Yordanova, Kirsten Engel, Mayra Ameneiros, Gary Abel, Tessa Alexanian (IBBIS, SecureDNA Foundation, Fourth Eon Biosecurity, Johns Hopkins CHS).

Files here: the PDF, a `pdftotext` extraction (`.txt`), and the thread images (`fig-*.jpg/png`).

## Thread claims
- Release rate of new benchtop devices "3x'd" comparing 2006–2015 vs 2016–2025.
- 50% of *active manufacturers* are in China (17/35).
- Some "benchtops" are large floor-standing devices (small benchtop → large benchtop → floor-standing).
- Chemistry is diversifying: beyond column/well phosphoramidite, now enzymatic, assembly-focused and array-based benchtop devices. Array-based used to be internal to big synthesis providers only.

## Whitepaper findings
**Landscape**
- ~280 device models introduced since the early 1980s; 102 discontinued; 27 in development.
- Release rate: 3.7 models/yr (2006–2015) → 9.3 models/yr (2016–2025), i.e. ~2.5x (thread rounds to 3x).
- Manufacturer HQs in 11 countries. Share of device *models*: China 31.8%, USA 25%, Japan 11.8%, EU total 16.8%. (Thread's 17/35 counts *active manufacturers*, a different denominator.)
- Capacity derivable for 83 models (197 not derivable from public specs).

**Chemistry / formats**
- Phosphoramidite: conventional column/well, or array-based (electrochemical, droplet deposition, photolithographic deprotection, other localized reactions).
- Enzymatic: engineered terminal deoxynucleotidyl transferase (TdT).
- "Other" / undisclosed, incl. assembly-focused.
- Array-based devices have the highest throughput: up to 1.5 billion unique nucleotides across up to 4,350,000 sites per run. Benchtop throughput now approaches mail-order provider scale.

**Biosecurity / governance**
- No international regulatory requirements or consensus best practices for benchtop biosecurity.
- US National Policy for Nucleic Acid Synthesis Screening (NSTM-6, 5 Nov 2026) sets obligations for device manufacturers and calls for technical standards for on-device screening, including form, issuance, cryptographic verification, physical security and validity of authorizations issued to individual devices.
- Proposed layered safeguards:
  - KYC at purchase/transfer, plus ongoing verification via proprietary consumables (reagents, kits, cartridges).
  - Operator-device: unique user auth, tiered licensing, MFA, cryptographic credentials / e-signatures; KYC sets default tier.
  - Software: networked "phone-home" authorization (protect proprietary sequences) or offline screening (protect databases/updates).
  - Hardware: secure boot with hardware root of trust so firmware/controllers for fluidics, thermal, electronics execute only signed jobs; tamper detection triggering lockout.
  - Record-keeping: audit logs for attribution and automated reporting of tamper attempts.

**Data access**: full dataset on request via managed access (dataaccess@ibbis.bio). Full report, dataset and analysis scripts (GitHub) promised later.

## Reactions in thread
- Jacques Thibodeau (@JacquesThibs) quote: after a month studying cloud labs, "things are moving much faster than many scientists realize," and incentives plus AI will accelerate the reconfiguration.
- Fadi Hassan: some "benchtops" wouldn't fit on a bench with a microscope on it.

## Possible uses for Synthesis
- Device/vendor landscape baseline (request the IBBIS dataset for model-level data).
- Design input if building or integrating synthesis hardware: plan for NSTM-6 compliance (per-device authorization, signed jobs, audit logs, KYC).
- Watch the full report for the manufacturer map and safeguard comparison.

## Implications for Synthesis

Grounded in this repository (`README.md`, `anvil/BRIEF.md`, `anvil/SHOTS.md`) and the IBBIS findings above. No product, company, or specification is added here.

**The film and the landscape are about the same object.** This repo's ANVIL cut is a film, not a product announcement: there is no company called Anvil, and every number in the overlay is a placeholder. Its subject is an automated nucleic acid synthesis factory, built in the United States, that refuses to run without a verified screen. The repo already states NSTM-6 (5 Nov 2026) conditions federal-funded purchases on HHS-listed Adherent Suppliers by 13 July 2027, and requires benchtop synthesizers to refuse a run without a valid authorization from a verified Screener by 11 October 2027. IBBIS cites that same policy as the first national obligation on device manufacturers, and calls for standards on the form, issuance, cryptographic verification, physical security, and validity of per-device authorizations. The film's line "No verified screen. No synthesis." is that October 2027 clause in CircuitHub register, not a shipped interlock.

**Floor-standing cells sit inside IBBIS's "benchtop" category.** The survey runs from small research instruments to floor-standing production synthesizers. The ANVIL hall of synthesis cells is a cinematic floor-standing reading of that range, not a separate class of machine.

**High-mix routing rhymes with array-scale throughput; they are not the same claim.** The film argues, after CircuitHub, that high-mix production needs routing, not a fixed line: every plate takes its own route, so 96 different sequences run as easily as 96 of one. IBBIS finds array-based benchtop devices now reach up to 1.5 billion unique nucleotides across up to 4,350,000 sites per run — throughput approaching mail-order provider scale. Those statements rhyme (many sequences, one run). The film's "96" is overlay copy, not a spec. Do not treat either figure as a Synthesis capability.

**"Built here" is copy, not a market map.** Overlay and end card say "Made in America" / "Built here." IBBIS's manufacturer HQs: China 31.8% of device models, USA 25%, Japan 11.8%, EU 16.8% (the thread's 17/35 counts active manufacturers, a different denominator). The copy is a register choice. The map is the landscape. Do not collapse them.

**If hardware is ever designed, IBBIS's safeguard stack is the positive frame this repo already points at:** KYC, per-device authorization, signed jobs (secure boot / hardware root of trust), tamper lockout, audit logs. The film already holds: no real sequence data on screen; orders as nucleotide counts only; screening as a lock, not a loophole. Do not depict hazardous sequences, misuse, or bypass. Request the IBBIS dataset (`dataaccess@ibbis.bio`) for a model-level baseline before any vendor or chemistry choice; the full report is promised later.

**Nothing in this repo says a machine is being built.** Use the landscape as research. Keep the film a film.

## Key references cited
- Langenkamp, *Securing benchtop DNA synthesizers*, IFP (2024): https://ifp.org/securing-benchtop-dna-synthesizers
- NTI, *Benchtop DNA Synthesis Devices: Capabilities, Biosecurity Implications, and Governance* (2023)
- Forget et al., evolving TdT for commercial enzymatic DNA synthesis, NAR 53 (2025), doi:10.1093/nar/gkaf115
- Baker & Church, *Protein design meets biosecurity*, Science 383:349 (2024)
