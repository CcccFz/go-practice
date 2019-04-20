#!/bin/bash
function show
{
    echo $1$2
}

show 'ww' 'ss'

i=0
((i++))
echo $i

let i++
echo $i

expr $i + 1
echo $i

