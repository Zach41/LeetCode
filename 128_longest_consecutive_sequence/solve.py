#!/usr/bin/env python
# -*- coding : utf-8 -*-

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        map_num = {}
        rec_map = {}
        for num in nums:
            if num not in map_num:
                map_num[num] = 1
        max_size = 1

        for e in nums:
            if e in rec_map:
                continue
            rec_map[e] = 1
            k = e-1
            tmp = 1
            while k in map_num:
                rec_map[k] = 1
                tmp += 1
                k = k-1
            k = e+1
            while k in map_num:
                rec_map[k] = 1
                tmp += 1
                k = k+1

            max_size = max(tmp, max_size)
        return max_size


s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 2, 3])
print s.longestConsecutive([1])
print s.longestConsecutive([])
print s.longestConsecutive([1, 2, 3, 4, 5, 6])
