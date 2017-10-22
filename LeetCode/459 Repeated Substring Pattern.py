# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:40:55 2017

@author: yc
"""
#24% not very fast
#split s by 2
#judge if them are the same, if yes, retur true
#else split s by 3
#...
#until split s by len(s)
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        k = 2
        m = l//k
        while(m != 0):
            if l % k ==0:
                test = [s[i*m:i*m+m] for i in range(k)]
                print(test)
                if len(set(test)) == 1:
                    return True
                else:
                    k += 1
                    m = l//k
            else:
                k += 1
                m = l//k
        return False
#test = Solution()
#print(test.repeatedSubstringPattern('aabaab'))

#a very nice idea:
# return s in 2*s[1:-1]
