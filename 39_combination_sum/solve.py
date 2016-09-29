#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def combinationSum(self, candidates, target):
        ans, n = [], len(candidates)

        def dfsSearch(idx, target, path):
            if target == 0:
                ans.append(path)
                return
            if target < 0 or idx >= n:
                return
            dfsSearch(idx+1, target, path)
            dfsSearch(idx, target - candidates[idx], path + [candidates[idx]])
        dfsSearch(0, target, [])
        return ans

s = Solution()
print s.combinationSum([2, 3, 6, 7], 7)
