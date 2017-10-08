# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:24:02 2017

@author: yc
"""
#先排序，要么是最大的三个正数相乘，
#要么是两个最小的负数和最大的正数相乘
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])