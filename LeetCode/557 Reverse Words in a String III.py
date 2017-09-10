# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:25:24 2017

@author: yc
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        result = []
        for word in words:
            temp = ''
            for w in word[::-1]:
                temp += w
            result.append(temp)
        return ' '.join(result)
#test = Solution()
#print(test.reverseWords("Let's take LeetCode contest"))
                