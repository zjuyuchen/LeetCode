# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:12:37 2017

@author: yc
"""
#divide to left and right part.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = len(strs)
        if l == 0:
            return ''
        minl = min([len(strs[i]) for i in range(l)])
        mid = minl//2
        if minl == 0:
            return ''
        elif minl == 1:
            return strs[0][0] if len(set([strs[i][0] for i in range(l)])) == 1 else ''
        elif len(set([strs[i][:mid] for i in range(l)])) == 1:
            return strs[0][:mid] + self.longestCommonPrefix([strs[i][mid:] for i in range(l)])
        else:
            return self.longestCommonPrefix([strs[i][:mid] for i in range(l)])
        
test = Solution()
print(test.longestCommonPrefix(['ba','']))