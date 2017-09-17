# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:33:26 2017

@author: Administrator
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        if not nums:
            return result
        minl = min(nums)
        maxl = max(nums)
        l = maxl - minl + 1

        c = [-1 for i in range(l+1)]
        for i in range(len(nums)-1):
            j = i
            while((j < len(nums)-1) and (nums[i] > nums[j+1])):
                j += 1
            if (j < len(nums) - 1) and (nums[i] < nums[j+1]):
                c[nums[i]-minl] = nums[j+1]
        for f in findNums:
                result.append(c[f - minl])
        return result
test = Solution()
print(test.nextGreaterElement([1,2,3],[6,5,4,3,2,1,7]))
            
            