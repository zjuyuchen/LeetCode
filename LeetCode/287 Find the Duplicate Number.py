# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:34:10 2017

@author: Demo
"""
#看到这种n+1大小的数组包含n个数字的题目，可以考虑用元素代表下标来构造一个链表！
#数组中必然包括一个重复的数字，也就是说构造出来的链表是有环的，余下的任务就用classical solution找到环的入口！
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[slow]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while(fast != slow):
            fast = nums[fast]
            slow = nums[slow]
        return fast
    