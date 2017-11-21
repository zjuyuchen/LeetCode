# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:55:48 2017

@author: Demo
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(l):
            while ((nums[i]>0) and (nums[i]<=len(nums)) and (nums[i] != nums[nums[i]-1])):
                nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                print(nums)
        
        for i in range(l):
            if nums[i] != i+1:
                return i + 1
        return  l+1
test = Solution()
test.firstMissingPositive([3,4,-1,1])