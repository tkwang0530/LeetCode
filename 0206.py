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


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        return self.helper(head, None)

    def helper(self, curr: ListNode, prev: ListNode) -> ListNode:
        if curr is None:
            return prev
        n = curr.next
        curr.next = prev
        return self.helper(n, curr)


# Unit Tests
import unittest


class TestReverseList(unittest.TestCase):
    def testReverseList1(self):
        func = Solution().reverseList
        func2 = Solution().reverseList2
        head = ListNode.fromArray([1, 2, 3, 4, 5])
        head2 = ListNode.fromArray([1, 2, 3, 4, 5])
        self.assertEqual(repr(func(head=head)), "5->4->3->2->1")
        self.assertEqual(repr(func2(head=head2)), "5->4->3->2->1")


if __name__ == "__main__":
    unittest.main()