#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        rec = {}

        for e in nums:
            if rec.has_key(e):
                rec[e] += 1
            else:
                rec[e] = 1

        sorted_x = sorted(rec.items(), key=operator.itemgetter(1))
        sorted_x.reverse()
        return map(lambda x: x[0], sorted_x[:k])

    # O(n) solution
    def topKFrequent2(self, nums, k):
        rec_frequency = {}
        rec_num = {}

        for e in nums:
            if rec_frequency.has_key(e):
                rec_frequency[e] += 1
            else:
                rec_frequency[e] = 1
        for e in nums:
            frequency = rec_frequency[e]
            if rec_num.has_key(frequency):
                if e not in rec_num[frequency]:
                    rec_num[frequency].append(e)
            else:
                rec_num[frequency] = [e]
                    
                
        ans = []
        cnt = k, 
        for i in range(len(nums), 0, -1):
            if rec_num.has_key(i):
                ans.extend(rec_num[i])
                k -= len(rec_num[i])
            if k == 0:
                break
        return ans

s = Solution()

import pdb
pdb.set_trace()

print s.topKFrequent2([1, 1, 1, 2, 2, 2, 3, 3, 3], 3)
