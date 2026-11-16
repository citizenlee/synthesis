import os, json, base64, urllib.request, concurrent.futures as cf, pathlib

KEY = os.environ["OPENAI_API_KEY"]
MODEL = "gpt-image-2.6-sunburst"
SIZE = "1536x1024"
OUT = pathlib.Path(__file__).resolve().parent.parent / "plates"
OUT.mkdir(exist_ok=True)

STYLE = (" Photorealistic, cinematic, shot on 35mm, shallow depth of field. Palette: polished "
         "concrete grey, brushed aluminum, black anodized metal, one warm amber accent. Cool "
         "industrial key light from upper left, soft fill, gentle atmospheric haze. "
         "No people, no hands, no text, no lettering, no logos, no signage.")

SHOTS = {
 "01-floor": "Cinematic wide shot inside a modern American biotechnology manufacturing hall. Two rows of tall brushed aluminum automated synthesis cabinets line a polished concrete floor, each with a dark glass window lit faintly from inside. An overhead linear gantry rail runs the length of the hall. High clerestory daylight, deep perspective down the centre aisle.",
 "02-arm": "Close medium shot of an industrial robotic gantry arm gripping a clear plastic 96-well microplate by its short edges, moving it through a stainless steel automation enclosure. Precise servo joints, black anodized linear rails, brushed aluminum, a small amber status LED.",
 "03-pumps": "Extreme close-up of a bank of six peristaltic pump heads in an industrial fluid handling system. Three-roller rotors compress translucent silicone tubing; clear fluid visible in the lines. Stainless manifold, machined aluminum housing, knurled fittings.",
 "04-fluid": "Extreme macro of clear colourless reagent flowing through transparent tubing into a stainless steel manifold block. Visible meniscus, tiny bubbles in the line, refraction and caustics through the liquid. A precision solenoid valve body beside it. Cold clinical light.",
 "05-seat": "An industrial robot gripper lowering a clear 96-well microplate onto a machined aluminum deck nest inside an automated instrument. The plate seats precisely into the nest. Cool white interior lighting, visible precision linear rails.",
 "06-head": "An eight-channel precision dispense head descending over a clear 96-well microplate inside an automated liquid handling instrument. Eight polished stainless steel tips aligned exactly over one column of wells. Machined aluminum, precision linear bearings.",
 "07-fill": "Extreme macro, near top-down, of a clear 96-well microplate being filled column by column with clear liquid from an eight-channel dispense head. Each filled well holds a bright meniscus catching the light. Filled columns glisten; the remaining wells are dry and matte.",
 "08-interlock": "Close-up of a machined stainless steel safety interlock on an industrial instrument: a solid steel bolt seated in its receiver, with a round amber indicator lamp beside it in a knurled bezel. Brushed metal, cool light, crisp mechanical detail.",
 "09-hero": "Cinematic product hero shot of a large brushed aluminum automated nucleic acid synthesis machine standing on polished concrete in a clean industrial facility. Dark glass window, precision machined panels, visible reagent bottles and bundled tubing, a robotic arm inside. Dramatic key light from upper left, deep soft shadows, one amber accent.",
 "10-scale": "Wide shot down a long hall of identical brushed aluminum automated synthesis machines in an American manufacturing facility. Polished concrete floor, overhead gantry rail, cool daylight haze, strong repetition and sense of scale.",
}

def gen(item):
    name, prompt = item
    dest = OUT / f"{name}.png"
    if dest.exists() and dest.stat().st_size > 50000:
        return name, "cached"
    body = json.dumps({"model": MODEL, "prompt": prompt + STYLE, "size": SIZE, "n": 1}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=body,
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            d = json.load(r)
        dest.write_bytes(base64.b64decode(d["data"][0]["b64_json"]))
        return name, f"ok {dest.stat().st_size//1024}KB"
    except Exception as e:
        detail = getattr(e, "read", lambda: b"")()
        return name, f"FAIL {e} {detail[:160]}"

with cf.ThreadPoolExecutor(max_workers=10) as ex:
    for name, status in ex.map(gen, SHOTS.items()):
        print(f"{name:14} {status}")
