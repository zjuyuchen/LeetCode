# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:52:48 2017

@author: yc
"""
#哈哈，感觉自己挺聪明的 [0], [1], [1,2], [1,2,2,3], [[1,2,2,3]+[i+1 for i in [1,2,2,3]]]....


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        a = [0, 1]
        b = [1]
        while(True):
            b = b + [i+1 for i in b]
            i = 0
            while(i<len(b) and len(a) < num+1):
                a.append(b[i])
                i += 1
            if len(a) == num+1:
                break
        return a