#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        ans = digits[:]

        flag = 1
        for i in range(n-1, -1, -1):
            ans[i] += flag
            if ans[i] == 10:
                flag = 1
                ans[i] = 0
            else:
                flag = 0

        if flag == 1:
            ans.insert(0, 1)

        return ans

s = Solution()
print s.plusOne([1, 0, 9, 9])
print s.plusOne([2, 0, 9, 4])
print s.plusOne([0])
