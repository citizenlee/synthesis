import os, json, base64, urllib.request, concurrent.futures as cf, pathlib

KEY = os.environ["OPENAI_API_KEY"]
OUT = pathlib.Path(__file__).resolve().parent.parent/"plates"/"wides"; OUT.mkdir(parents=True, exist_ok=True)

STYLE = (" Photorealistic documentary photograph of a real working facility, shot on 35mm. "
         "Palette: polished concrete grey, brushed aluminum, black anodized metal, one warm "
         "amber accent. Cool industrial light, gentle haze. Believable engineering, realistic "
         "human scale, ordinary industrial ceiling. No people, no hands, no text, no lettering, "
         "no logos, no signage, no infinite corridor, no endless repetition.")

CANDS = {
 "w1-line": "Interior of a working pharmaceutical automation suite. A waist-height stainless steel conveyor track runs through the centre of frame carrying clear 96-well microplates in black carriers. Along the left side, four open-front instrument bays in a brushed aluminum frame, each with a rectangular transfer port where a plate enters the machine. On the right, plate hotel racks loaded with microplates. Overhead cable carrier track and a linear rail with a carriage. Exposed ducting and strip lighting on a normal ceiling.",
 "w2-cell": "A single robotic work cell in an industrial laboratory, seen three-quarter from the front. A six-axis robot arm on a pedestal reaches into an open-fronted brushed aluminum instrument to place a clear 96-well microplate. Plate hotels and stacked carriers beside it. Safety fencing of black posts and clear polycarbonate panels around the cell. Concrete floor with faded painted lane markings, utility conduit overhead.",
 "w3-row": "Three identical brushed aluminum automated synthesis machines standing side by side with clear service gaps between them in a working industrial room. Each has an open loading port with a microplate carrier at it and bundled tubing entering from above. Utility conduit and cable trays run across a normal industrial ceiling. Polished concrete floor, a service trolley to one side, a solid wall behind with electrical panels.",
 "w4-floor": "Wide view across a modest manufacturing floor in a converted industrial building. Two automated synthesis cells in the middle distance with open loading ports, a stainless transfer conveyor between them, reagent drums on a rack, and an overhead linear gantry on a single rail spanning only the working area, not the whole room. Brick and painted steel structure, clerestory windows high on one wall only, concrete floor.",
}

def gen(item):
    name, prompt = item
    dest = OUT/f"{name}.png"
    body = json.dumps({"model": "gpt-image-2.6-sunburst", "prompt": prompt+STYLE,
                       "size": "1536x1024", "n": 1}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=body,
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=600) as r: d = json.load(r)
        dest.write_bytes(base64.b64decode(d["data"][0]["b64_json"]))
        return name, f"ok {dest.stat().st_size//1024}KB"
    except Exception as e:
        return name, f"FAIL {e} {getattr(e,'read',lambda:b'')()[:160]}"

with cf.ThreadPoolExecutor(max_workers=4) as ex:
    for n, s in ex.map(gen, CANDS.items()): print(f"{n:10} {s}")
