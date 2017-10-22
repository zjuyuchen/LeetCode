# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:28:26 2017

@author: yc
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, base=2)
        b = int(b, base=2)
        return bin(a+b)[2:]