#!/usr/bin/env python
# -*- coding : utf-8 -*-

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        positive = [0]*n
        negtive = [0]*n

        if nums[0] > 0:
            positive[0]= nums[0]
        else:
            negtive[0] = nums[0]

        max_p = nums[0]
        for i in range(1, n):
            if nums[i] > 0:
                positive[i] = max(positive[i-1]*nums[i], nums[i])
                negtive[i]  = negtive[i-1] * nums[i]
            elif nums[i] < 0:
                positive[i] = negtive[i-1]*nums[i]
                negtive[i]  = min(positive[i-1] * nums[i], nums[i])
            if positive[i] > max_p:
                max_p = positive[i]

        return max_p

s = Solution()
print s.maxProduct([2, 3, -2, 4])
                
