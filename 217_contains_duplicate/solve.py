#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt_map = {}
        for num in nums:
            cnt = cnt_map.get(num, 0)
            if cnt > 0:
                return True
            else:
                cnt_map[num] = cnt+1
        return False

s = Solution()
print s.containsDuplicate([])
print s.containsDuplicate([1, 2, 3, 4])
print s.containsDuplicate([1, 2, 2, 4])
            
