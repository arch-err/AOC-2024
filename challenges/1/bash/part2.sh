#!/usr/bin/env bash

input="../input/2/input"

grep -oP "^\d+" $input | sort > tmp1
grep -oP "\d+$" $input | sort > tmp2

tot=0
for i in $(seq $(cat tmp1 | wc -l))
do
	i1=$(sed -n "$i"p tmp1)
	i2=$(sed -n "$i"p tmp2)
	n=$(grep "$i1" tmp2 | wc -l)

	sc=$(( $i1 * $n ))
	tot=$((tot+$sc))
done

rm tmp*
echo $tot
