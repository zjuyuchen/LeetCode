# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 00:30:01 2017

@author: Administrator
"""

class Solution(object):
    def findLUSlength(self, A, B):
        if A == B:
            return -1
        return max(len(A), len(B))