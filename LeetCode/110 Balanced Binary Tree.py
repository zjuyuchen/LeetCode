# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 23:02:28 2017

@author: yc
"""
#BalencedTree的定义是：任何Node!!!!的左右孩子深度不能相差大于1！！

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.dep(root.left)-self.dep(root.right)) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def dep(self,root):
        if not root:
            return 0
        return 1 + max(self.dep(root.left), self.dep(root.right))

#
#
##我不知道为啥不能通过！！！！
#
## Definition for a binary tree node.
#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
#
#class Solution(object):
#    def isBalanced(self, root):
#        """
#        :type root: TreeNode
#        :rtype: bool
#        """
#        if not root:
#            return True
#        print(self.dep(root.left)-self.dep(root.right))
#        return abs(self.dep(root.left)-self.dep(root.right)) <=1
#    def dep(self,root):
#        if not root:
#            return 0
#        return 1 + max(self.dep(root.left), self.dep(root.right))
##    def inO(self, root):
##        if root:
##            self.inO(root.left)
##            print(root.val)
##            self.inO(root.right)
##test = Solution()
##tree = TreeNode(1)
##tree.left = TreeNode(2)
##tree.left.left = TreeNode(3)
##tree.left.left.left = TreeNode(4)
##tree.left.left.left.right = TreeNode(4)
##tree.right = TreeNode(2)
##tree.right.right = TreeNode(3)
##tree.right.right.right = TreeNode(4)
##tree.right.right.right.right = TreeNode(4)
##test.inO(tree)
##print(test.isBalanced(tree))