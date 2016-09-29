#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def generateMatrix(self, n):
        if n == 0:
            return []

        flag = [0] * (n*n)
        curDir = 1
        pos = (0, 0)
        ans = [[0] * n for _ in range(n)]

        for i in range(1, n*n+1):
            x, y = pos
            ans[x][y] = i
            flag[n*x+y] = 1
            x, y = self.nextStep(curDir, pos)
            if x >= n or y >=n or x < 0 or y < 0 or flag[n*x+y] == 1:
                curDir = self.changeDir(curDir)
                x, y = self.nextStep(curDir, pos)
                if x >= n or y >=n or x < 0 or y < 0 or flag[n*x + y] == 1:
                    break
                pos = (x, y)
            else:
                 pos = (x, y)

        return ans

    def changeDir(self, curDir):
        curDir += 1

        if curDir == 5:
            return 1
        else:
            return curDir

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

print s.generateMatrix(3)
print s.generateMatrix(4)
print s.generateMatrix(2)
print s.generateMatrix(1)
