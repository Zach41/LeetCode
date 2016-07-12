#!/usr/bin/env python
# -*- coding : utf-8 -*-

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        A = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if j == 0:
                    A[i][j] = 1 if matrix[i][j] == '1' else 0
                else:
                    if matrix[i][j] != '0':
                        A[i][j] = A[i][j-1] + int(matrix[i][j])

        A.append([-1]*n)
        max_area = 0

        for i in range(n):
            max_area = max(max_area, self.largestArea(A, i, m))
        return max_area

    def largestArea(self, A, j, m):
        stack = []
        max_area = 0
        for i in range(m+1):
            while len(stack) != 0 and A[i][j]<= A[stack[-1]][j]:
                h = A[stack.pop()][j]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                max_area = max(max_area, h*w)
            stack.append(i)
        return max_area

s = Solution()
matrix = ['0110', '1011', '0011']
matrix2 = ["01101","11010","01110","11110","11111","00000"]
import pdb
pdb.set_trace()
print s.maximalRectangle(matrix)
print s.maximalRectangle(matrix2)
                    
