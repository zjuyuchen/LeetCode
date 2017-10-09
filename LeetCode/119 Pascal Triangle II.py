# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 19:29:29 2017

@author: yc
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def jiecheng(i):
            if i == 0:
                return 1
            else:
                result = 1
                for k in range(1,i+1):
                    result *= k
            return result
        def c(m,n):
            return int(jiecheng(n)/(jiecheng(n-m)*jiecheng(m)))
        return [c(m, rowIndex) for m in range(rowIndex+1)]
test = Solution()
print(test.getRow(8))