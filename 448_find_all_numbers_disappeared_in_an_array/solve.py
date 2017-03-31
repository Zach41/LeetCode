#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            nums[(nums[i] - 1) % n] += n
        rec = []
        for i in range(n):
            if nums[i] <= n:
                rec.append(i+1)
        return rec
