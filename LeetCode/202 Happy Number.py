# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:06:24 2017

@author: yc
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Thanks Freezen, his solution helps me to undertand Floyd Cycle finally!
        def digitSquareSum(n):
            su = 0
            while(n):
                tem = n % 10
                su += tem**2
                n //= 10
            return su
        slow = fast = n
        while True:
            slow = digitSquareSum(slow)
            fast = digitSquareSum(digitSquareSum(fast))
            if slow == fast:
                break
        fast = n
        #This step can print the start of the circle!
#        while True:
#            slow = digitSquareSum(slow)
#            fast = digitSquareSum(fast)
#            if slow == fast:
#                print(fast)
#                break
        if slow == 1:
            return True
        else:
            return False
test = Solution()
print(test.isHappy(16))