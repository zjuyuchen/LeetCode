# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:36:42 2017

@author: yc
"""

#本质上是斐波那契数列，除了第一二层，后面的每层都是 f(n-1) + f(n-2)，要么一步到f(n-1)，要么两步到f(n-2)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [1,1,2]
        for i in range(3,n+1):
                a.append(a[i-1] + a[i-2])
        return a[n]
        