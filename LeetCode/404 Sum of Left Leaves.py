# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 00:03:15 2017

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def nochild(root):
            if root.left == None and root.right == None:
                return True
            return False
        if not root:
            return 0
        elif root.left == None:
            return self.sumOfLeftLeaves(root.right)
        elif nochild(root.left):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)