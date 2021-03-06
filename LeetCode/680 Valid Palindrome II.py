# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:43:05 2017

@author: yc
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        def pail(a):
            mid = len(a)//2
            if len(a) %2 == 0:
                return a[:mid] == a[mid:][::-1]
            else:
                return a[:mid+1] == a[mid:][::-1]

        i = 0
        for i in range(len(s)//2+1):
            if s[i] != s[len(s)-1-i]:
                return pail(s[:i]+s[i+1:]) or pail(s[:len(s)-1-i]+s[len(s)-i:])
            else:
                continue
        return True
test = Solution()
print(test.validPalindrome(''))