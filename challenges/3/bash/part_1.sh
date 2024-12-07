#!/usr/bin/env bash

input="../input/1/input"

echo $(( "$(cat $input | grep -oP 'mul\(\d+,\d+\)' | perl -pe 's/mul\(//g; s/,/*/g; s/\)\n/ + /')0" ))
