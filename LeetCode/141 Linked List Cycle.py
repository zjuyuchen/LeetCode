# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:14:35 2017

@author: Demo
"""

# This is a classical solution to determine if there exist circle in a datastructure!

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head.next
            fast = slow.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
    
        