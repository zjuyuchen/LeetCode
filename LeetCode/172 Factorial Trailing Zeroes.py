# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:31:21 2017

@author: yc
"""
#All zeros come from 5, but for 5^n, they contribute n zeros.
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            return n//5 + self.trailingZeroes(n//5)
        
test = Solution()
print(test.trailingZeroes(30))