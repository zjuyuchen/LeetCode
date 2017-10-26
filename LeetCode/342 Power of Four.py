# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:27:10 2017

@author: yc
"""
#原题不让用loop也不让用调用，只能数学方法/

import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=0:
            return False
        return math.log10(num)/(math.log10(2)) % 2 == 0