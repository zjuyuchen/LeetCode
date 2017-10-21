# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 10:32:55 2017

@author: yc
"""

#将二叉树转化为字符串，关键是要把根节点，左右节点都做标记。

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
        
        return convert(t) in convert(s)