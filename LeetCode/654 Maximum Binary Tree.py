# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 21:33:51 2017

@author: yc
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def construct(nums):
            if not nums:
                return
            elif len(nums) == 1:
                root = TreeNode(nums[0]) 
            else:
#                dic = {}
#                for i, n in enumerate(nums):
#                    dic[n] = i
#We can use nums.index(max(nums)) to instead that dic!
                ma= max(nums)
                i = nums.index(ma)
                root = TreeNode(ma)
                root.left = construct(nums[:i])
                root.right = construct(nums[i+1:])
            return root
        return construct(nums)
#test = Solution()
#root = test.constructMaximumBinaryTree([3,2,1,6,0,4])