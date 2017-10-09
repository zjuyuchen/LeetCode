# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:35:34 2017

@author: yc
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            a = self.countAndSay(n-1)
            s = ''
            count = 1
            i = 0
            temp = a[i]
            while i < len(a):
                if i < len(a) -1 and a[i+1] == temp:
                    count += 1
                    i += 1
                else:
                    s = s + str(count) + temp
                    i += 1
                    count = 1
                    if i < len(a):
                        temp = a[i]
            return s
test = Solution()
print(test.countAndSay(6))