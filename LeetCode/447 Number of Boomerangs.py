# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 00:58:26 2017

@author: Administrator
"""

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        l = len(points)
        disMatrix = [[0 for i in range(l)] for j in range(l)]
        for i in range(l):
            for j in range(i, l):
                disMatrix[i][j] = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                disMatrix[j][i] = disMatrix[i][j]
        result = 0
        for row in disMatrix:
            dic = {}
            for r in row:
                if r not in dic:
                    dic[r] = 1
                else:
                    dic[r] += 1
            for d in dic:
                result += dic[d] * (dic[d] - 1)
        return result
            
                
        