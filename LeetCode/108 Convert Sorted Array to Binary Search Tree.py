# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 23:00:09 2017

@author: yc
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        else:
            middle = len(nums)//2
            left = nums[:middle]
            right = nums[middle+1:]
            c = TreeNode(nums[middle])
            c.left = self.sortedArrayToBST(left)
            c.right = self.sortedArrayToBST(right)
        return c
        