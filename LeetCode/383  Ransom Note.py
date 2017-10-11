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
        dicr = {}
        for i in ransomNote:
            if i in dicr:
                dicr[i] += 1
            else:
                dicr[i] = 1
        dicm = {}
        for j in magazine:
            if j in dicm:
                dicm[j] += 1
            else:
                dicm[j] = 1
        for d in dicr:
            if d not in dicm or dicr[d]>dicm[d]:
                return False
        return True
#                
#test =  Solution()
#print(test.canConstruct('aa','aab'))