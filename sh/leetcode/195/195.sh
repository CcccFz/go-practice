#!/usr/bin/env bash

# LeetCode 195

head -n 10 file.txt | awk 'END{if(NR==10){print $0}}'