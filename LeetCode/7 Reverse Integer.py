# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 00:14:57 2017

@author: yc
"""

##Wow, beat 99.5%!

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        bo = 1
        if x <0:
            x = x*-1
            bo = -1
        while(x!=0):
            res  = 10*res + x % 10
            x = x//10
        if res > 2**31 +1:
            return 0
        return res*bo
        