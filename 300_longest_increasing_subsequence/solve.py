#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bisect import bisect_left


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            max_l = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    max_l = max(dp[j] + 1, max_l)
            dp[i] = max_l
        return max(dp)

    def lengthOfLIS2(self, nums):
        # O(nlogn) version
        ans = []
        for val in nums:
            l = bisect_left(ans, val)
            if l == len(ans):
                ans.append(val)
            else:
                ans[l] = val
        return len(ans)


s = Solution()
print(s.lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))
