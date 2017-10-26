# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:15:14 2017

@author: yc
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        mi, ma = min(p.val,q.val), max(p.val, q.val)
        if mi <= root.val <= ma:
            return root.val
        if ma < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if mi > root.val:
            return self.lowestCommonAncestor(root.right, p, q)