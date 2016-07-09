#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_map = {}

        for num in nums:
            cnt = num_map.get(num, 0)
            num_map[num] = cnt + 1

        ans = [[]]
        for key in num_map.keys():
            tmp1 = [x[:] for x in ans]
            tmp2 = [x[:] for x in ans]

            for x in tmp1:
                x.append(key)
            for i in range(2, num_map[key]+1):
                for x in tmp2:
                    tmp1.append(x+[key]*i)
            ans.extend(tmp1)
        return ans
                

s = Solution()
import pdb
pdb.set_trace()
print s.subsetsWithDup([1, 2, 2])
                
