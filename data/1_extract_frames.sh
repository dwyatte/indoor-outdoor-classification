#!/bin/sh

extract_frames_from_video () {
    # skip first and last $skip seconds to minimize intro/outro frames
    skip=.15
    duration=`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$1"`
    ss=`echo "($duration * $skip) / 1" | bc`
    t=`echo "($duration - $ss) / 1" | bc`
    hash=`cat "$1" | md5`
    extension="${1##*.}"
    tmpfile=/tmp/$hash.$extension 
    ffmpeg -y -i "$1" -ss $ss -t $t -codec copy $tmpfile < /dev/null
    # extract $frames linearly spaced frames to maximize variance
    frames=100
    fps=`echo "($t - $ss) / $frames" | bc`
    ffmpeg -y -i $tmpfile -vf fps=1/$fps -vframes $frames "$2/$hash-%03d.png" < /dev/null
}

mkdir -p indoor/frames outdoor/frames

indoor
find indoor/video -type f -print0 | while IFS= read -r -d '' video
do
   extract_frames_from_video "$video" indoor/frames
done
outdoor
find outdoor/video -type f -print0 | while IFS= read -r -d '' video
do
    extract_frames_from_video "$video" outdoor/frames
done
