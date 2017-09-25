# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 01:14:55 2017

@author: Administrator
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        while(s[-1] == ' ' and len(s) >=2):
            s = s[:-1]
        if s == ' ':
            return 0
        return len(s.split(' ')[-1])
    
test = Solution()
print(test.lengthOfLastWord("Hello World "))