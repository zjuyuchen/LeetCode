# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:14:06 2017

@author: yc
"""
#题目的目的是不使用迭代输出中序遍历
#这里使用栈来实现


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        li = []
        stack = []
        temp = root
        while(temp or stack):
            while temp:
                stack.append(temp)
                temp = temp.left
            temp  = stack.pop()
            li.append(temp.val)
            temp = temp.right
        return li
        