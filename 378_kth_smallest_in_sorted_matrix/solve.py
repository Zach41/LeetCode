#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import PriorityQueue, Queue
from bisect import bisect_right


class Solution(object):
    def kthSmallest(self, matrix, k):
        # BFS
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        q = PriorityQueue()
        n = len(matrix)
        visited = {}
        q.put((matrix[0][0], (0, 0)))
        visited[0] = True

        while not q.empty():
            k -= 1
            top = q.get()
            if k == 0:
                return top[0]
            x, y = top[1][0], top[1][1]
            if x < n - 1 and not ((x + 1) * n + y) in visited:
                q.put((matrix[x + 1][y], (x + 1, y)))
                visited[(x + 1) * n + y] = True
            if y < n - 1 and not (x * n + y + 1) in visited:
                q.put((matrix[x][y + 1], (x, y + 1)))
                visited[x * n + y + 1] = True

    def kthSmallest2(self, matrix, k):
        # Binary search
        n = len(matrix)
        l, r = matrix[0][0], matrix[n - 1][n - 1]

        while l < r:
            mid = l + (r - l) // 2
            num = 0
            for i in range(n):
                num += bisect_right(matrix[i], mid)
            if num < k:
                l = mid + 1
            else:
                r = mid
        return l


s = Solution()
print(s.kthSmallest2([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
print(s.kthSmallest2([[1, 5, 9], [2, 6, 10], [3, 7, 11]], 8))
