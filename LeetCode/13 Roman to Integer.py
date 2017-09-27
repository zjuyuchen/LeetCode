# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:56:12 2017

@author: Administrator
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'M': 1000, 'D': 500, 'C':100, 
               'L': 50, 'X': 10, 'V': 5, 'I':1}
        result = 0
        if len(s) == 1:
            return dic[s]
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                result -= dic[s[i]]
            else:
                result += dic[s[i]]
        return dic[s[i+1]] + result
test = Solution()
print(test.romanToInt('XCIX'))
                
        