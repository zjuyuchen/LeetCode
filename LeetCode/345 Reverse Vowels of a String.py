# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:02:41 2017

@author: yc
"""
#Two points solution, however need extra space for list[s]
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        s = list(s)
        i, j = 0, len(s)-1
        while(i<j):
            if s[i] in vowels:
                if s[j] in vowels:
                    s[i], s[j] = s[j], s[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        return ''.join(s)
#test = Solution()
#print(test.reverseVowels('Leetcode'))
                
            