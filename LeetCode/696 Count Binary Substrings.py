# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 22:38:20 2017

@author: yc
"""

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        li = list(s)
        num_1 = 0 if li[0] == '0' else 1 
        num_0 = 1 if li[0] == '0' else 0
        print(num_1, num_0)
        count = 0
        for i in range(len(li)-1):
            num_1 = 0
            num_0 = 0
            for j in range(i+1,len(li)):
                if li[j] == '1':
                    num_1 += 1
                else:
                    num_0 += 1
                print(num_0,num_1)
                if num_1 == num_0:
                    count += 1
        return count
test = Solution()
print(test.countBinarySubstrings("00110011"))