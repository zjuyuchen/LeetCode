# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:58:35 2017

@author: yc
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def f(x):
            return [-x[0], x[1]]
        people.sort(key=f)
        res = []
        for item in people:
            res.insert(item[1], item)
        return res