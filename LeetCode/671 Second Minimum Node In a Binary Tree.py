# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 01:56:15 2017

@author: yc
"""
#Takes about 10 mins

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        li = []
        def InOr(node):
            if node:
                InOr(node.left)
                li.append(node.val)
                InOr(node.right)
        InOr(root)
        i = 1
        li.sort()
        while(i < len(li) and li[i] <= li[i-1]):
            i += 1
        if i < len(li):
            return li[i]
        return -1