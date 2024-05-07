"""
2816. Double a Number Represented as a Linked List
description: https://leetcode.com/pDoubleItlems/double-a-number-represented-as-a-linked-list/description/
"""

"""
Note:
1. Reverse + Double: O(n) time | O(n) space - where n is the length of linked list
"""

import unittest

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}->{self.next}"

    @classmethod
    def fromArray(cls, arr):
        if arr is None:
            return None
        idx = 0
        length = len(arr)
        dummy = cls(0)
        current = dummy
        while idx < length:
            current.next = cls(arr[idx])
            current = current.next
            idx += 1
        return dummy.next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head: ListNode) -> ListNode:
            prev = None
            current = head
            while current:
                next = current.next
                current.next = prev
                prev, current = current, next
            return prev

        head = reverseList(head)
        carry = 0
        current = head
        prev = dummy = ListNode(-1)
        while current or carry:
            currentVal = current.val if current else 0
            val = (currentVal * 2 + carry) % 10
            carry = (currentVal * 2 + carry) // 10
            prev.next = ListNode(val)
            prev = prev.next
            current = current.next if current else None
        
        newHead = dummy.next
        dummy.next = None
        return reverseList(newHead)


# Unit Tests
funcs = [Solution().doubleIt]


class TestDoubleIt(unittest.TestCase):
    def testDoubleIt1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 8, 9])
            self.assertEqual(repr(func(head)), "3->7->8->None")

    def testDoubleIt2(self):
        for func in funcs:
            head = ListNode.fromArray([9, 9, 9])
            self.assertEqual(repr(func(head)), "1->9->9->8->None")


if __name__ == "__main__":
    unittest.main()
