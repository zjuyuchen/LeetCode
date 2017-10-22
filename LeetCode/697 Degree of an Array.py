# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 23:34:37 2017

@author: yc
"""
#Beat91%，使用一个每个键对应三个值的字典‘a’:[numbers of a, start_index of a, end_index of a]
#find the maximun of numbers, and minimun end-start + 1

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                dic[n][0] += 1
                dic[n][2] = i
            else:
                dic[n] = [1,i,i]
        ma = -1
        res = len(nums)
        for d in dic:
            ma = max(dic[d][0], ma)
        for d in dic:
            if dic[d][0] == ma:
                res = min(res, dic[d][2]-dic[d][1]+1)
        return res
#test = Solution()
#print(test.findShortestSubArray([1,2,2,3,1,4,2]))