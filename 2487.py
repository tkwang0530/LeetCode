"""
2487. Remove Nodes From Linked List
description: https://leetcode.com/problems/remove-nodes-from-linked-list/description/
"""

"""
Note:
1. Monotonic stack: O(n) time | O(n) space - where n is the length of linked list
"""

import unittest
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    # TEST ONLY
    def __repr__(self):
        if self is None:
            return "None"
        nums = [self.val]
        while self.next:
            nums.append(self.next.val)
            self = self.next
        return "->".join(str(num) for num in nums)

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

from typing import Optional
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("inf"))
        stack = []
        current = head
        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()
            stack.append(current)
            current = current.next
        
        current = dummy
        for node in stack:
            current.next = node
            current = current.next
        
        return dummy.next


# Unit Tests
funcs = [Solution().removeNodes]


class TestRemoveNodes(unittest.TestCase):
    def testRemoveNodes1(self):
        for func in funcs:
            head = ListNode.fromArray([5, 2, 13, 3, 8])
            self.assertEqual(repr(func(head=head)), "13->8")

    def testRemoveNodes2(self):
        for func in funcs:
            head = ListNode.fromArray([1, 1, 1, 1])
            self.assertEqual(repr(func(head=head)), "1->1->1->1")


if __name__ == "__main__":
    unittest.main()
