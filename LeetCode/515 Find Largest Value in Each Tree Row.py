# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:47:19 2017

@author: yc
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        info = []
        def dfs(node, depth=0):
            if node:
                if len(info)<=depth:
                    info.append(-float('inf'))
                info[depth]= max(node.val, info[depth])
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)
        dfs(root)
        return info
    