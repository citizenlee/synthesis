import os, json, base64, time, urllib.request, pathlib, sys

KEY = os.environ["MINIMAX_API_KEY"]
ROOT = pathlib.Path(__file__).resolve().parent.parent
FR, CL = ROOT/"frames", ROOT/"clips"; CL.mkdir(exist_ok=True)
API = "https://api.minimax.io/v1"
H = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

MOTION = {
 "01-floor": "Slow steady dolly forward down the centre aisle of the hall. Faint haze drifts in the light shafts. Machines idle with subtle internal movement. Locked horizon, no camera shake.",
 "02-arm": "The robotic gantry arm glides smoothly to the right carrying the microplate, camera tracks laterally with it. Precise servo motion, constant speed.",
 "03-pumps": "The peristaltic pump rotors turn steadily and the tubing compresses in sequence as clear fluid moves through the lines. Slow push in.",
 "04-fluid": "Clear liquid flows through the transparent tube, small bubbles travelling along the line. The solenoid valve actuates once with a crisp mechanical movement. Camera locked with slight drift.",
 "05-seat": "The gripper lowers the microplate and seats it precisely into the aluminum nest, then releases. Slow push in at deck level.",
 "06-head": "The eight-channel dispense head descends steadily toward the microplate, the stainless tips approaching one column of wells. Camera follows the head down.",
 "07-fill": "Clear liquid dispenses into the wells column by column, bright menisci forming and catching the light as each column fills. Slow push in.",
 "08-interlock": "The solid steel bolt slides across and locks with a crisp mechanical movement. The amber indicator lamp brightens. Slow push in.",
 "09-hero": "Slow cinematic orbit around the machine, key light sweeping across the brushed aluminum panels. The arm inside moves subtly behind the glass.",
 "10-scale": "Slow camera pull back revealing more identical machines receding down the long hall. Haze and light shafts, steady motion.",
}

def post(path, payload):
    req = urllib.request.Request(API+path, data=json.dumps(payload).encode(), headers=H)
    with urllib.request.urlopen(req, timeout=180) as r: return json.load(r)

def get(path):
    req = urllib.request.Request(API+path, headers={"Authorization": f"Bearer {KEY}"})
    with urllib.request.urlopen(req, timeout=120) as r: return json.load(r)

tasks = {}
for name, motion in sorted(MOTION.items()):
    dest = CL/f"{name}.mp4"
    if dest.exists() and dest.stat().st_size > 100000:
        print(f"{name:14} cached"); continue
    b64 = base64.b64encode((FR/f"{name}.jpg").read_bytes()).decode()
    try:
        d = post("/video_generation", {
            "model": "MiniMax-Hailuo-02",
            "prompt": motion,
            "first_frame_image": f"data:image/jpeg;base64,{b64}",
            "duration": 6, "resolution": "1080P",
        })
        tid = d.get("task_id")
        if tid: tasks[name] = tid; print(f"{name:14} submitted {tid}")
        else:   print(f"{name:14} NO TASK {json.dumps(d)[:200]}")
    except Exception as e:
        print(f"{name:14} SUBMIT FAIL {e} {getattr(e,'read',lambda:b'')()[:200]}")
    time.sleep(14)

(ROOT/"clips"/"tasks.json").write_text(json.dumps(tasks, indent=1))
print(f"\n{len(tasks)} tasks submitted; polling\n", flush=True)

pending = dict(tasks); done = {}
deadline = time.time() + 2100
while pending and time.time() < deadline:
    time.sleep(20)
    for name, tid in list(pending.items()):
        try: st = get(f"/query/video_generation?task_id={tid}")
        except Exception as e: print(f"  {name} poll err {e}"); continue
        s = st.get("status")
        if s == "Success":
            done[name] = st["file_id"]; pending.pop(name)
            print(f"  {name:14} ready ({st.get('video_width')}x{st.get('video_height')})", flush=True)
        elif s in ("Fail", "Failed"):
            pending.pop(name); print(f"  {name:14} FAILED {json.dumps(st)[:200]}", flush=True)

if pending: print("TIMED OUT still pending:", list(pending))

for name, fid in done.items():
    try:
        u = get(f"/files/retrieve?file_id={fid}")["file"]["download_url"]
        urllib.request.urlretrieve(u, CL/f"{name}.mp4")
        print(f"{name:14} downloaded {(CL/f'{name}.mp4').stat().st_size//1024}KB")
    except Exception as e:
        print(f"{name:14} DOWNLOAD FAIL {e}")
