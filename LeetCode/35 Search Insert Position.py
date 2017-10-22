# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:04:48 2017

@author: yc
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1
        mid = len(nums)//2
        if nums[mid-1] < target <= nums[mid]:
            return mid
        elif target == nums[mid -1]:
            return mid-1
        elif target < nums[mid]:
            return self.searchInsert(nums[:mid], target)
        else:
            return mid + 1 + self.searchInsert(nums[mid+1:], target)
#test = Solution()
#print(test.searchInsert([1,2],3))