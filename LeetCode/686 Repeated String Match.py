# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:21:47 2017

@author: yc
"""

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if not A and not B:
            return 1
        elif not A:
            return -1
        elif len(A) > len(B):
            if B not in A:
                if B not in A*2:
                    return -1
                else:
                    return 2
            else:
                return 1
        else:
            time = len(B)//len(A)
            if B not in A*time:
                time += 1
                if B not in A*time:
                    return -1
        return time
#test = Solution()
#print(test.repeatedStringMatch('aa','a'))
            