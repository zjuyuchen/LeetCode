# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 14:04:55 2017

@author: yc
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #定义一个addtodic函数，判断每一个[i, j],如果等于1,就加入数组c中，对周围四个位置做递归。但要排除已经添加到c中的位置。
        #优化时间，对已经加入过c中的位置不再做计算，通过dic来判断。全1数组只需要进行1次遍历，而非m*n次遍历。
        dic = []
        def addtodic(i,j):
            if (i>=0 and i< len(grid) and j>=0 and j< len(grid[0])) and [i, j] not in c:
                if grid[i][j] == 1:
                    c.append([i, j])
                    dic.append([i, j])
                    addtodic(i-1, j)
                    addtodic(i+1, j)
                    addtodic(i, j-1)
                    addtodic(i, j+1)
        nums = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                c = []
                if [i, j] not in dic:
                    addtodic(i, j)
                    nums.append(len(c))
        return max(nums)
#test = Solution()
#print(test.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]))