# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:31:27 2017

@author: yc
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh = len(haystack)
        ln = len(needle)
        if lh ==0 and ln == 0:
            return 0
        elif lh < ln:
            return -1
        elif ln == 0:
            return 0
        else:
            i = 0
            while(i+ln<=lh):
                if needle == haystack[i:i+ln]:
                    return i
                else:
                    i += 1
        return -1
test = Solution()
print(test.strStr('baa','ac'))