#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        
        maxJump = 0
        maxReach = 0
        step = 0

        for i in range(n):
            if i > maxReach:
                step += 1
                maxReach = maxJump
            maxJump = max(maxJump, nums[i]+i)

        return step
                

s = Solution()

print s.jump([2, 3, 1, 1, 4])
print s.jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3])
            
        
