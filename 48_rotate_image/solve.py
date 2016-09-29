#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def rotate(self, matrix):
        if not matrix:
            return None

        n = len(matrix)

        ans = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            row = matrix[i]
            for j in range(n):
                col = n-1-i
                ans[j][col] = row[j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = ans[i][j]

    def rotate2(self, matrix):
        ''' in place version '''
        if not matrix:
            return None
        n = len(matrix)
        
        matrix.reverse()
        for i in range(0, n):
            for j in range(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        print matrix
        
        
        

s = Solution()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate2(matrix)

        
