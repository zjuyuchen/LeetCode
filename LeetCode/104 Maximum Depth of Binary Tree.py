# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 23:32:05 2017

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dep(root):
            if not root:
                return 0
            else:
                return 1 + max(dep(root.left),dep(root.right))
        return dep(root)
            