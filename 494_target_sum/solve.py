#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        tot = sum(nums)
        if tot < S or not nums or (tot + S) % 2:
            return 0
        sum_p = (sum(nums) + S) // 2
        dp = [0 for _ in range(sum_p + 1)]
        dp[0] = 1
        for v in nums:
            for k in range(sum_p, v-1, -1):
                dp[k] += dp[k - v]
        return dp[sum_p]


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
