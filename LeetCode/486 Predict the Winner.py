# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:32:23 2017

@author: yc
"""
#My solution cost a lot!!!
#class Solution(object):
#    def PredictTheWinner(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: bool
#        """
#        def score(nums):
#            s1 = 0
#            s2 = 0
#            if not nums:
#                return 0,0
#            elif len(nums) == 1:
#                return nums[0],0
#            else:
#                s1 = nums[0]+score(nums[1:])[1]
#                s2 = nums[-1]+score(nums[:-1])[1]
#                if s1>s2:
#                    return s1, score(nums[1:])[0]
#                else:
#                    return s2, score(nums[0:-1])[0]
#        res1, res2 = score(nums)[0], score(nums)[1]
#        return res1>=res2
#test = Solution()
#print(test.PredictTheWinner([2,4,3,4,55,1,2,3,1,2,4,3,4,5,1]))