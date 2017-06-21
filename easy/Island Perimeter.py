# -*- coding: utf-8 -*-
"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island 
(i.e., one or more connected land cells). 
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. 
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""

grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
grid1 = [[1]]
def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row = len(grid)
    column = len(grid[0])
    grid.insert(row, [0]*column)
    grid.insert(0, [0]*column)
    for g in grid:
        g.insert(column,0)
        g.insert(0,0)
      
    perimeter = 0
    for i in range(1,row+1):
        for j in range(1,column+1):
            if grid[i][j] == 1:
                around = [grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1]]
                perimeter += 4- sum(around)
                
    return grid, perimeter
grid_final, perimeter = islandPerimeter(grid1)
print(grid_final)
print(perimeter)