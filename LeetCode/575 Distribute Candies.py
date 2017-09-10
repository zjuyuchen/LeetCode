# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:14:45 2017

@author: yc
"""
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        setc = set(candies)
        if len(setc) >= len(candies)//2:
            return len(candies)//2
        else:
            return len(setc)
        '''
        or
        return min(len(setc), len(candies)//2)