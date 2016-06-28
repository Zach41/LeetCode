#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_map = {}
        t_map = {}

        for c in s:
            cnt = s_map.get(c, 0)
            s_map[c] = cnt+1

        for c in t:
            cnt = t_map.get(c, 0)
            t_map[c] = cnt+1

        return self._check(s_map, t_map) and self._check(t_map, s_map)

    def _check(self, map1, map2):
        for key in map1.keys():
            if not map2.has_key(key):
                return False
            if map2[key] != map1[key]:
                return False
        return True

s = Solution()

print s.isAnagram("a", "ab")
print s.isAnagram("anagram", "naagram")
print s.isAnagram("rat", "car")
