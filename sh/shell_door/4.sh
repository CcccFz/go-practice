#!/usr/bin/env bash

# 向/var目录下的每个文件，子目录，递归子目录打招呼

SUM=0
cd /var
for line in `ls /var/*`; do
    echo "hello $line"
    ((SUM++))
done