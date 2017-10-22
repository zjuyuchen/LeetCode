# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:46:05 2017

@author: yc
"""
#Thnaks Google's solusion
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = cmaxs = nums[0]
        for n in nums[1:]:
            cmaxs = max(n, cmaxs+n)
            maxs = max(maxs, cmaxs)
        return maxs
            