#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        num_map = {}

        n = len(nums)

        for i in range(n):
            if num_map.has_key(nums[i]):
                num_map[nums[i]].append(i)
            else:
                num_map[nums[i]] = [i]

        for key in num_map.keys():
            arr = num_map[key]
            for i in range(len(arr)-1):
                if arr[i+1] - arr[i] <=k:
                    return True
                
        return False

s = Solution()
print s.containsNearbyDuplicate([], 2)
print s.containsNearbyDuplicate([1, 2, 3, 1, 4, 2], 4)
print s.containsNearbyDuplicate([1, 2, 3, 1, 4, 2], 1)
