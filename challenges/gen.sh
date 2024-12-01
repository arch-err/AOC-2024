#!/usr/bin/env bash

for i in $(seq 2 24)
do
	mkdir $i
	cd $i

	echo "# Day $i:

## Part 1
<++>

### Solves
- []()

## Part 2
<++>

### Solves
- []()" > README.md

	mkdir -p input/1
	mkdir -p input/2
	touch input/1/input_test
	touch input/2/input_test
	cd -
done
