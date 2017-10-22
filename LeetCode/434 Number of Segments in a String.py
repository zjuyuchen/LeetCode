# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:33:12 2017

@author: yc
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = s.split(' ')
        print(s)
        count = 0
        for i in s:
            if i != '':
                count += 1
        return count
test = Solution()
print(test.countSegments('   '))