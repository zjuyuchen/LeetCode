# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:22:45 2017

@author: yc
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# find the index of the last noneincrease i for left sorted array
# find the index of the first noneincrese j for right sorted array
        i = 0
        j = len(nums) - 1
        while( i < len(nums)-1 and nums[i+1]>=nums[i]):
            i += 1
        if i == len(nums) -1:
            return 0
        while(j > 1 and nums[j-1]<=nums[j]):
            j -= 1
        ma = max(nums[i:j+1])
        mi = min(nums[i:j+1])
        print(ma,mi)
        print(i,j)
        left = i
        right = j
        for m, x in enumerate(nums[:i]):
            if mi < x:
                left = m
                print(left)
                break
        for n, x in enumerate(nums[j:]):
            if ma > x:
                right = j + n +1
                print(right)
        return right - left
#test = Solution()
#print(test.findUnsortedSubarray([1,2,3,4,1]))