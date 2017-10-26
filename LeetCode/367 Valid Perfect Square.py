# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:41:44 2017

@author: yc
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        a = [1, num]
        mid = (a[0]+a[1])//2
        while(a[0]**2<num and a[1]**2>num):
            b = a[:]
            mid = (a[0]+a[1])//2
            temp = mid**2
            if temp == num:
                return True
            elif temp < num:
                a[0] = mid
            else:
                a[1] = mid
            if a == b:
                break
        return False
test = Solution()
print(test.isPerfectSquare(32))