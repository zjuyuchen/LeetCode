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
        dic = []
        def InOrderWalk(node, k):
            if node:
                a = InOrderWalk(node.left)
                if node.val in dic: 
                    return True
                else:
                    dic.append(k-node.val)
                b = InOrderWalk(node.right)
                if a or b:
                    return True
        return InOrderWalk(root, k)
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
test = Solution()
print(test.findTarget(root,4))