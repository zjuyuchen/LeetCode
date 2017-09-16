# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:44:12 2017

@author: Administrator
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in s:
            result = 26*result + ord(i) - ord('A') + 1
        return result
test = Solution()
print(test.titleToNumber('AA'))
            