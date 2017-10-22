# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 19:31:57 2017

@author: yc
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []
        if len(nums) == 1:
            return 1
        m = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[:i][-1]:
                nums[m] = nums[i]
                m += 1
        return m
#test =  Solution()
#print(test.removeDuplicates([1,1,2]))