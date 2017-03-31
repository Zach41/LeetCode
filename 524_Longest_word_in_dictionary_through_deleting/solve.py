#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        rec = []
        str_n = len(s)
        for word in d:
            ptr1, ptr2 = 0, 0
            word_n = len(word)
            while ptr2 < word_n:
                while ptr1 < str_n and word[ptr2] != s[ptr1]:
                    ptr1 += 1
                if ptr1 == str_n:
                    break
                ptr1 += 1
                ptr2 += 1
            if ptr2 == word_n:
                rec.append(word)
        if not rec:
            return ""
        rec.sort(key=lambda x: (-len(x), x))
        return rec[0]

    def elegant_version(self, s, d):
        rec = []
        for word in d:
            i = 0
            word_n = len(word)
            for c in s:
                if i < word_n and word[i] == c:
                    i += 1
                if i == word_n:
                    rec.append(word)
                    break
        if not rec:
            return ""
        else:
            rec.sort(key=lambda x: (-len(x), x))
            return rec[0]


s = Solution()
print(s.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
print(s.elegant_version("abpcplea", ["ale", "apple", "monkey", "plea"]))
