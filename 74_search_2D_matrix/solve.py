#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        lasts = [row[-1] for row in matrix]
        row   = self.findRow(lasts, target)

        if row == -1:
            return False

        return self.findValue(matrix[row], target)

    def findValue(self, row, target):
        l, r = 0, len(row)-1

        while l < r:
            mid = (l + r) / 2
            if (row[mid] == target):
                return True
            if row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if row[l] == target:
            return True
        return False

    def findRow(self, lasts, target):
        for i in range(len(lasts)):
            if lasts[i] >= target:
                return i
        return -1

s = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]

print s.searchMatrix(matrix, 4)
    
