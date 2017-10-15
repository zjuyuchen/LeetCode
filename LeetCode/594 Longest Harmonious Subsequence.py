# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 21:53:49 2017

@author: yc
"""
import collections
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        dic = collections.Counter(nums)
#        for n in nums:
#            if n in dic:
#                dic[n] += 1
#            else:
#                dic[n] = 1
        res = 0
        keys = sorted(dic.keys())
        i = 0
        while(i<len(keys)-1):
            if keys[i+1] == keys[i] +1:
                res = max(res, dic[keys[i]] + dic[keys[i+1]])
            i += 1
        return res
test = Solution()
print(test.findLHS([1,2,2,2,3,3,3,4,4,4,4]))