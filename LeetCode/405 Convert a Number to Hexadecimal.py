# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:40:05 2017

@author: yc
"""

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            return self.toHex(4294967296+num)
        hexg = [str(i) for i in range(10)]+['a', 'b', 'c', 'd', 'e', 'f']
        res = ''
        while(num % 16 !=0 or num //16 != 0):
            res += hexg[num % 16]
            num //= 16
        return res[::-1]
test = Solution()
print(test.toHex(16))