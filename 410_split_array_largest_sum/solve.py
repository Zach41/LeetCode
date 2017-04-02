#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if m >= len(nums):
            return max(nums)
        cur, sums, n = 0, [0], len(nums)
        for v in nums:
            cur += v
            sums.append(cur)

        dp = [sums[:], [0]*len(sums)]
        cur = 0
        import pdb
        pdb.set_trace()
        for m0 in range(2, m + 1):
            for n0 in range(m0, n + 1):
                large_sum = max(dp[cur][m0 - 1], sums[n0] - sums[m0 - 1])
                for idx in range(m0, n0):
                    large_sum = min(
                        max(dp[cur][idx], sums[n0] - sums[idx]), large_sum)
                dp[1-cur][n0] = large_sum
            cur = 1-cur
        return dp[cur][n]


s = Solution()
print(s.splitArray([7, 2, 5, 10, 8], 2))
