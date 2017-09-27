# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:58:44 2017

@author: Administrator
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            if dic[i]:
                dic[i] += 1
            else:
                dic[i] = 1
        count = 0
        for d in dic:
            count += d.value//2
        