# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:10:48 2017

@author: yc
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = root = ListNode(0)
        while(l1 and l2):
            if l1.val < l2.val:
                root.next = l1
                l1 = l1.next
            else:
                root.next = l2
                l2 = l2.next
            root = root.next
        root.next = l1 or l2
        return res.next 
            