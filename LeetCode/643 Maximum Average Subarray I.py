# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 19:00:40 2017

@author: yc
"""
#Thanks awice's solusion
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        p = [0]
        for x in nums:
            p.append(p[-1] + x)
        ma = max(p[i+k] - p[i] for i in range(len(nums)- k +1))
        return ma / float(k)
#My firt solusion
#      return max(sum(nums[i:i+k]) for i in range(len(nums)-k+1))/float(k)
#Time limit!!!