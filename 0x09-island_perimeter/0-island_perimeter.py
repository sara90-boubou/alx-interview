#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid
    :param grid:
    :return:
    """
    area = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, i2 in zip([0] + row, row + [0]):
            area += int(i1 != i2)
    return area                                                                                                                                                                                                                                    # Upper check
                                                                                                                                                                                                                                                                                        if (i != 0 and grid[i - 1][j] == 0):
                                                                                                                                                                                                                                                                                                            total_perimeter += 1
                                                                                                                                                                                                                                                                                                                        if (i == 0):
                                                                                                                                                                                                                                                                                                                                            # top edge case
                                                                                                                                                                                                                                                                                                                                                            total_perimeter += 1

                                                                                                                                                                                                                                                                                                                                                                        # Bottom Check
                                                                                                                                                                                                                                                                                                                                                                                    if (i != len(grid) - 1 and grid[i + 1][j] == 0):
                                                                                                                                                                                                                                                                                                                                                                                                        total_perimeter += 1
                                                                                                                                                                                                                                                                                                                                                                                                                    if (i == len(grid) - 1):
                                                                                                                                                                                                                                                                                                                                                                                                                                        # bottom edge case
                                                                                                                                                                                                                                                                                                                                                                                                                                                        total_perimeter += 1

                                                                                                                                                                                                                                                                                                                                                                                                                                                            return total_perimeter
