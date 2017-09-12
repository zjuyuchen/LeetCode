# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 00:28:36 2017

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def noChild(root):
            if root.left ==None and root.right == None:
                return True
        def dep(root):
            if not root:
                return 0
            elif noChild(root):
                return 1
            elif root.left == None and root.right:
                return 1 + dep(root.right)
            elif root.right == None and root.left:
                return 1 + dep(root.left)
            else:
                return 1 + min(dep(root.left),dep(root.right))
        if not root:
            return 0
        else:
            return dep(root)