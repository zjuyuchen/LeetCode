# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:50:16 2017

@author: yc
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSy(root.left, root.right)
    def isSy(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.isSy(left.left, right.right) and self.isSy(left.right, right.left)
        return False