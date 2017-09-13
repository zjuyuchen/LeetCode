# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:32:49 2017

@author: 126PC-3
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def cap(w):
            if not w:
                return False
            if 'Z' >= w >= 'A':
                return True
            else:
                return False
        if not word:
            return False
        elif cap(word[0]):
            if len(word) == 1:
                return True
            elif cap(word[1]):
                i = 2
                while(i < len(word) and cap(word[i])):
                    i += 1
                if i == len(word):
                    return True
                else:
                    return False
            else:
                i = 2
                while(i < len(word) and not cap(word[i])):
                    i += 1
                if i == len(word):
                    return True
                else:
                    return False
        else:
            i = 1
            while(i < len(word) and not cap(word[i])):
                i += 1
            if i == len(word):
                return True
            else:
                return False
    

#test  = Solution()
#print(test.detectCapitalUse('G'))