# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:40:59 2017

@author: yc
"""
#This is a typical solution using self space.
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                result.append(abs(n))
            else:
                nums[abs(n)-1] *= -1
        return result