"""
203. Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example2:
Input: head = [], val = 1
Output: []

Example3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
The number of nodes in the list is in the range [0, 10^4].
1 <= Node.val <= 50
0 <= val <= 50
"""

"""
Note:
1. One pass: O(n) time | O(1) space
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    # TEST ONLY
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = dummy = ListNode(0)
        dummy.next = head
        while current:
            while current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next
        return dummy.next

# Unit Tests
import unittest
funcs = [Solution().removeElements]

class TestRemoveElements(unittest.TestCase):
    def testRemoveElements1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 6, 3, 4, 5, 6])
            val = 6
            self.assertEqual(repr(func(head=head, val=val)), "1->2->3->4->5->None")

    def testRemoveElements2(self):
        for func in funcs:
            head = None
            val = 1
            self.assertEqual(repr(func(head=head, val=val)), "None")

    def testRemoveElements3(self):
        for func in funcs:
            head = ListNode.fromArray([7, 7, 7, 7])
            val = 7
            self.assertEqual(repr(func(head=head, val=val)), "None")


if __name__ == "__main__":
    unittest.main()