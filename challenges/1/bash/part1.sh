#!/usr/bin/env bash

input="../input"

grep -oP "^\d+" $input | sort > tmp1
grep -oP "\d+$" $input | sort > tmp2

tot=0
for i in $(seq $(cat tmp1 | wc -l))
do
	i1=$(sed -n "$i"p tmp1)
	i2=$(sed -n "$i"p tmp2)
	distance=$(( $i2 - $i1 ))
	distance=${distance#-} # Absolute value of distance
	tot=$((tot+$distance))
done
echo $tot
