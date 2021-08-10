"""
206. Reverse Linked List
Reverse a singly linked list.

Examples:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

"""
Note:
1. Iteration: O(n) time | O(1) space
2. Recursion: O(n) time | O(n) space
"""




import unittest
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
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev, head = head, next
        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        return self.helper(head, None)

    def helper(self, current: ListNode, prev: ListNode) -> ListNode:
        if current is None:
            return prev
        next = current.next
        current.next = prev
        return self.helper(next, current)


# Unit Tests
funcs = [Solution().reverseList, Solution().reverseList2]


class TestReverseList(unittest.TestCase):
    def testReverseList1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 3, 4, 5])
            self.assertEqual(repr(func(head=head)), "5->4->3->2->1->None")


if __name__ == "__main__":
    unittest.main()
