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
        dic = {}
        res = len(list1) + len(list2)
        s = []
        for i,l in enumerate(list1):
            dic[l] = i
        for i,l in enumerate(list2):
            if l in dic:
                res = min(res, i+dic[l])
        for i,l in enumerate(list2):
            if l in dic:
                if res == i+dic[l]:
                    s.append(l)
        return s