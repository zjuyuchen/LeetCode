# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 23:32:53 2017

@author: Administrator
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []
        n = len(nums)
        return int(n* (n + 1)/2 - sum(nums))
#test = Solution()
#print(test.missingNumber([]))