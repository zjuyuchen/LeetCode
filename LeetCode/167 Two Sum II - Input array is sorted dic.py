# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:59:40 2017

@author: Administrator
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return dic[target -num]+1, i+1
            else:
                dic[num] = i
            