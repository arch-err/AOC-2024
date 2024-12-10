#!/usr/bin/env python

with open("../input/1/input") as f:
    grid = [[c for c in lines.strip()] for lines in f.readlines()]


startingPosChar = "^"
startingDirection = "u"

for y in range(len(grid)):
    try:
        x = grid[y].index(startingPosChar)
        startingPos = (x, y)
        break
    except ValueError:
        continue

print(startingPos)

x = startingPos[0]
y = startingPos[1]
direction = startingDirection

grid[y][x] = "X"

directions = "urdlurdl"

# Movement-rules
# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.

while True:
    if direction == "u":
        if y == 0:
            break
        if grid[y - 1][x] == "#":
            direction = directions[directions.index(direction) + 1]
            continue
        y -= 1
    elif direction == "d":
        if y == len(grid) - 1:
            break

        if grid[y + 1][x] == "#":
            direction = directions[directions.index(direction) + 1]
            continue
        y += 1
    elif direction == "l":
        if x == 0:
            break
        if grid[y][x - 1] == "#":
            direction = directions[directions.index(direction) + 1]
            continue
        x -= 1
    elif direction == "r":
        if x == len(grid[y]) - 1:
            break
        if grid[y][x + 1] == "#":
            direction = directions[directions.index(direction) + 1]
            continue
        x += 1

    grid[y][x] = "X"
    # [print(i) for i in grid]
    # print(direction)

print(x, y)
[print(i) for i in grid]

distinctPlaces = 0
for y in range(len(grid)):
    distinctPlaces += grid[y].count("X")

print(distinctPlaces)
