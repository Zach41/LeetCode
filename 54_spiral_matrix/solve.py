#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        curDir = 1
        pos = (0, 0)
        flag = [[0] * n for _ in range(m)]
        ans = []
        while True:
            x, y = pos
            ans.append(matrix[x][y])
            flag[x][y] = 1

            x, y = self.nextStep(curDir, pos)
            if x >= m or y >= n or y < 0 or x < 0 or flag[x][y] == 1:
                curDir = self.changeDir(curDir)
                x, y = self.nextStep(curDir, pos)
                if x >= m or y >= n or y < 0 or x < 0 or flag[x][y] == 1:
                    break
                pos = self.nextStep(curDir, pos)                
            else:
                pos = (x, y)
        return ans
                
    def changeDir(self, curDir):
        newDir = curDir + 1

        if newDir == 5:
            return 1
        else:
            return newDir

    def nextStep(self, curDir, point):
        if curDir == 1:
            return (point[0], point[1]+1)
        if curDir == 2:
            return (point[0]+1, point[1])
        if curDir == 3:
            return (point[0], point[1]-1)
        if curDir == 4:
            return (point[0]-1, point[1])


s = Solution()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
import pdb
pdb.set_trace()
print s.spiralOrder(matrix)
