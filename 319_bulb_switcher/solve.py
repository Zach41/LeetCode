#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Solution(object):
    def bulbSwitch_tle(self, n):
        tot = 0
        
        for x in range(1, n+1):
            cnt = 0
            i = 1
            while i*i <= x:
                if x % i == 0:
                    cnt += 2 if x/i != i else 1
                i += 1
            tot += 1 if cnt%2 == 1 else 0
        return tot

    def bulbSwitch(self, n):
        return int(math.sqrt(n))

s = Solution()
import pdb
pdb.set_trace()
print s.bulbSwitch(3)
print s.bulbSwitch(6)
print s.bulbSwitch(1)
            
