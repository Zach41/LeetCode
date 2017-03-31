#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx1, idx2 = 0, len(numbers) - 1
        while idx1 < idx2:
            cur = numbers[idx1] + numbers[idx2]
            if cur == target:
                return [idx1+1, idx2+1]
            elif cur < target:
                idx1 += 1
            else:
                idx2 -= 1


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
