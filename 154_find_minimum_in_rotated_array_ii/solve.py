#!/usr/bin/env python
# -*- utf-8 -*-

class Solution(object):
    # O(n) version
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_e = nums[0]

        for num in nums:
            if min_e > num:
                min_e = num

        return min_e

s = Solution()
print s.findMin([4, 5, 6, 7, 0, 1, 2, 3])
