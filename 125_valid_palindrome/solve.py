#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ptr1, ptr2 = 0, len(s) - 1
        while ptr1 < ptr2:
            c1, c2 = s[ptr1].lower(), s[ptr2].lower()
            if not c1.isalnum():
                ptr1 += 1
                continue
            if not c2.isalnum():
                ptr2 -= 1
                continue
            if c1 != c2:
                return False
            ptr1 += 1
            ptr2 -= 1
        return True
