# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:59:28 2017

@author: Administrator
"""
#Thanks StefanPochmann, origin from his idea.
#Go through all the possible time.
#class Solution(object):
#    def readBinaryWatch(self, num):
#        """
#        :type num: int
#        :rtype: List[str]
#        """
#        result = []
#        for i in range(12):
#            for j in range(60):
#                if (bin(i)+bin(j)).count('1') == num:
#                    result.append('%d:%02d' % (i, j))
#        return result
s = 'Hello'
s[1] = 'd'
print(s[1])