# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 22:46:49 2017

@author: yc
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lw = len(grid[0])
        lh = len(grid)
        c = [[0 for i in range(lw+2)] for j in range(lh+2)]
        for i in range(lh):
            for j in range(lw):
                c[i+1][j+1] = grid[i][j]
                
        def sum_count(i,j):
            sets = (i + 1, j), (i - 1, j), (i , j + 1), (i , j + 1)
            sum_ = 0
            for x, y in sets:
                if c[x][y] == 0:
                    sum_ += 1
            return sum_

        perimeter = 0
        for i in range(1,lh+1):
            for j in range(1,lw+1):
                if c[i][j] == 1:
                    perimeter += sum_count(i,j)
        return perimeter
#test = Solution()
#print(test.islandPerimeter([[1],[0]]))