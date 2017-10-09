# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:19:14 2017

@author: yc
"""
#I do not understand why nums[:] = nums[-k:] + nums[:-k] dose not work.
#The difference between nums and nums[:] is that the latter one dose not make a copy.
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nums[:] = nums[l-k:] + nums[:l-k]