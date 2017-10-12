# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:11:42 2017

@author: Administrator
"""
#Store p in a dic.
#Then store s[:len(p)] in dic_s
#if dic_s == dic, the append i
##important!!! when i ++, we do not need to check s[i:i+len(p)], we just minus1 or remote dic_s[s[i-1]]
#and add dic_s[s[i]].
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        dic_s = {}
        dic = {}
        for i in p:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in s[:len(p)]:
            if j in dic_s:
                dic_s[j] += 1
            else:
                dic_s[j] = 1
        i = 0
        while(i<len(s)-len(p)):
            if dic_s == dic:
                res.append(i)
            i += 1
            dic_s[s[i-1]] -= 1
            if dic_s[s[i-1]] == 0:
                dic_s.pop(s[i-1])
            if s[i+len(p)-1] in dic_s:
                dic_s[s[i+len(p)-1]] += 1
            else:
                dic_s[s[i+len(p)-1]] = 1
        if dic_s == dic:
            res.append(i)
        return res
test = Solution()
print(test.findAnagrams("ababab","ab"))
            
            