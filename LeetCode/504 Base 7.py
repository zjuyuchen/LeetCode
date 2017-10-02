# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 23:39:45 2017

@author: Administrator
"""
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        temp = ''
        neg = False
        if num == 0:
            return '0'
        if not num:
            return ''
        if num < 0:
            neg = True
            num = -num
        while(num>0):
            temp = str(num%7) + temp 
            num //= 7
        if neg:
            return '-' + temp
        return temp
#test = Solution()
#print(test.convertToBase7(-100))