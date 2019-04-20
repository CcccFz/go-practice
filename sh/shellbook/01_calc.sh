#!/bin/bash

i=0
while [ $i -lt 100 ]
do
    ((i++))
done

echo $i

dir=$(ps fax)
echo $dir

A=(1 2 this)
echo ${A[0]} ${A[2]}

alls[0]=Be
alls[1]=Bee
alls[2]=Beee
echo ${alls[2]}

declare -a tf
echo ${#alls[*]}

echo $opid


if test -f $1
then
    pr $1
elif
    test -d $1
then
    (cd $1;ls)
else
    echo $1 is neither a file nor a directory
fi

while ［ $reply!="y" ］ && [ $reply!="Y" ]                         #下面将学习的循环语句
do
    echo "\nAre you want to continue?(Y/N)\c"
    read reply             #读取键盘
    case $replay in
        (y|Y) break;;         #退出循环
        (n|N) echo "\n\nTerminating\n"
              exit 0;;
           *) echo "\n\nPlease answer y or n"
              continue;       #直接返回内层循环开始出继续
    esac
done

bc
