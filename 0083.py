"""
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example1:
Input: head = [1,1,2]
Output: [1,2]

Example2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300]
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

"""
Note:
1. Two Pointers(current, nextDistinct): O(n) time | O(1) space
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        currentNode = head
        while currentNode is not None:
            nextDistinctNode = currentNode.next
            while nextDistinctNode is not None and nextDistinctNode.val == currentNode.val:
                nextDistinctNode = nextDistinctNode.next
            currentNode.next = nextDistinctNode
            currentNode = currentNode.next
        return head

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates2(head.next)
        return head.next if head.val == head.next.val else head


# Unit Tests
funcs = [Solution().deleteDuplicates, Solution().deleteDuplicates2]


class TestDeleteDuplicates(unittest.TestCase):
    def testDeleteDuplicates1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 1, 2])
            self.assertEqual(repr(func(head=head)), "1->2->None")

    def testDeleteDuplicates2(self):
        for func in funcs:
            head = ListNode.fromArray([1, 1, 2, 3, 3])
            self.assertEqual(repr(func(head=head)), "1->2->3->None")

    def testDeleteDuplicates3(self):
        for func in funcs:
            head = ListNode.fromArray([])
            self.assertEqual(repr(func(head=head)), "None")

    def testDeleteDuplicates4(self):
        for func in funcs:
            head = ListNode.fromArray([1])
            self.assertEqual(repr(func(head=head)), "1->None")


if __name__ == "__main__":
    unittest.main()
