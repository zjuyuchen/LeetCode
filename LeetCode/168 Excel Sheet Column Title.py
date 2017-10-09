# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:56:00 2017

@author: Administrator
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while(n > 0):
            if n%26 ==0:
                result = 'Z' + result
                n = n//26 -1
            else:
                result = chr(n%26 + ord('A') -1) + result
                n = n//26
        return result
test = Solution()
print(test.convertToTitle(29))