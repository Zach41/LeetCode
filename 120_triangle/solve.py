#!/usr/bin/env python
# -*- coding : utf-8 -*-

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)

        if n == 0:
            return 0
        if n == 1:
            return triangle[0][0]

        dp = triangle[-1][:]

        for i in range(n-2, -1, -1):
            arr = triangle[i]
            for j in range(len(arr)):
                dp[j] = min(arr[j]+dp[j], arr[j]+dp[j+1])
        return dp[0]

s = Solution()
print s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
