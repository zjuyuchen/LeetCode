# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 00:12:39 2017

@author: Administrator
"""

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def returnXY(com):
            x = ''
            y = ''
            i = 0
            while(com[i] != '+'):
                x += com[i]
                i += 1
            i += 1
            while(com[i] != 'i'):
                y += com[i]
                i += 1
            return [int(x), int(y)]
        at = returnXY(a)
        bt = returnXY(b)
        x = at[0]*bt[0] - at[1]*bt[1]
        y = at[0]*bt[1] + at[1]*bt[0]
#        return str(x)+'+'+str(y)+'i'
#        return '{}+{}i'.format(x, y)
        return '%d+%di' % (x,y)
test = Solution()
print(test.complexNumberMultiply('1+1i','1+1i'))
    