#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bisect import bisect_left


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        pivot = self.find_pivot(nums, target)
        # print("PIVOT: %d" % pivot)
        pos1 = bisect_left(nums[:pivot], target)
        pos2 = bisect_left(nums[pivot:], target)

        if pos1 < pivot and nums[pos1] == target:
            return True
        if pos2 < len(nums) - pivot and nums[pos2 + pivot] == target:
            return True
        return False

    def find_pivot(self, nums, target):
        enum_nums = list(enumerate(nums))
        for i in range(0, len(enum_nums) - 1):
            if enum_nums[i][1] > enum_nums[i + 1][1]:
                return enum_nums[i + 1][0]
        return 0

    def search2(self, nums, target):
        # elagant solution, worst case O(n)
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return True
            if nums[mid] < nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return nums[l] == target


s = Solution()
print(s.search2([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search2([4, 5, 6, 7, 0, 1, 2], 2))
print(s.search2([4, 5, 6, 6, 6, 7, 0, 0, 1, 2], 0))
print(s.search2([4, 5, 6, 6, 6, 7, 0, 0, 1, 2], 6))
print(s.search2([1, 1, 1, 3, 1], 3))
