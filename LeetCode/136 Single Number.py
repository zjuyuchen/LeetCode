# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 13:11:14 2017

@author: yc
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = max(nums)
        b = min(nums)
        l = a - b
        temp = [0 for i in range(l+1)]
        for num in nums:
            temp[num-b] += 1
        for t in range(len(temp)):
            if temp[t] == 1:
                return t+b
            
#test = Solution()
#print(test.singleNumber([2,2,4,4,3]))
        