# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 12:37:09 2017

@author: yc
"""

class Solution(object):
    def judgeCircle(self, moves):
        pos = [0, 0]
        str = list(moves)
        for i in str:
            if i=='U':
                pos[1]+=1
            elif i=='D':
                pos[1]-=1
            elif i=='L':
                pos[0]-=1;
            else:
                pos[0]+=1;
        return pos == [0,0]
    
#test = Solution()
#print(test.judgeCircle("UD"))
#print(test.judgeCircle("LL"))               