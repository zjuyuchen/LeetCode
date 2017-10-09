# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:07:20 2017

@author: Administrator
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        for j in t:
            if j not in dic2:
                dic2[j] = 1
            else:
                dic2[j] += 1
        for k in dic1:
            if k not in dic2 or dic2[k] != dic1[k]:
                return False
        return True
        
#test = Solution()
#print(test.isAnagram('abcdefg','acdbegfm'))