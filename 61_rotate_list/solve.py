#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        total = 0
        cur = head
        while cur.next:
            cur = cur.next
            total += 1
        total += 1
        cur.next = head
        for _ in range(total - k % total - 1):
            head = head.next
        cur = head.next
        head.next = None
        return cur


s = Solution()

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5


def print_list(a):
    ret = ""
    while a:
        ret += str(a.val) + " "
        a = a.next
    return ret


print(print_list(s.rotateRight(a1, 2)))
