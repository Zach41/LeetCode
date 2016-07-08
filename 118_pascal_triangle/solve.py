#!/usr/bin/env python
# -*- coding : utf-8 -*-

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            row = ans[i-1]
            tmp = [1]
            for j in range(0, len(row)-1):
                tmp.append(row[j] + row[j+1])
            tmp.append(1)
            ans.append(tmp)

        return ans

s = Solution()
print s.generate(5)
print s.generate(6)
            
