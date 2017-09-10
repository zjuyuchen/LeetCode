# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:31:22 2017

@author: yc
"""
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        size = len(nums) * len(nums[0])
        if r * c != size:
            return nums
        else:
            temp = []
            for n in nums:
                for i in n:
                    temp.append(i)
            return [[temp[row*c + col] for col in range(c)] for row in range(r)]
#test = Solution()
#print(test.matrixReshape([[1,2],[3,4]],4,1))