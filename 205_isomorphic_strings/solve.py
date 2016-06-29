#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isIsomorphic(self, s, t):
        char_map = {}
        rec = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if char_map.has_key(s[i]):
                if t[i] != char_map[s[i]]:
                    return False
            elif t[i] in rec:
                return False
            else:
                rec.append(t[i])
                char_map[s[i]] = t[i]
            
        return True


s = Solution()
print s.isIsomorphic("egg", "add")
print s.isIsomorphic("foo", "bar")
print s.isIsomorphic("paper", "title")
print s.isIsomorphic("ab", "aa")
