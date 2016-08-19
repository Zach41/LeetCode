#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def superPow(self, a, b):
        def quickPow(a, b):
            ans = 1
            base = a

            while b:
                if b % 2:
                    ans *= base
                base = base*base
                b /= 2
            return ans

        ans = 1
        for x in b[::-1]:
            ans = ans * quickPow(a, x) % 1337
            a   = quickPow(a, 10) % 1337
        return ans % 1337

s = Solution()
import pdb
pdb.set_trace()
print s.superPow(2, [1, 0])
print s.superPow(12, [1, 0, 2, 4])
            
