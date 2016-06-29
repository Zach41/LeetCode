#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isHappy(self, n):
        rec = set()

        rec.add(n)
        
        while True:
            sum = 0
            for c in str(n):
                sum += int(c) * int(c)
            if sum == 1:
                return True

            if sum in rec:
                return False
            n = sum
            rec.add(sum)

s = Solution()
import pdb
pdb.set_trace()
print s.isHappy(19)
print s.isHappy(14)
