#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        cnt_map = {}
        bulls, cows = 0, 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                cnt = cnt_map.get(secret[i], 0)
                cnt_map[secret[i]] = cnt+1

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                continue
            if cnt_map.has_key(guess[i]) and cnt_map[guess[i]] > 0:
                cows += 1
                cnt_map[guess[i]] -= 1

        return "%dA%dB" % (bulls, cows)

s = Solution()

print s.getHint("1807", "7810")
print s.getHint("1123", "0111")
