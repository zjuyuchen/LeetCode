# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 23:39:51 2017

@author: yc
"""
#class Solution(object):
#    def lengthOfLongestSubstring(self, s):
#        """
#        :type s: str
#        :rtype: int
#        """
#        res = 0
#        res_temp = {}
#        i = 0
#        while(i<len(s)):
#            if i < len(s)-1 and s[i] not in res_temp:
#                res_temp[s[i]] = i
#                i += 1
#            elif i == len(s)-1 and s[i] not in res_temp:
#                res_temp[s[i]] = i
#                res = max(res,len(res_temp))
#            else:
#                res = max(res,len(res_temp))
#                i = res_temp[s[i]] + 1
#                res_temp = {}
#        return res
                
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i= 0
        j = 0
        while(i<=j<len(s)):
            if s[j] not in s[i:j]:
                j += 1
            else:
                res = max(res, len(s[i:j]))
                i += 1
        return max(res, len(s[i:j]))

#test = Solution()
#print(test.lengthOfLongestSubstring('abcabcd'))