"""
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(nlogn) time and O(1) memory (i.e. constant space)?
Example1:
Input: head = [4, 2 ,1, 3]
Output: [1, 2, 3, 4]

Example2:
Input: head = [-1, 5, 3, 4, 0]
Output: [-1, 0, 3, 4, 5]

Example3:
Input: head = []
Output: []
"""

"""
Note:
1. Merge sort using recursion: O(nlogn) time | O(logn) space
2. 
"""




from typing import List
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


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(mid)
        return self.merge(left, right)

    def merge(self, left, right):
        if not left or not right:
            return left or right
        dummy = p = ListNode(0)
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left or right
        return dummy.next


# Unit Tests

funcs = [Solution().sortList]


class TestSortList(unittest.TestCase):
    def testSortList1(self):
        head = ListNode.fromArray([4, 2, 1, 3])
        for func in funcs:
            self.assertEqual(repr(func(head=head)), '1->2->3->4')

    def testSortList2(self):
        head = ListNode.fromArray([-1, 5, 3, 4, 0])
        for func in funcs:
            self.assertEqual(repr(func(head=head)), '-1->0->3->4->5')

    def testSortList3(self):
        head = ListNode.fromArray([])
        for func in funcs:
            self.assertEqual(repr(func(head=head)), 'None')


if __name__ == "__main__":
    unittest.main()
