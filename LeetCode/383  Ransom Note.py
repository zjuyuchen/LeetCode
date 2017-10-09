# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:24:53 2017

@author: yc
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        def contain(a,word):
            l1 = len(a)
            l2 = len(word)
            bol = False
            l = 0 
            while(l<=l2-l1):
                c = word[l:l+l1]
                if a == c:
                    bol = True
                    break
                else:
                    l += 1
            return bol
        a = ransomNote.split(" ")
        b = magazine.split(" ")
        for i in a:
            for j in b:
                if not contain(i,j):
                    return False
        return True
test = Solution()
print(test.canConstruct("aa cc","aa cc"))