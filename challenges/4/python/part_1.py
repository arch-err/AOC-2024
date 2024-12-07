#!/usr/bin/env python

with open("../input/1/input") as f:
    grid = [[c for c in lines.strip()] for lines in f.readlines()]

total = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        c = grid[y][x]

        if c != "X":
            continue

        # 🡹
        if y >= 4 - 1:
            for offset, char in enumerate("XMAS"):
                if grid[y - offset][x] != char:
                    break
            else:
                print(f"🡹  XMAS at ({y}, {x})")
                total += 1

            # 🢅
            if x <= (len(grid[y]) - 4):
                for offset, char in enumerate("XMAS"):
                    if grid[y - offset][x + offset] != char:
                        break
                else:
                    print(f"🢅  XMAS at ({y}, {x})")
                    total += 1

            # 🡼
            if x >= 4 - 1:
                for offset, char in enumerate("XMAS"):
                    if grid[y - offset][x - offset] != char:
                        break
                else:
                    print(f"🢅  XMAS at ({y}, {x})")
                    total += 1

        # 🡲
        if x <= (len(grid[y]) - 4):
            for offset, char in enumerate("XMAS"):
                if grid[y][x + offset] != char:
                    break
            else:
                print(f"🡲  XMAS at ({y}, {x})")
                total += 1

        # 🡸
        if x >= 4 - 1:
            for offset, char in enumerate("XMAS"):
                if grid[y][x - offset] != char:
                    break
            else:
                print(f"🡸  XMAS at ({y}, {x})")
                total += 1

        # 🡻
        if y <= (len(grid[y]) - 4):
            for offset, char in enumerate("XMAS"):
                if grid[y + offset][x] != char:
                    break
            else:
                print(f"🡻  XMAS at ({y}, {x})")
                total += 1

            # 🢆
            if x <= (len(grid[y]) - 4):
                for offset, char in enumerate("XMAS"):
                    if grid[y + offset][x + offset] != char:
                        break
                else:
                    print(f"🢆  XMAS at ({y}, {x})")
                    total += 1

            # 🢇
            if x >= 4 - 1:
                for offset, char in enumerate("XMAS"):
                    if grid[y + offset][x - offset] != char:
                        break
                else:
                    print(f"🢇  XMAS at ({y}, {x})")
                    total += 1

# print("-", [str(i) for i in range(10)])
# [print(i, row) for i, row in enumerate(grid)]

print(total)
