#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return;
        m, n = len(board), len(board[0])

        tmp_board = [ x[:] for x in board]
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if self._check(tmp_board, (i, j)) else 0
        self.board = board
        
                

    def _check(self, board, pos):
        x, y = pos
        m, n = len(board), len(board[0])
        cnt_live, cnt_dead = 0, 0
        pos_off = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        for off in pos_off:
            x1 = x + off[0]
            y1 = y + off[1]

            if x1<0 or x1>=m or y1<0 or y1>=n:
                continue
            if board[x1][y1] == 0:
                cnt_dead += 1
            else:
                cnt_live += 1
        if board[x][y] == 1:
            if cnt_live < 2:
                return False
            elif cnt_live <= 3:
                return True
            else:
                return False
        else:
            if cnt_live == 3:
                return True
            else:
                return False
        return False

    def _check2(self, board, pos):
        x, y = pos
        m, n = len(board), len(board[0])
        cnt_live, cnt_dead = 0, 0
        pos_off = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        for off in pos_off:
            x1 = x + off[0]
            y1 = y + off[1]

            if x1<0 or x1>=m or y1<0 or y1>=n:
                continue
            if board[x1][y1] == 1 or board[x1][y1] == 2:
                cnt_live += 1
            else:
                cnt_live += 1
        if board[x][y] == 1:
            if cnt_live < 2:
                return False
            elif cnt_live <= 3:
                return True
            else:
                return False
        else:
            if cnt_live == 3:
                return True
            else:
                return False
        return False

    def gameOfLife2(self, board):
        """ in-place solution"""
        if not board:
            return [[]]
        m, n = len(board), len(board[0])
        pos_off = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        for x in range(m):
            for y in range(n):
                cnt_live = 0
                cnt_dead = 0
                for off in pos_off:
                    x1 = x + off[0]
                    y1 = y + off[1]
                    if x1 < 0 or x1>=m or y1<0 or y1>=n:
                        continue
                    if board[x1][y1] ==1 or board[x1][y1] == 2:
                        cnt_live += 1
                    else:
                        cnt_dead += 1
                if board[x][y] == 1:
                    if cnt_live < 2:
                        board[x][y] = 2
                    elif cnt_live <= 3:
                        board[x][y] = 1
                    else:
                        board[x][y] = 2
                else:
                    if cnt_live == 3:
                        board[x][y] = 3
                    else:
                        board[x][y] = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1 or board[i][j] == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        self.board = board
                    


s = Solution()
board = [[1, 1, 0, 1, 0],
         [0, 1, 0, 1, 0],
         [0, 0, 1, 1, 0],
         [0, 0, 0, 0, 0]]

board2 = [[1]]
board3 = [[0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0]]

import pdb
pdb.set_trace()
s.gameOfLife(board)
print s.board
s.gameOfLife(board2)
print s.board
s.gameOfLife2(board3)
print s.board
