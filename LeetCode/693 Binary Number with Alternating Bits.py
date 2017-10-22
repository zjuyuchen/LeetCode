# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 10:00:29 2017

@author: Administrator
"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = list(bin(n))[2:]
        i = 0
        while(i<len(x)-1):
            if x[i+1] == x[i]:
                return False
            i += 1
        return True
        