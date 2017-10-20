# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 01:30:15 2017

@author: yc
"""

#about 10 mins。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def depth(node):
            if not node:return 0
            return max(depth(node.left),depth(node.right))+1
        l = depth(root.left)
        r = depth(root.right)
        if l  == r == 0:
            return 0
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), depth(root.left)+ depth(root.right))