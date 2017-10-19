# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:42:45 2017

@author: yc
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def su(node):
            if not node:
                return 0
            s = node.val + su(node.left) + su(node.right)
            dic[s] += 1
            return s
        dic = collections.Counter()
        if not root:
            return []
        su(root)
        mx = max(dic.values())
        return [v for v in dic if dic[v] == mx]