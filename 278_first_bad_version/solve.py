#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 19:
        return True
    return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


s = Solution()
print(s.firstBadVersion(20))
print(s.firstBadVersion(100))
