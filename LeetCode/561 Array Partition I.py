# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 13:05:27 2017

@author: yc
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        i = 0
        while(i<len(nums)):
            sum += nums[i]
            i += 2
        return sum
    