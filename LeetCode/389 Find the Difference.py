# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:44:47 2017

@author: Administrator
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cs = [0 for i in range(27)]
        ct = [0 for i in range(27)]
        for j in s:
            cs[ord(j) - ord('a')] += 1
        for k in t:
            ct[ord(k) - ord('a')] += 1
        for i in range(27):
            if cs[i] != ct[i]:
                return chr(i + ord('a'))
            
test = Solution()
print(test.findTheDifference('abcd','abcde'))