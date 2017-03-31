#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_ptr, fast_ptr = head, head
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        if fast_ptr:
            slow_ptr = slow_ptr.next
        rev = self.reverse(slow_ptr)

        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True

    def reverse(self, head):
        if not head:
            return None
        cur = head
        next = cur.next
        while next:
            tmp = next.next
            next.next = cur
            cur = next
            next = tmp
        head.next = None
        return cur


s = Solution()
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(2)
a5 = ListNode(1)

# a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5

print(s.isPalindrome(a1))
