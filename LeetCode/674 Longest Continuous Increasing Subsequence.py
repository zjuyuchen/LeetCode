# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 22:27:38 2017

@author: yc
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = []
        count = 0
        i = 0
        while(i<len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                c.append(count+1)
                count = 0
            i += 1
        c.append(count+1)
        if len(nums) == 0:
            return 0
        return max(c)
#test = Solution()
#print(test.findLengthOfLCIS([]))