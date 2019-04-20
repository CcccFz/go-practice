#!/usr/bin/env bash

# 读取用户信息，向每个用户打招呼，并告诉用户它的ID，最后统计用户数

FILE="/etc/passwd"
SUM=0
for line in `cat $FILE`; do
    name=`echo "$line" | cut -d":" -f1`
    id=`echo "$line" | cut -d":" -f3`
    echo "Hello $name, your id is $id"
    ((SUM++))
done
echo "Total user sum is $SUM"