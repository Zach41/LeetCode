#!/usr/bin/env python
# -*- coding : utf-8 -*-

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        ans = []
        for i in range(rowIndex + 1):
            ans.append(1)
            for j in range(i-1, 0, -1):
                ans[j] = ans[j] + ans[j-1]
        return ans

s = Solution()
print s.getRow(3)
print s.getRow(4)
