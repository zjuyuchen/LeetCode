# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 23:17:18 2017

@author: Administrator
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxn = 0
        temp = 0 
        for i in nums:
            if i == 1:
                temp += 1
                if temp > maxn:
                    maxn = temp
            else:
                temp = 0
        return maxn