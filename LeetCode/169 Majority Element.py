# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 23:26:00 2017

@author: Administrator
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        l = len(nums)
        for i in nums:
            if i in dic:
                dic[i] += 1
            if dic[i] < l/2:
                return i
            else:
                dic[nums[i]] = 1
#            
#test = Solution()
#print(test.majorityElement([3,2,3]))
            
                
        
        