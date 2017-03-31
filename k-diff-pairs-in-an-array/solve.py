#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        ptr1, ptr2, n = 0, 1, len(nums)

        cnt = 0
        while ptr2 < n:
            if ptr1 == ptr2:
                ptr2 += 1
                continue
            if nums[ptr2] - nums[ptr1] == k:
                cnt += 1
                while ptr2 < n and nums[ptr2] - nums[ptr1] == k:
                    ptr2 += 1
            elif nums[ptr2] - nums[ptr1] < k:
                ptr2 += 1
            else:
                ptr1 += 1
        return cnt

    def findPairs2(self, nums, k):
        # O(n) solution
        if k > 0:
            return len(set(nums) & set(n + k for n in nums))
        elif k == 0:
            return sum(v > 1 for v in collections.Counter(nums).values())
        else:
            return 0


s = Solution()

print(s.findPairs2([3, 1, 4, 1, 5], 2))
print(s.findPairs2([1, 3, 1, 5, 4], 0))
print(s.findPairs2([1, 2, 3, 4, 5], 1))
print(s.findPairs2([1, 1, 1, 2, 2], 0))
