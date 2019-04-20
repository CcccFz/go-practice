#!/usr/bin/env bash

# 读取1.txt的内容，转化为所需要的格式

awk '{
    if(NR==1) {
        sum=$1;
        next;
    }
    print sum;
    print $0;
    sum+=$2;
}'


