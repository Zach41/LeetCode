#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) <=2:
            return []
        
        ans = []
        nums.sort()

        for i in range(len(nums)-1, 1, -1):
            if i<len(nums)-1 and nums[i] == nums[i+1]:
                continue
            res = self._twoSum(nums, i-1, -nums[i])

            for tmp in res:
                tmp.append(nums[i])
                ans.append(tmp)

        return ans
    
    def _twoSum(self, nums, end, target):
        res = []
        l, r = 0, end

        while l<r:
            if (nums[l] + nums[r] == target):
                tmp = [nums[l], nums[r]]
                res.append(tmp)
                l += 1
                r -= 1
                while l<r and nums[l] == nums[l-1]:
                    l += 1
                while l<r and nums[r] == nums[r+1]:
                    r -= 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1

        return res

s = Solution()
import pdb
pdb.set_trace()
print s.threeSum([-1, 0, 1, 2, -1, -4])
                    
                
