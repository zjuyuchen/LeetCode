# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:34:42 2017

@author: Administrator
"""

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        c = [0, 0]
        i = int(area**0.5)
        print(i)
        while(i>=1):
            if  area%i == 0:
                c[0], c[1] =  area//i, i
                break
            else:
                c[0], c[1] = 0, 0
            i -= 1
        return c
#test = Solution()
#print(test.constructRectangle(4))