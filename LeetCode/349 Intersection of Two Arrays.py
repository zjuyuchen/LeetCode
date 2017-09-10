# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 13:22:38 2017

@author: yc
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i = j =0
        c = []
        key = ''
        while( (i < len(nums1)) & (j < len(nums2))):
            if(nums1[i] < nums2[j]) | (nums1[i] == key):
                i += 1
            elif (nums1[i] > nums2[j]) | (nums2[j] == key):
                j += 1
            else:
                c.append(nums1[i])
                key = nums1[i]
                i += 1
                j += 1
        return c
    
#    def intersection2(self, nums1, nums2):
#        return list(set(nums1) & set(nums2))
#test  = Solution()
#print(test.intersection([1,2,2,3],[2,2]))
#print(test.intersection2([1,2,2,3],[2,2]))