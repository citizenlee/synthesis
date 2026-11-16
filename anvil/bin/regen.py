import os, json, base64, time, urllib.request, pathlib
KEY = os.environ["MINIMAX_API_KEY"]; ROOT = pathlib.Path(__file__).resolve().parent.parent
API = "https://api.minimax.io/v1"; H = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}
JOBS = {
 "01-floor": "Slow steady dolly forward alongside the conveyor track. A microplate carrier advances smoothly along the rail toward the open transfer port. Faint haze in the light. Locked horizon, no camera shake.",
 "10-scale": "Slow steady push in toward the three machines. Subtle mechanical movement behind the open loading ports, tubing hanging still. Light shifts gently across the brushed panels. No camera shake.",
}
def post(p, d):
    r = urllib.request.Request(API+p, data=json.dumps(d).encode(), headers=H)
    return json.load(urllib.request.urlopen(r, timeout=180))
def get(p):
    r = urllib.request.Request(API+p, headers={"Authorization": f"Bearer {KEY}"})
    return json.load(urllib.request.urlopen(r, timeout=120))
tasks = {}
for name, motion in JOBS.items():
    b64 = base64.b64encode((ROOT/"frames"/f"{name}.jpg").read_bytes()).decode()
    d = post("/video_generation", {"model":"MiniMax-Hailuo-02","prompt":motion,
        "first_frame_image":f"data:image/jpeg;base64,{b64}","duration":6,"resolution":"1080P"})
    if d.get("task_id"): tasks[name]=d["task_id"]; print(f"{name:10} submitted {d['task_id']}", flush=True)
    else: print(f"{name:10} NO TASK {json.dumps(d)[:160]}", flush=True)
    time.sleep(14)
pend = dict(tasks); done = {}; end = time.time()+1800
while pend and time.time() < end:
    time.sleep(20)
    for n, t in list(pend.items()):
        try: st = get(f"/query/video_generation?task_id={t}")
        except Exception: continue
        if st.get("status") == "Success": done[n]=st["file_id"]; pend.pop(n); print(f"  {n} ready", flush=True)
        elif st.get("status") in ("Fail","Failed"): pend.pop(n); print(f"  {n} FAILED", flush=True)
for n, fid in done.items():
    u = get(f"/files/retrieve?file_id={fid}")["file"]["download_url"]
    urllib.request.urlretrieve(u, ROOT/"clips"/f"{n}.mp4")
    print(f"{n:10} downloaded {(ROOT/'clips'/f'{n}.mp4').stat().st_size//1024}KB")
