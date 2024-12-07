#!/usr/bin/env python

with open("../input/2/input") as f:
    grid = [[c for c in lines.strip()] for lines in f.readlines()]

total = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        c = grid[y][x]

        if c != "A":
            continue

        if (len(grid) - 1) > y > 0 and (len(grid[y]) - 1) > x > 0:
            if grid[y - 1][x - 1] == "M" and grid[y + 1][x + 1] == "S":
                if grid[y - 1][x + 1] == "M" and grid[y + 1][x - 1] == "S":
                    print(f"X-MAS at ({y}, {x})")
                    total += 1
                if grid[y - 1][x + 1] == "S" and grid[y + 1][x - 1] == "M":
                    print(f"X-MAS at ({y}, {x})")
                    total += 1
            if grid[y - 1][x - 1] == "S" and grid[y + 1][x + 1] == "M":
                if grid[y - 1][x + 1] == "M" and grid[y + 1][x - 1] == "S":
                    print(f"X-MAS at ({y}, {x})")
                    total += 1
                if grid[y - 1][x + 1] == "S" and grid[y + 1][x - 1] == "M":
                    print(f"X-MAS at ({y}, {x})")
                    total += 1


print("-", [str(i) for i in range(10)])
[print(i, row) for i, row in enumerate(grid)]

print(total)
