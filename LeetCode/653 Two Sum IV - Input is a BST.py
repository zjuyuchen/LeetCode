# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:38:31 2017

@author: yc
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.f = False
        dic = {}
        def InOrderWalk(node, k):
            if node:
                InOrderWalk(node.left, k)
                if node.val in dic: 
                    self.f = True
                else:
                    dic[k - node.val] = 1
                InOrderWalk(node.right, k)
        InOrderWalk(root, k)
        return self.f
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
test = Solution()
print(test.findTarget(root,4))