# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 23:51:46 2017

@author: yc
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r
test = Solution()
print(test.mySqrt(2))