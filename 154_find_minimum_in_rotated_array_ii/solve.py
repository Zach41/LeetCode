#!/usr/bin/env python
# -*- utf-8 -*-

class Solution(object):
    # O(n) version
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_e = nums[0]

        for num in nums:
            if min_e > num:
                min_e = num

        return min_e

    def findMin2(self, nums):
        # worst case is O(n)
        n = len(nums)
        start, end = 0, n-1
        while start+1<end:
            mid = (start + end) / 2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                end -= 1

        return min(nums[start], nums[end])
s = Solution()
print s.findMin([4, 5, 6, 7, 0, 1, 2, 3])
print s.findMin([1, 2, 2, 2, 2, 2])
