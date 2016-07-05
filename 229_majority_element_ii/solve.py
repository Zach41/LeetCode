#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        cnt_map = {}
        for num in nums:
            cnt = cnt_map.get(num, 0)
            cnt_map[num] = cnt+1
        ans = []
        for key in cnt_map.keys():
            if cnt_map[key] > n/3:
                ans.append(key)
        return ans

    def majorityElement2(self, nums):
        # O(1) space version
        n1, n2 = None, None
        c1, c2 = 0, 0
        n = len(nums)
        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 == 0:
                c1, n1 = 1, num
            elif c2 == 0:
                c2, n2 = 1, num
            else:
                c1, c2 = c1-1, c2-1
        return [x for x in [n1, n2] if x is not None and nums.count(x) > n/3]
    

s = Solution()
import pdb
pdb.set_trace()
print s.majorityElement2([1, 1, 1, 3, 3, 2, 2, 2])
print s.majorityElement2([1, 2, 2])
print s.majorityElement2([1, 2])
print s.majorityElement2([1])

