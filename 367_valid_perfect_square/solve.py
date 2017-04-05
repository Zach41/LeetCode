#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = (num + 1) // 2
        l = 1

        while l < r:
            mid = l + (r - l) // 2
            tmp = mid * mid
            if tmp == num:
                return True
            elif tmp > num:
                r = mid - 1
            else:
                l = mid + 1
        return l*l == num

s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
