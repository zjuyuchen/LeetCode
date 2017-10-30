# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:54:40 2017

@author: Demo
"""
#对于树来说，能用递归就用递归。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        if not root:
            return ['']
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
        d = depth(root)
        res = [['']*(2**d-1) for i in range(d)]
        def prints(node, d, pos):
            res[-d][pos] = str(node.val)
            if node.left:
                prints(node.left, d - 1, pos - 2**(d-2))
            if node.right:
                prints(node.right, d - 1, pos + 2**(d-2))
        prints(root, d, 2**(d-1)-1)
        return res
                