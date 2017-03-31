#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tot = self.count(head)
        if tot == n:
            head = head.next
            return head
        cur = head
        for _ in range(tot - n % tot - 1):
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
        else:
            head = None
        return head

    def count(self, head):
        cnt = 0
        while head.next:
            cnt += 1
            head = head.next
        return cnt

    def removeNthFromEnd2(self, head, n):
        # much elegant solution
        ptr1, ptr2 = head, head
        while n:
            ptr2 = ptr2.next
            n -= 1
        if not ptr2:
            return head.next

        ptr2 = ptr2.next
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = ptr1.next.next
        return head


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


print(print_list(s.removeNthFromEnd2(a1, 2)))
