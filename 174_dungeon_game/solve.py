#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        MAX_INT = 2**32
        hp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(n+1):
            hp[m][i] = MAX_INT
        for i in range(m+1):
            hp[i][n] = MAX_INT
        hp[m-1][n] = 1
        hp[m][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need = min(hp[i+1][j], hp[i][j+1]) - dungeon[i][j]
                hp[i][j] = 1 if need <= 0 else need

        return hp[0][0]


s = Solution()
print(s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
print(s.calculateMinimumHP([[1, -3, 2], [0, -1, 2], [0, 0, -2]]))
