# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 00:37:48 2017

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def noChild(root):
            if root.left == None and root.right == None:
                return True
        if not t:
            return ''
        elif noChild(t):
            return str(t.val)
        elif t.left and t.right == None:
            return str(t.val) + '(' + str(self.tree2str(t.left)) +')'
        elif t.right and t.left == None:
            return str(t.val) + '()(' + str(self.tree2str(t.right)) +')'
        else:
            return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
            