# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:24:44 2017

@author: yc
"""
# 先中序遍历整个二叉树，将每个元素存在a中
#在有序数列a中选择最小差值。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a = []
        def walkInOrder(root,a):
            if root.left:
                walkInOrder(root.left,a)
            a.append(root.val)
            if root.right:
                walkInOrder(root.right,a)
            return a
        walkInOrder(root,a)
        mi = float('inf')
        i = 0
        for i in range(len(a)-1):
            mi = min((a[i+1]-a[i]), mi)
        return mi
            
        