# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:02:38 2017

@author: yc
"""

#数组合并直接用a+b

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        if left == [] and right == []:
            return [str(root.val)]
        if left != [] and right == []:
            return [str(root.val) + '->' + i for i in left]
        if right != [] and left == []:
            return [str(root.val) + '->' + i for i in right]
        return [str(root.val) + '->' + i for i in left + right]