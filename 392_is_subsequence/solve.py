#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from bisect import bisect_left

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ptr1, ptr2 = 0, 0
        while ptr1 < len(s):
            while ptr2 < len(t) and t[ptr2] != s[ptr1]:
                ptr2 += 1
            if ptr2 == len(t):
                return False
            ptr1 += 1
            ptr2 += 1

        return True

    def isSubsequence2(self, s, t):
        def createMap():
            posMap = defaultdict(list)
            for (i, c) in enumerate(t):
                posMap[c].append(i)
            return posMap
        posMap = createMap()
        lowBound = 0
        for c in s:
            if c not in posMap:
                return False
            chrList = posMap[c]
            r = bisect_left(chrList, lowBound)
            if r == len(chrList):
                return False
            lowBound = chrList[r] + 1
        return True


s = Solution()
print(s.isSubsequence2("abc", "ahbgdc"))
print(s.isSubsequence2("axc", "ahbgdc"))
