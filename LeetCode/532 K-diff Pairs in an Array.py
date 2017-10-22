# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 23:21:22 2017

@author: yc
"""


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        count = 0
        for n in nums:
            if n+k in dic or n-k in dic:
                count += 1
                dic[n] = 1
            else:
                dic[n] = 1
        return count 
test = Solution()
print(test.findPairs([1, 3, 1, 5, 4],2))