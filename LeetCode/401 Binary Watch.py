# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 01:13:25 2017

@author: Administrator
"""

#Thanks StefanPochmann, origin from his idea.
#Go through all the possible time.
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for i in range(12):
            for j in range(60):
                if (bin(i)+bin(j)).count('1') == num:
                    result.append('%d:%02d' % (i, j))
        return result