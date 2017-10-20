# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 01:27:02 2017

@author: yc
"""
#Only take several minus, great！ 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.a = 0
        def conv(root):
            if root:
                conv(root.right)
                root.val += self.a
                self.a = root.val
                conv(root.left)
            return root
        conv(root)
        return root