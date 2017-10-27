# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:16:47 2017

@author: yc
"""
#别人的算法，不需要更改board，很简洁。不明白的是为啥我复制的是30ms的，但我自己运行就是82ms，3.2%？？
class Solution(object):
    def countBattleships(self, board):
        battleships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X" and (i == 0 or board[i-1][j] == ".") and (j == 0 or board[i][j-1] == "."):
                    battleships += 1
                    
        return battleships
            



#深度优先搜索，但是更改了board的内容。21%，很慢。


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    count += 1
                    m = i
                    n = j
                    while(m+1<len(board) and n < len(board[0]) and board[m+1][n] == 'X'):
                        board[m+1][n] = '.'
                        m += 1
                    while(m<len(board) and n+1 < len(board[0]) and board[m][n+1] == 'X'):
                        board[m][n+1] = '.'
                        n += 1
        return count
test = Solution()
print(test.countBattleships([['X','.', 'X'],['X','.','X']]))