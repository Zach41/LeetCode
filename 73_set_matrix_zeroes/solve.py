#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])


        flag1, flag2 = False, False
        for i in range(n):
            if matrix[0][i] == 0:
                flag1 = True
        for i in range(m):
            if matrix[i][0] == 0:
                flag2 = True
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        if flag1:
            for i in range(n):
                matrix[0][i] = 0
        if flag2:
            for i in range(m):
                matrix[i][0] = 0
        print matrix

s = Solution()

matrix = [[3, 0, 4], [1, 2, 0], [1, 1, 1]]
import pdb
pdb.set_trace()
s.setZeroes(matrix)

                    
        
