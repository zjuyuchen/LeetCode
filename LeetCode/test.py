# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:59:28 2017

@author: Administrator
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        count = 0
        temp = 0
        for d in dic:
            count += dic[d]//2 *2
            temp += dic[d] % 2
        if temp != 0:
            return count + 1
        return count
test = Solution()
print(test.longestPalindrome(""))