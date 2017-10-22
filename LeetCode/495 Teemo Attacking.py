# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:21:24 2017

@author: Demo
"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] -timeSeries[i-1] <= duration: 
                res += timeSeries[i] -timeSeries[i-1]
            else:
                res += duration
        if timeSeries != []:
            return res + duration
        return 0
            
#test = Solution()
#print(test.findPoisonedDuration([1,2],2))