#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    if num > 6:
        return 1
    elif num < 6:
        return -1
    return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            guess_ret = guess(mid)
            if guess_ret == 0:
                return mid
            elif guess_ret == 1:
                r = mid - 1
            else:
                l = mid + 1
        return l


s = Solution()
import pdb
pdb.set_trace()
print(s.guessNumber(10))
