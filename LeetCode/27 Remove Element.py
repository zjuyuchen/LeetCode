# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:52:29 2017

@author: yc
"""
#Thank vy7Sun's Solusion
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        m= 0
        length = len(nums)
        for i in range(length):
            if nums[i] != val:
                nums[m] = nums[i]
                m += 1
        return m