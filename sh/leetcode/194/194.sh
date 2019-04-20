#!/usr/bin/env bash

# LeetCode 193

IFS_old=$IFS
IFS=$'\n'

num=0
array1=()
array2=()
for line in `cat file.txt`; do
    array1+=(`echo $line | awk '{print $1}'`)
    array2+=(`echo $line | awk '{print $2}'`)
done

echo ${array1[*]}
echo ${array2[*]}

IFS=$IFS_old