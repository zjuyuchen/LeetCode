# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:54:40 2017

@author: yc
"""
#这个题目描述不清楚，差评。
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in digits:
            num = num*10 + i
        num += 1
        result = []
        while(num!=0):
            result.append(num%10)
            num //=10
        return result[::-1]
test = Solution()
print(test.plusOne([9,9,9,9,9,2]))