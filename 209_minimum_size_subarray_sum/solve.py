#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    # this is a time limit error
    def minSubArrayLen2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s or not nums:
            return 0
        n = len(nums)
        dp = [-1]*n

        tot_sum = [0]*n
        tot_sum[0] = nums[0]
        for i in range(1, n):
            tot_sum[i] = tot_sum[i-1] + nums[i]

        min_size = n
        for i in range(n):
            if tot_sum[i] < s:
                continue
            else:
                for j in range(i, dp[i], -1):
                    if tot_sum[i] - tot_sum[j] + nums[j] >= s:
                        dp[i] = j
                        if i-j+1 < min_size:
                            min_size = i-j+1
                        break
        return min_size

    def minSubArrayLen(self, s, nums):
        if sum(nums) < s:
            return 0
        left, right = 0, 0
        n = len(nums)
        min_size = n

        tot_sum = [0]*n
        tot_sum[0] = nums[0]
        for i in range(1, n):
            tot_sum[i] = tot_sum[i-1]+nums[i]

        while True:
            if right >= n or left >=n:
                break
            if tot_sum[right] - tot_sum[left] + nums[left] < s:
                right += 1
            else:
                min_size = min(min_size, right-left+1)
                left += 1
        return min_size

    def minSubArrayLen3(self, s, nums):
        # O(nlogn) version
        if sum(nums) < s:
            return 0
        n = len(nums)
        tot_sum = [0]*(n+1)
        for i in range(1, n+1):
            tot_sum[i] = tot_sum[i-1]+nums[i-1]
        min_size = n
        for i in range(0, n):
            tmp = self.search(i, n, tot_sum, s)
            if tmp != 0:
                min_size = min(min_size, tmp)
        return min_size

    def search(self, left, right, arr, value):
        l, r= left, right
        if arr[right] - arr[left]< value:
            return 0
        min_size = right - left
        mid = (l+r)/2
        while l < r:
            if arr[mid] - arr[left] >= value:
                min_size = mid-left
                r = mid
            else:
                l = mid+1
            mid = (l+r) / 2
        return min_size
                



s = Solution()
import pdb
pdb.set_trace()
print s.minSubArrayLen3(7, [2, 3, 1, 2, 4, 3])
print s.minSubArrayLen3(4, [1, 4, 4])
print s.minSubArrayLen3(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8])
        
