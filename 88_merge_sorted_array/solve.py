#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i, j = m-1, n-1
        k    = m + n - 1

        while i >=0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

        while j>=0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        self.nums = nums1

s = Solution()
import pdb
pdb.set_trace()
s.merge([1], 1, [], 0)
print s.nums
s.merge([1, 3, 4, 0, 0, 0], 3, [2, 6, 8], 3)
print s.nums        
