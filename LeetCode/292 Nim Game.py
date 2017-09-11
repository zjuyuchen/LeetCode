# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 00:59:07 2017

@author: Administrator
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not n%4 == 0

#test = Solution()
#print(test.canWinNim(134820612))