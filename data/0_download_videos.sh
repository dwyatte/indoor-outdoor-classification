#!/bin/sh

mkdir -p indoor/video outdoor/video

# indoor
for url in `grep -v \# indoor.txt`
do
    youtube-dl -o 'indoor/video/%(title)s.%(ext)s' $url
done

# outdoor
for url in `grep -v \# outdoor.txt`
do
    youtube-dl -o 'outdoor/video/%(title)s.%(ext)s' $url
done