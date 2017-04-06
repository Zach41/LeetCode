#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        if row > col:
            matrix = self.transpose(matrix)
            row, col = col, row
        ans = -2**32

        for l in range(row):
            sums = [0] * col
            for r in range(l, row):
                curSum = 0
                accu = [0]

                for i in range(col):
                    sums[i] += matrix[r][i]
                cur_max = -2**32

                for val in sums:
                    curSum += val
                    idx = bisect.bisect_left(accu, curSum - k)
                    if (idx < len(accu)):
                        cur_max = max(cur_max, curSum - accu[idx])
                    bisect.insort_left(accu, curSum)
                ans = max(ans, cur_max)
        return ans

    def transpose(self, matrix):
        return [list(row) for row in zip(*matrix)]


s = Solution()
print(s.maxSumSubmatrix([[2, 2, -1]], 0))
print(s.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))
