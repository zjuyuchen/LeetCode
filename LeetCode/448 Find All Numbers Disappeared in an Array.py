# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:52:12 2017

@author: 126PC-3
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        size = len(nums)
        temp = [0 for i in range(size)]
        for i in nums:
            temp[i-1] += 1
        for t in range(size):
            if not temp[t]:
                result.append(t+1)
        return result
#test = Solution()
#print(test.findDisappearedNumbers([1,3,4,4]))