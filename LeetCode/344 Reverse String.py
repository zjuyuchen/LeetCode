# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:00:03 2017

@author: yc
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
test = Solution()
print(test.reverseString("Hello"))