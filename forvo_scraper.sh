#!/bin/bash
# Forvo scraper

BASEURL="http://forvo.com/search/"
AUDIOURL="http://audio.forvo.com/audios/mp3/"
word=$1
lang=$2

path="data/pronunciation/${lang}/${word}.mp3"
url="${BASEURL}${word}/${lang}"

if test ! -f "$path"; then
    file="$(wget -qO- "${url}" | grep 'onclick="Play(' | head -1 | sed "s/^.*Play(.*,'\([^']*\)','[^']*',.*$/\1/g" | base64 -d)"
    mkdir -p "data/pronunciation/${lang}"
    echo "Download to ${path}..."
    wget -qO "$path" "${AUDIOURL}${file}"
fi