#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)

        k = (m+n) / 2
        if (m+n) % 2 == 0:
            return (self.findKth(nums1, nums2, 0, 0, m, n, k) +
                    self.findKth(nums1, nums2, 0, 0, m, n, k+1)) / 2.0
        else:
            return self.findKth(nums1, nums2, 0, 0, m, n, k+1)

    def findKth(self, arr1, arr2, start1, start2, len1, len2, k):
        if len1 > len2:
            return self.findKth(arr2, arr1, start2, start1, len2, len1, k)
        if len1 == 0:
            return arr2[start2 + k - 1]
        if k == 1:
            return min(arr1[start1], arr2[start2])
        p1 = min(k/2, len1)
        p2 = k-p1

        if (arr1[start1+p1-1] > arr2[start2+p2-1]):
            return self.findKth(arr1, arr2, start1, start2+p2, len1, len2-p2, k-p2)
        elif arr1[start1+p1-1] < arr2[start2+p2-1]:
            return self.findKth(arr1, arr2, start1+p1, start2, len1-p1, len2, k-p1)
        else:
            return arr1[start1+p1-1]

s = Solution()
print s.findMedianSortedArrays([1, 3], [2])
print s.findMedianSortedArrays([1, 2], [3, 4])
