# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:30:34 2017

@author: yc
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        after x step movements, we get every number equal to m.
        then we have:
            sum + x(n-1) = n*m
        we know that m = min(nums) + m
        then we can get x
        """
        l = len(nums)
        s = sum(nums)
        minn = min(nums)
        return s - l*minn
    