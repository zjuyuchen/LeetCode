# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 20:35:53 2017

@author: yc
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        k = 0
        count = m
        while(j<n and (k-j)<m):
            print(nums1,nums2[j],nums1[k],j,k)
            if nums2[j] < nums1[k]:
                nums1[k+1:count+1] = nums1[k:count]
                nums1[k] = nums2[j]
                j += 1
                k += 1
                count += 1
            else:
                k += 1
        if j<n:
            nums1[k:k+n-j] = nums2[j:n]
        return nums1
#test = Solution()
#print(test.merge([1,2,3,4,0,0,0,0,0,0,0],4,[1,2,3,4,6],5))