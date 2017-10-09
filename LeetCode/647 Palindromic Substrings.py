# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 00:46:41 2017

@author: Administrator
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isP(s):
            return s == s[::-1]
        count = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if isP(s[i:j]):
                    count += 1
        return count
        
test = Solution()
print(test.countSubstrings(''))