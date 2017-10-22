# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:21:08 2017

@author: yc
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def generateRow(lastrow):
            row = [0 for i in range(len(lastrow) + 1)]
            row[0] = lastrow[0]
            row[-1] = lastrow[-1]
            for i in range(1,len(lastrow)):
                row[i] = lastrow[i-1] + lastrow[i]
            return row
        if numRows == 0:
            return [[]]
        elif numRows == 1:
            return [[1]]
        else:
            result = [[1]]
            for i in range(1,numRows):
                result.append(generateRow(result[i-1]))
            return result
test = Solution()
print(test.generate(5))