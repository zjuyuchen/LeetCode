# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 01:56:46 2017

@author: yc
"""

#半夜不适合编程序，早上两分钟的事情，晚上用了二十分钟没解决。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        info = []
        def bot(node, depth=0):
            if node:
                if len(info) <= depth:  #注意这里的等于号
                    info.append([node.val])
                else:
                    info[depth].append(node.val)
                bot(node.left, depth+1)
                bot(node.right, depth +1)
        bot(root)
        return info[::-1]