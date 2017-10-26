# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:38:35 2017

@author: yc
"""

#路径要么包含node（），要么不包含(pathSum(node.right,sum) + pathSum(node.left,sum))
#如果包含node，就要用findPath去计算，是否存在从node往下连续经过的节点之和等于sum的路径。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def findpath(root,s):
            if not root:
                return 0
            return int(root.val == s) + findpath(root.left,s-root.val) + findpath(root.right, s-root.val)
        if not root:
            return 0
        return findpath(root,s) + self.pathSum(root.left, s) + self.pathSum(root.right,s)