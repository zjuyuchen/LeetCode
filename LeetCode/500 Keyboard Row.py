# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:07:39 2017

@author: yc
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = set("qwertyuiopQWERTYUIOP")
        set2 = set("asdfghjklASDFGHJKL")
        set3 = set("zxcvbnmZXCVBNM")
        result =[]
        for w in words:
            alpha = set(w)
            if alpha.issubset(set1) | alpha.issubset(set2) | alpha.issubset(set3):
                result.append(w)
        return result
        