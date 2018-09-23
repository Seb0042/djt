#!/bin/bash
export LANG=en_US.UTF-8
env > b.log
#/data/djt/ls/get_file.py "$1" "$2"
echo cat radio.txt "$2"
cat radio.txt >> "$2"
sync
cp radiot.txt "$2"
echo bidule > test_fin
exit 0
