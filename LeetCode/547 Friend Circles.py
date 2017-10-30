# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:32:10 2017

@author: Demo
"""

b = [[1,1,0],[1,1,0],[0,0,1],[0,0,0]]*2
print(b)
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(x,y,M):
            if x>=0 and x <len(M) and y>=0 and y < len(M[0]):
                if M[x][y] == 1:
                    M[x][y] = 0
                    dfs(x-1,y,M)
                    dfs(x,y-1,M)
                    dfs(x+1,y,M)
                    dfs(x,y+1,M)
                    
        count = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    dfs(i,j,M)
                    count += 1
        return count
test = Solution()
print(test.findCircleNum(b))