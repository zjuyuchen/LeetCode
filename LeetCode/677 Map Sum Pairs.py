# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 22:41:21 2017

@author: yc
"""

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.li = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.li[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        leng = len(prefix)
        s = 0
        for l in self.li:
            if prefix == l[:leng]:
                s += self.li[l]
        return s


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)