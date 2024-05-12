#!/usr/bin/python3
"""
defining a function that calculates
the perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter in the given grid
    """
    length = len(grid)
    breath = len(grid[0])
    p = 0
    for i in range(length):
        for j in range(breath):
            if grid[i][j] == 1:
                p += 4
                if (j < breath - 1 and grid[i][j + 1] == 1):
                    p -= 2
                if (i < length - 1 and grid[i + 1][j] == 1):
                    p -= 2
    return p
