# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:14:39 2017

@author: Administrator
"""

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        i = 0
        score = 0
        c = []
        while(i<len(ops)):
            if  ops[i] == 'C':
                c = c[:-1]
            elif ops[i] != 'D' and ops[i] != '+':
                c.append(int(ops[i]))
            elif ops[i] == 'D':
                c.append(2*c[-1])
            else:
                c.append(c[-1]+c[-2])
            i += 1
        for i in c:
            score += i
        return score
test = Solution()
print(test.calPoints(["-60","D","-36","30","13","C","C","-33","53","79"]))
        
                
                
                