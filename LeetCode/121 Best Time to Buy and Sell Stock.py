# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:00:44 2017

@author: yc
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPro = 0
        min_Pri = float('inf')
        for p in prices:
            min_Pri = min(p, min_Pri)
            pro = p - min_Pri
            maxPro = max(maxPro, pro)
        return maxPro