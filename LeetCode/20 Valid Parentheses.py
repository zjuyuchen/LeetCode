# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:51:28 2017

@author: yc
"""
#Push '([{' to a stack
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        for i in s:
            if i in ['[', '(', '{']:
                temp.append(i)
            else:
                if temp == []:
                    return False
                elif [temp[-1], i] in [['(',')'],['[',']'],['{','}']]:
                    del temp[-1]
                else:
                    return False
        if temp == []:
            return True
        else:
            return False
test = Solution()
print(test.isValid('{[{}]}()()[{}'))
