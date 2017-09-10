# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:52:41 2017

@author: yc
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        result = k + 1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    result = min(j-i,result)
        return result <= k
test = Solution()
print(test.containsNearbyDuplicate()
