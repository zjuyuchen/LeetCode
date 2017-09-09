# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 01:30:57 2017

@author: Administrator
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)): 
                print(i,j)
                if ((nums[i] + nums[j]) == target):

                    return [i,j]
                else:
                    continue
#test = Solution()
#print(test.twoSum([3,2,4],6))