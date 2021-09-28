"""
25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example1:
1->2->3->4->5 => 2->1->4->3->5
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example2:
1->2->3->4->5 => 3->2->1->4->5
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example4:
Input: head = [1], k = 1
Output: [1]

Constraints:
The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

"""
Note:
1. reverse part of the list wth tail if tail is not none: O(n) time | O(1) space
"""

from typing import Optional, Tuple
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = dummy = ListNode(0)
        dummy.next = head
        while current:
            runningK = k
            head = current.next
            tail = current
            nextHead = tail.next
            while runningK > 0:
                tail = tail.next if tail else None
                nextHead = tail.next if tail else None
                runningK -= 1
            if not tail:
                return dummy.next
            else:
                newHead, newTail = self.reverseList(head, tail)
                current.next = newHead
                newTail.next = nextHead
                current = newTail
        return dummy.next

    def reverseList(self, head: ListNode, tail: ListNode) -> Tuple[ListNode, ListNode]:
        if not head:
            return (None, None)
        if not head.next:
            return (head, head)
        prev = None
        newTail = head
        while head and prev != tail:
            next = head.next
            head.next = prev
            prev, head = head, next
        return (prev, newTail)


# Unit Tests
import unittest
funcs = [Solution().reverseKGroup]

class TestReverseKGroup(unittest.TestCase):
    def testReverseKGroup1(self):
        for func in funcs:
            head = ListNode.fromArray([1,2,3,4,5])
            k = 2
            self.assertEqual(repr(func(head=head, k=k)), "2->1->4->3->5->None")

    def testReverseKGroup2(self):
        for func in funcs:
            head = ListNode.fromArray([1,2,3,4,5])
            k = 3
            self.assertEqual(repr(func(head=head, k=k)), "3->2->1->4->5->None")

    def testReverseKGroup3(self):
        for func in funcs:
            head = ListNode.fromArray([1,2,3,4,5])
            k = 1
            self.assertEqual(repr(func(head=head, k=k)), "1->2->3->4->5->None")

    def testReverseKGroup4(self):
        for func in funcs:
            head = ListNode.fromArray([1])
            k = 1
            self.assertEqual(repr(func(head=head, k=k)), "1->None")


if __name__ == "__main__":
    unittest.main()
