#!/usr/bin/env bash

input="../input/2/input"

funcRegex="(mul\(\d+,\d+\)|do(n't)?\(\))"

calcString="$(cat $input | perl -pe "s/\n//g" | grep -oP $funcRegex | perl -pe "s/\n/ /g" | perl -pe "s/don't\(\) .*? do\(\) //g" | perl -pe "s/ do\(\)//g; s/mul\(//g; s/,/*/g; s/\)/ +/g; s/ don.*//")0"

echo $(( $calcString ))
