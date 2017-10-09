# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:29:48 2017

@author: yc
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return ''
        c = [i for i in nums]
        c.sort()
        dic = {}
        i = 0
        for k in c[::-1]:
            dic[k] = i
            i += 1
        result = ['' for i in range(len(nums))]
        print(dic)
        for j, n in enumerate(nums):
            print(j,n,dic[n])
            if dic[n] == 0:
                result[j] = 'Gold Medal'
            elif dic[n] == 1:
                result[j] = 'Silver Medal'
            elif dic[n] == 2:
                result[j] = 'Bronze Medal'
            else:
                result[j] = str(dic[n]+1)
        return result
                
test = Solution()
print(test.findRelativeRanks([10,3,8,9,4]))