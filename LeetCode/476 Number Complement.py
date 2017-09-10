# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 13:37:14 2017

@author: yc
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = []
        while(num):
            temp.append(num%2)
            num = num//2
        for i in range(len(temp)):
            temp[i] = ~temp[i]+2
        result = 0
        i = len(temp)-1
        while(i>=0):
            result = result*2 + temp[i]
            i -= 1
        return result
        
        
#test = Solution()
#print(test.findComplement(5))