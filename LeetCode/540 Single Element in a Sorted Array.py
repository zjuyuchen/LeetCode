# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:28:49 2017

@author: yc
"""

#题目感觉很简单，却搞了一个小时才debug完。做题前先在本子上把思路捋顺了在动手。节约时间！！！
#95%

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        mid = len(nums)/2
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        l = len(nums[:mid])
        if nums[mid] == nums[mid-1]:
            if l % 2 == 0:
                return self.singleNonDuplicate(nums[:mid-1])
            else:
                return self.singleNonDuplicate(nums[mid+1:])
        else:
            if l % 2 == 0:
                return self.singleNonDuplicate(nums[mid+2:])
            else:
                return self.singleNonDuplicate(nums[:mid])