#!/usr/bin/env bash

echo "1: $1"
echo "2: $2"
echo "3: $3"
echo $#
echo $*
echo $@

VAR="Hello ChengDU!"
echo ${#VAR}
echo ${VAR:6:5}
echo ${VAR:(-1)}
echo ${VAR:(-3):2}

VAR="xiao 11gou gou"
#echo ${VAR//gou/mao}
#echo ${VAR/gou/mao}
#echo ${VAR//gou/}
#echo ${VAR//gou/}
echo ${VAR//[0-9]/}

URL="http://www.baidu.com/baike/user.html"
#echo ${URL##*/}
#echo ${URL##*//}
#echo ${URL%.*}
#echo ${URL%%.*}

#while true; do
#    select mysql_version in 5.1 5.6; do
#        echo $mysql_version
#        break
#    done
#done # bash
i=0
while true; do
   ((i++))
done

trap "func" 2
func() {
    read -p "Term(Y/N)" input
    if [ "$input" == "Y" ]; then
        exit
    fi
}
for i in {1..10}; do
    echo $i
    sleep 1
done