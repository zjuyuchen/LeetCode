# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 23:09:31 2017

@author: Administrator
"""

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        return min(i[0] for i in ops)*min(j[1] for j in ops)
test = Solution()
print(test.maxCount(3,3,[[2,2],[3,3]]))