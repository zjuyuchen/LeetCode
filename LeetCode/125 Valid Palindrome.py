# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:05:52 2017

@author: yc
"""

#class Solution(object):
#    def isPalindrome(self, s):
#        """
#        :type s: str
#        :rtype: bool
#        """
#        if not s:
#            return True
#        if set(s) == {' '}:
#            return True
#        alpha_a = [chr(ord('a')+i) for i in range(26)]
#        alpha_A = [chr(ord('A')+i) for i in range(26)]
#        nums = [str(i) for i in range(10)]
#        dis = ord('A') - ord('a')
#        test = []
#        for i in s:
#            if i in alpha_A:
#                test.append(chr(ord(i)-dis))
#            elif i in alpha_a:
#                test.append(i)
#            elif i in nums:
#                test.append(i)
#        def isP(a):
#            return all(a[i] == a[len(a)-1-i] for i in range(len(a)//2))
#        return isP(test)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if set(s) == {' '}:
            return True
        test = []
        for i in s:
            if i.lower().isalnum():
                test.append(i.lower())
        def isP(a):
            return all(a[i] == a[len(a)-1-i] for i in range(len(a)//2))
        return isP(test)
test = Solution()
print(test.isPalindrome("aA"))