# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:31:46 2017

@author: yc
"""

#Leetcode里面默认'/'是求整数部分，实际上‘//'才返回整数，所以如果判断的是float类型，一定要强制转换才可以！

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        count = 0
        temp = 2
        for i in range(1,len(A)-1):
            if float(A[i]) == (A[i-1] + A[i+1])/2.0:
                temp += 1
            else:
                if temp >= 3:
                    count += (temp-1)*(temp-2)/2
                temp = 2
        if temp >= 3:
            count += (temp-1)*(temp-2)/2
        return int(count)