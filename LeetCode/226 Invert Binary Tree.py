# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:24:38 2017

@author: yc
"""

#比较简单的交换即可

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root
        root.left, root.right= self.invertTree(root.right), self.invertTree(root.left)
        return root
        