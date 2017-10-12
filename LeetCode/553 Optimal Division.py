# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:24:30 2017

@author: yc
"""
#no parenthesis is the smallest!!! 2/3/4/5/6, due to all nums are positive intergers.
#so s[0]/smallest(s[1:])
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''
        s = map(str,nums)
        l = len(s)
        if s == 2:
            return s[0] + '/' + s[1]
        else:
            return '{}/({})'.format(s[0],'/'.join(s[1:]))
