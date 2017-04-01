#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        houses.sort()

        heaters = [float('-inf')] + heaters + [float('inf')]
        ans, i = 0, 0
        for house in houses:
            while house > heaters[i + 1]:
                i += 1
            dis = min(house - heaters[i], heaters[i + 1] - house)
            ans = max(ans, dis)
        return ans


s = Solution()
print(
    s.findRadius([
        282475249, 622650073, 984943658, 144108930, 470211272, 101027544,
        457850878, 458777923
    ], [
        823564440, 115438165, 784484492, 74243042, 114807987, 137522503,
        441282327, 16531729, 823378840, 143542612
    ]))
print(s.findRadius([1, 5], [2]))
print(s.findRadius([1, 2, 3], [2]))
print(s.findRadius([1, 2, 3, 4], [1, 4]))
