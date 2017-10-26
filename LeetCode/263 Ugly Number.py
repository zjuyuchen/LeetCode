# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:33:12 2017

@author: yc
"""

#浪费半小时。只要一直去用2，3，5去除，除到最后等于1就可以了。

class Solution(object):

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1
        
#        if num <=0:
#            return False
#        if num == 1:
#            return True
#        prime = set()
#        for i in range(7,int(num/2)+1):
#            j = 2
#            while(j<=(i/2)+1):
#                if i % j ==0:
#                    break
#                j += 1
#            if j == int(i/2)+2:
#                prime.add(i)
#        print(prime)
#        for i in range(2, int(math.sqrt(num))+1):
#            if num % i == 0 and (i in prime or num//i in prime):
#                return True
#        return False
#test = Solution()
#print(test.isUgly(214797179))