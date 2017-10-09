# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 00:34:43 2017

@author: Administrator
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        for i,l in enumerate(list1):
            if l in list2:
                print(index(l))
test = Solution()
print(test.findRestaurant(['a','b'],['a','c']))