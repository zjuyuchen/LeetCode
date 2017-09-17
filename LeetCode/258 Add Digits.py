# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:06:16 2017

@author: 126PC-3
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num//10:
            return num
        else:
            temp =0
            while(num != 0):
                temp += num%10
                num = num//10
            return self.addDigits(temp)