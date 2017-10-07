# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 08:16:39 2017

@author: Administrator
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = s.count('A')
        s2 = s.count('LLL')
        print(s1,s2)
        if s1>1 or s2:
            return False
        else:
            return True
test = Solution()
print(test.checkRecord("PPALLPLL"))