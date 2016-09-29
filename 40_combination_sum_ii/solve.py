#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def combinationSum2(self, candidates, target):
        ans, n = [], len(candidates)

        candidates.sort()

        def dfs(idx, target, path):
            if target == 0:
                ans.append(path)
                return
            if target < 0:
                return

            for i in range(idx, n, 1):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, target - candidates[i], path + [candidates[i]])
            

        dfs(0, target, [])
        return ans

s = Solution()
import pdb
pdb.set_trace()
print s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
