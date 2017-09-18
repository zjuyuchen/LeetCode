# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:29:21 2017

@author: Administrator
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i ,k = 0, len(numbers)-1
        while(1):
            if numbers[i] + numbers[k] == target:
                return i+1, k+1
            elif numbers[i] + numbers[k] > target:
                k -= 1
            else:
                i += 1
                