# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 22:44:43 2017

@author: yc
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c = []
        dic1 = {}
        dic2 = {}
        for n1 in nums1:
            if n1 not in dic1:
                dic1[n1] = 1
            else:
                dic1[n1] += 1
        for n2 in nums2:
            if n2 not in dic2:
                dic2[n2] = 1
            else:
                dic2[n2] += 1
        for d in dic1:
            if d in dic2:
                count = min(dic1[d], dic2[d])
                for i in range(count):
                    c.append(d)
        return c
test = Solution()
print(test.intersect([1,2,2,1],[2,2]))