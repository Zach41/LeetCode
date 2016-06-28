#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        d = [0] * (n+1)
        for cite in citations:
            if cite > n:
                d[n] += 1
            else:
                d[cite-1] += 1
        sum = [0]*(n+1)
        sum[-1] = d[-1]
        for i in range(n-1, -1, -1):
            sum[i] = d[i] + sum[i+1]

        h_index = 0
        for i in range(1, n+1):
            if sum[i-1] >= i:
                h_index += 1
            else:
                break
        return h_index

s = Solution()
import pdb
pdb.set_trace()

print s.hIndex([1])
print s.hIndex([3, 0, 6, 1, 5])

        
