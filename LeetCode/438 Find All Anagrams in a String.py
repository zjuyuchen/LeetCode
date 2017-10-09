# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:11:42 2017

@author: Administrator
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        
        
#        def isAnagram(s, t):
#            dic1 = {}
#            dic2 = {}
#            if len(s) != len(t):
#                return False
#            for i in s:
#                if i not in dic1:
#                    dic1[i] = 1
#                else:
#                    dic1[i] += 1
#            for j in t:
#                if j not in dic2:
#                    dic2[j] = 1
#                else:
#                    dic2[j] += 1
#            for k in dic1:
#                if k not in dic2 or dic2[k] != dic1[k]:
#                    return False
#            return True
#        a = []
#        for i in range(len(s)-len(p)):
#            t = s[i:i+len(p)]
#            if isAnagram(t, p):
#                a.append(i)
#        return a
