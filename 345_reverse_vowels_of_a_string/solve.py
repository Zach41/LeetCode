#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ptr1, ptr2 = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        while ptr1 < ptr2:
            if s[ptr1] in vowels and s[ptr2] in vowels:
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                ptr1 += 1
                ptr2 -= 1
            if s[ptr1] not in vowels:
                ptr1 += 1
            if s[ptr2] not in vowels:
                ptr2 -= 1
        return ''.join(s)


s = Solution()
str1 = "hello"
str2 = "leetcode"

print(s.reverseVowels(str1))
print(s.reverseVowels(str2))
print(s.reverseVowels("aA"))
