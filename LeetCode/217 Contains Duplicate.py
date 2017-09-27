# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:10:49 2017

@author: Administrator
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        s = set(nums)
        if len(s) == len(nums):
            return False
        else:
            return True
test = Solution()
print(test.containsDuplicate([]))