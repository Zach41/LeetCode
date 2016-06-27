#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_map = {}
        
        for i in range(len(words)):
            word_map[words[i]] = i

        ans = []
        for word in words:
            word_rev = word[::-1]
            if word_map.has_key(word_rev) and word_map[word] != word_map[word_rev]:
                ans.append([word_map[word], word_map[word_rev]])

            for i in range(len(word)):
                w1 = word[:i][::-1]

                if word_map.has_key(w1) and self._isPal(word[i:]):
                    ans.append([word_map[word], word_map[w1]])

                w2 = word_rev[:i]
                if word_map.has_key(w2) and self._isPal(word_rev[i:]):
                    ans.append([word_map[w2], word_map[word]])

        return ans

    def _isPal(self, word):
        l, r =  0, len(word)-1
        while l<r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True


s = Solution()
import pdb
pdb.set_trace()
print s.palindromePairs(["bat", "tab", "cat"])
print s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
