# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:07:29 2017

@author: yc
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= k:
            return s[:k][::-1]
        elif len(s) <= 2*k:
            return s[:k][::-1] + s[k:]
        else:
            return self.reverseStr(s[:2*k],k) + self.reverseStr(s[2*k:],k)
#test = Solution()
#print(test.reverseStr("abcdefg",8))