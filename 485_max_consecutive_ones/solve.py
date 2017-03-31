#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cur = 0
        cnt = 0
        for c in nums:
            if c == 1:
                cnt += 1
            else:
                max_cur = max(max_cur, cnt)
                cnt = 0
        max_cur = max(cnt, max_cur)
        return max_cur


s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(s.findMaxConsecutiveOnes([0, 0, 0]))
