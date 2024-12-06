#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island described in grid.

    Args:
        grid (list of list of int): The grid representation of the map
                                     (0 for water, 1 for land).

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract 2 for each horizontal or vertical neighbor
                if r > 0 and grid[r - 1][c] == 1:  # Check above
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
