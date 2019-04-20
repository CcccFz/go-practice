#!/usr/bin/env bash

# LeetCode 192

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'
