# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:57:58 2017

@author: yc
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma1 = float('-inf')
        ma2 = float('-inf')
        ma3 = float('-inf')
        for n in nums:
            if ma1 < n:
                ma3 = ma2
                ma2 = ma1
                ma1 = n
            elif ma2 < n and n != ma1 and n!= ma2:
                ma3 = ma2
                ma2 = n
            elif ma3 < n and n != ma2 and n!= ma1:
                ma3 = n
            else:
                continue
        if ma3 != float('-inf'):
            return ma3
        else:
            return ma1