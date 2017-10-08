# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 19:57:33 2017

@author: yc
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
#        if not nums:
#            return False
#        if k >= len(nums) and len(set(nums)) < len(nums):
#            return True
#        for i in range(len(nums)-k):
#            if len(set(nums[i:i+k+1])) <= k:
#                return True
#        return False

        #Thanks caikehe's Solution
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <=k:
                return True
            dic[v]  = i
        return False
#test = Solution()
#print(test.containsNearbyDuplicate([1,1], 2))