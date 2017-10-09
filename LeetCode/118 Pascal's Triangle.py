# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:07:40 2017

@author: yc
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def jiecheng(i):
            if i == 0:
                return 1
            else:
                result = 1
                for j in range(2,i+1):
                    result *=j
            return result
        def c(n,m):
            return jiecheng(n)/(jiecheng(m)*jiecheng(n-m))
        s = []
        for i in range(numRows):
            temp  = [c(i, m) for m in range(i+1)]
            s.append(temp)
        return s
test = Solution()
print(test.generate(5))