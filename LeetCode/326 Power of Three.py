# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 00:23:37 2017

@author: yc
"""
#题目建议不要用循环和递归，我这里还是用的递归
#如果不用递归的话，用Math.log_3是否为整数可以判断（可能要考虑浮点数）
#也可以cheating, 用32位digit所能存储的最大3幂数除以要判断的值，是整数就输出为真
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while(n>1):
            if n%3 != 0:
                return False
            n /= 3
        return True
            