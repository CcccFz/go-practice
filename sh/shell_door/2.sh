#!/usr/bin/env bash

# 读取2.txt的内容，将字母转换为大写，并把数字的位置交换

while read line; do
    echo $line | tr [:lower:] [:upper:] | sed -r 's/([0-9]{3})([A-Z]{3})([0-9]{3})/\3\2\1/'
done