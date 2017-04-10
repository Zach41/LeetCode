#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bisect import bisect_left


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            pos = bisect_left(row, target)
            if pos < len(row) and row[pos] == target:
                return True

        return False

    def searchMatrix2(self, matrix, target):
        # O(m+n) version
        if len(matrix) == 0 or not matrix:
            return False
        col = len(matrix[0]) - 1
        row = 0

        while col >= 0 and row < len(matrix):
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False


s = Solution()

print(
    s.searchMatrix2([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
print(
    s.searchMatrix2([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
