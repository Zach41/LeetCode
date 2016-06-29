#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) <= 10:
            return []
        sub_map = {}
        for i in range(len(s)-9):
            cnt = sub_map.get(s[i:10+i], 0)
            sub_map[s[i:10+i]] = cnt + 1
        ans = []
        for (key, cnt) in sub_map.items():
            if cnt >= 2:
                ans.append(key)
        return ans

s = Solution()
import pdb
pdb.set_trace()
print s.findRepeatedDnaSequences("AAAAAAAAAAA")
print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
            
