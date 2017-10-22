# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:09:35 2017

@author: yc
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        count = 1            
        sumf = 0
        while(i<len(flowerbed)):
            if flowerbed[i] == 0:
                count +=1
            else:
                sumf += (count-1)//2
                count = 0
            i += 1
        sumf += (count)//2
        return sumf >= n
#test = Solution()
#print(test.canPlaceFlowers([0,0,1,0,0,0,0,0,1],2))