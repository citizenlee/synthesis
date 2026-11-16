#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
FPS=24; ENC="-c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -r $FPS"

# 1. trim each shot to its cut length
trim () { # clip in dur out
  ffmpeg -y -v error -ss "$2" -i "clips/$1.mp4" -t "$3" \
    -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1" \
    -an $ENC "segs/$4.mp4"
}
trim 01-floor     0.25 4.8 01
trim 09-hero      0.40 4.4 02
trim 02-arm       0.30 4.3 03
trim 03-pumps     0.25 3.9 04
trim 04-fluid     0.40 3.4 05
trim 05-seat      0.30 3.9 06
trim 08-interlock 0.40 4.0 07
trim 06-head      0.30 3.9 08
trim 07-fill      0.20 5.6 09
trim 10-scale     0.25 4.3 10

# 2. the end card: the hero shot, darkened, with the lockup over it
ffmpeg -y -v error -ss 1.6 -i clips/09-hero.mp4 -loop 1 -i titles/07-endlockup.png -t 4.2 \
  -filter_complex "[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,\
eq=brightness=-0.26:saturation=0.55:contrast=0.92,gblur=sigma=7[bed];\
[1:v]format=rgba,fade=t=in:st=0.15:d=0.5:alpha=1[lk];\
[bed][lk]overlay=0:0[v]" -map "[v]" -an $ENC segs/11.mp4

# 3. concat
: > segs/list.txt
for i in 01 02 03 04 05 06 07 08 09 10 11; do echo "file '$PWD/segs/$i.mp4'" >> segs/list.txt; done
ffmpeg -y -v error -f concat -safe 0 -i segs/list.txt -c copy out/cut.mp4

# 4. type over the footage
ffmpeg -y -v error -i out/cut.mp4 \
  -loop 1 -i titles/01-name.png -loop 1 -i titles/02-route.png \
  -loop 1 -i titles/03-nochange.png -loop 1 -i titles/04-screen.png \
  -loop 1 -i titles/05-built.png \
  -filter_complex "\
[1:v]format=rgba,fade=t=in:st=1.3:d=0.35:alpha=1,fade=t=out:st=4.95:d=0.35:alpha=1[o1];\
[0:v][o1]overlay=0:0:enable='between(t,1.3,5.3)'[v1];\
[2:v]format=rgba,fade=t=in:st=9.6:d=0.35:alpha=1,fade=t=out:st=13.05:d=0.35:alpha=1[o2];\
[v1][o2]overlay=0:0:enable='between(t,9.6,13.4)'[v2];\
[3:v]format=rgba,fade=t=in:st=17.7:d=0.35:alpha=1,fade=t=out:st=21.15:d=0.35:alpha=1[o3];\
[v2][o3]overlay=0:0:enable='between(t,17.7,21.5)'[v3];\
[4:v]format=rgba,fade=t=in:st=25.0:d=0.35:alpha=1,fade=t=out:st=28.25:d=0.35:alpha=1[o4];\
[v3][o4]overlay=0:0:enable='between(t,25.0,28.6)'[v4];\
[5:v]format=rgba,fade=t=in:st=38.5:d=0.35:alpha=1,fade=t=out:st=41.85:d=0.35:alpha=1[o5];\
[v4][o5]overlay=0:0:enable='between(t,38.5,42.2)'[v5];\
[v5]fade=t=in:st=0:d=0.6[vout]" \
  -map "[vout]" -t 46.7 $ENC out/titled.mp4

# 5. score
ffmpeg -y -v error -i out/titled.mp4 -i audio/score.mp3 \
  -filter_complex "[1:a]atrim=0:46.7,afade=t=in:st=0:d=1.0,afade=t=out:st=44.4:d=2.3,volume=0.85[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest out/anvil.mp4

ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_type,width,height,r_frame_rate -of default=nw=1 out/anvil.mp4
