#!/usr/bin/env bash

# LeetCode 193

IFS_old=$IFS
IFS=$'\n'

FILE="words.txt"
for line in `cat "$FILE"`; do
    echo $line | grep -P "^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$"
done

IFS=$IFS_old