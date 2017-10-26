# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:39:07 2017

@author: yc
"""

#分治法，不过不怎么好。11%

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mid = len(nums)//2
        return max(nums[mid]+self.rob(nums[:mid-1]) +self.rob(nums[mid+2:]), self.rob(nums[:mid]) +self.rob(nums[mid+1:]))