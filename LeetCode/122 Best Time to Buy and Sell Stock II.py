# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 22:55:14 2017

@author: Administrator
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        pro = 0
        l = len(prices)
        for i in range(l-1):
            if prices[i+1] > prices[i]:
                pro += prices[i+1] - prices[i]
        return pro
                
#test = Solution()
#print(test.maxProfit([1,2,3]))