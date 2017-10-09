# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:19:48 2017

@author: Demo
"""

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
#do n=5, k=1, k=2, k=3, k=4, you will find the sequence:
#[1, k+1, 2, k, 3, k-1...]
        if k == 1:
            return [i+1 for i in range(n)]
        res = [(i+2)//2 for i in range(n)]
        for i in range(k-1):
            if (2*i + 1) < n:
                res[2*i+1] = k+1-i
        for j in range(k+1,n):
            res[j] = j+1
        return res
test = Solution()
print(test.constructArray(10,9))
        