#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.step(k, n, [], 1)
        return self.ans

    def step(self, k, n, cur, start):
        """
        注意在传数组参数的时候仍然是引用数组，所以一定要深复制
        """
        if n <=0 or k<=0:
            if k == 0 and n == 0:
                self.ans.append(cur)
            return
        for i in range(start, 10):
            tmp = cur[:] + [i]
            self.step(k-1, n-i, tmp, i+1)


s = Solution()
import pdb
pdb.set_trace()
print s.combinationSum3(3, 7)
        
