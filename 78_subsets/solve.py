#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = 2**(len(nums))
        l = len(nums)
        
        ans = []
        for i in range(n):
            tmp = []
            for j in range(l):
                if (i >> j) & 1:
                    tmp.append(nums[j])
            ans.append(tmp)
        return ans

    def subsets(self, nums):
        ans = [[]]

        for i in range(len(nums)):
            tmp = [x[:] for x in ans]
            for x in tmp:
                x.append(nums[i])
            ans.extend(tmp)
        return ans

s = Solution()
import pdb
pdb.set_trace()
print s.subsets([1, 2, 3])
