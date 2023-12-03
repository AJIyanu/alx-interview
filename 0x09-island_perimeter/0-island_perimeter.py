#!/usr/bin/python3
"""Calcluate the perimeter of an Island"""


def island_perimeter(grid):
    """Calculate the perimeter of an island"""
    row = 0
    column = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j == 0:
                if grid[i][j] == 1:
                    row += 1
            elif j == len(grid[i]) - 1:
                if grid[i][j] == 1:
                    row += 1
            else:
                if grid[i][j] != grid[i][j - 1]:
                    row += 1
                    # print(grid[i][j - 1])
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if j == 0:
                if grid[i][j] == 1:
                    column += 1
            elif j == len(grid[i]) - 1:
                if grid[i][j] == 1:
                    column += 1
            else:
                if grid[i][j] != grid[i][j - 1]:
                    column += 1
    return row + column
