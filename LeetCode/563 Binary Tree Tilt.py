# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 00:58:15 2017

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def sumOfChild(root):
            if not root:
                return 0
            left = sumOfChild(root.left)
            right = sumOfChild(root.right)
            self.result += abs(left - right)
            return root.val + left + right
        sumOfChild(root)
        return self.result