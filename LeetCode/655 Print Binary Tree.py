# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:36:23 2017

@author: yc
"""

# This problem takes me 2 hours, finally I give it up..
#Thanks lee215

def printTree(self, root):
        if not root: return [""]

        def depth(root):
            if not root: return 0
            return max(depth(root.left), depth(root.right)) + 1

        d = depth(root)
        self.res = [[""] * (2**d - 1) for _ in xrange(d)]

        def helper(node, d, pos):
            self.res[-d - 1][pos] = str(node.val)
            if node.left: helper(node.left, d - 1, pos - 2**(d - 1))
            if node.right: helper(node.right, d - 1, pos + 2**(d - 1))

        helper(root, d - 1, 2**(d - 1) - 1)
        return self.res