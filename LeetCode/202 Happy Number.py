# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:19:52 2017

@author: 126PC-3
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n**2 == 1:
            return True
        else:
            temp = 0
            while(n != 0):
                temp += (n%10)**2
                n //= 10
            return self.isHappy(temp)
test = Solution()
print(test.isHappy(2))