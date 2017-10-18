# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:14:40 2017

@author: yc
"""

#深度优先搜索，先给把右孩子的值赋给该层的纪录值，如果存在左孩子，
#则把左孩子的值赋给纪录值。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        info = []
        def dfs(node, depth=0):
            if node:
                if len(info)<=depth:
                    info.append([0,0])
                info[depth][0] = node.val
                info[depth][1] +=1
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)
        dfs(root)
        return info[-1][0]
            