#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        if not nums:
            return ans
        start = 0
        for i in range(len(nums)):
            if nums[i] == i-start+nums[start]:
                continue
            else:
                if start == i-1:
                    ans.append(str(nums[start]))
                else:
                    ans.append("%d->%d" % (nums[start], nums[i-1]))
                start = i
        if start == len(nums)-1:
            ans.append(str(nums[-1]))
        else:
            ans.append("%d->%d" % (nums[start], nums[-1]))
        return ans

s = Solution()

print s.summaryRanges([0, 1, 2, 4, 5, 7])
print s.summaryRanges([0, 1, 2, 4, 5, 7, 8, 9])
        
