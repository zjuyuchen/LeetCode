# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:07:42 2017

@author: Administrator
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        k = i = 0
        while(i<len(g) and k<len(s)):
            if g[i] <= s[k]:
                i += 1
                k += 1
            else:
                k += 1
        return i

                    
                