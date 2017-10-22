# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:42:46 2017

@author: Demo
"""
#If no zero, the results for all elements are product/element
#If two or more zeros, all the results should be 0.
#If only one zero, the result for zero is the product of all other elements.
##The results for other elements are 0.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero = 0
        result = 1
        for i in nums:
            if i == 0:
                zero += 1
            else:
                result *= i
        if zero > 1:
            return [0 for i in range(len(nums))]
        if zero == 1:
            return [0 if nums[i] !=0 else result for i in range(len(nums) )]
        return [result//i for i in nums]
#test = Solution()
#print(test.productExceptSelf([1,0]))