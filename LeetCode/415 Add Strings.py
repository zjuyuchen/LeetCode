# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:06:59 2017

@author: yc
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        res = []
        mem = 0
        count = len(num1) - len(num2)
        for n in zip(num1[::-1], num2[::-1]):
            s = mem + int(n[0]) + int(n[1])
            if s <10:
                res.append(str(s))
                mem = 0
            else:
                res.append(str(s%10))
                mem = 1
        for n in num1[:count][::-1]:
            s = int(n) + mem
            if s <10:
                res.append(str(s))
                mem = 0
            else:
                res.append(str(s%10))
                mem = 1
        if s >= 10:
            res.append('1')
            
        return ''.join(res[::-1])