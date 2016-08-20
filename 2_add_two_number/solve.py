#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + str(self.next)
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def getNum(lst):
            ret = 0
            base = 1
            while lst:
                ret += base * lst.val
                base *= 10
                lst  = lst.next
            return ret
                
        def genList(num):
            cur, prev = ListNode(int(str(num)[0])), None

            for x in str(num)[1:]:
                prev = cur
                cur = ListNode(int(x))
                cur.next = prev
            return cur

        num1 = getNum(l1)
        num2 = getNum(l2)
        return genList(num1+num2)


s = Solution()
test1 = ListNode(2)
n2    = ListNode(4)
n3    = ListNode(3)
test1.next = n2
n2.next    = n3

test2 = ListNode(5)
n4    = ListNode(6)
n5    = ListNode(4)
test2.next = n4
n4.next    = n5

import pdb
pdb.set_trace()
ans = s.addTwoNumbers(test1, test2)
print ans

    
                
    
    
