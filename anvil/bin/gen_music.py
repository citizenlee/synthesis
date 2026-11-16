import os, json, urllib.request, pathlib

KEY = os.environ["ELEVENLABS_API_KEY"]
OUT = pathlib.Path(__file__).resolve().parent.parent / "audio"; OUT.mkdir(exist_ok=True)

PROMPT = ("Instrumental score for a modern American manufacturing launch film. Low mechanical "
          "percussion and a steady machine-like pulse, precise and restrained. A cold synth bed "
          "with metallic textures. Holds back through the middle, then opens into one bright, "
          "confident swell, and resolves clean and quiet at the end. Cinematic, industrial, "
          "serious, forward-driving. 100 bpm. Absolutely no vocals, no singing, no voices.")

body = json.dumps({"prompt": PROMPT, "music_length_ms": 48000}).encode()
req = urllib.request.Request("https://api.elevenlabs.io/v1/music", data=body,
    headers={"xi-api-key": KEY, "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=600) as r:
        data = r.read()
        ct = r.headers.get("Content-Type", "")
    dest = OUT / ("score.mp3" if "mpeg" in ct or "mp3" in ct else "score.bin")
    dest.write_bytes(data)
    print(f"ok {dest} {len(data)//1024}KB content-type={ct}")
except Exception as e:
    print("FAIL", e, getattr(e, "read", lambda: b"")()[:300])
