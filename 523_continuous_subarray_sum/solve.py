#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pos_dict = {0: -1}
        cur_sum = 0
        for (idx, v) in enumerate(nums):
            cur_sum += v
            if k != 0:
                cur_sum %= k
            if cur_sum in pos_dict:
                if idx - pos_dict[cur_sum] > 1:
                    return True
            else:
                pos_dict[cur_sum] = idx
        return False


s = Solution()
print(s.checkSubarraySum([23, 2, 4, 6, 7], 6))
import pdb
pdb.set_trace()
print(s.checkSubarraySum([1, 1], 2))
print("TEST2:")
print(s.checkSubarraySum([23, 2, 6, 4, 7], 6))
