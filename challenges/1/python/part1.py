#!/usr/bin/env python

with open("../input/1/input", "r") as f:
    lines = f.readlines()

c1 = []
c2 = []
tot = 0

for line in lines:
    c1.append(int(line.split(" ")[0]))
    c2.append(int(line.split(" ")[3].replace("\n", "")))

c1.sort()
c2.sort()

for i in range(len(c1)):
    tot += abs(c2[i] - c1[i])

print(tot)
