# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 01:08:56 2017

@author: Administrator
"""

import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Any numSquares(n) must be 1(j*j) plus numSquares(n-j*j)
        cntLeast = [100000000 for i in range(n+1)]
        cntLeast[0] = 0
        for i in range(1, n+1):
            for j in range(1,int(math.sqrt(i))+1):
                cntLeast[i] = min(cntLeast[i], cntLeast[i-j*j]+1)
        return cntLeast[n]
        
                    