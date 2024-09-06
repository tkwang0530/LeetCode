"""
3217. Delete Nodes From Linked List Present in Array
description: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/
"""

"""
Note:
1. HashSet: O(n) time | O(n) space - where n is the length of linked list
"""

import unittest
from typing import Optional, List
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
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        numSet = set(nums)
        prev = dummy
        current = head
        while current:
            if current.val in numSet:
                current = current.next
            else:
                prev.next = current
                prev, current = current, current.next
                prev.next = None

        return dummy.next

# Unit Tests
funcs = [Solution().modifiedList]


class TestModifiedList(unittest.TestCase):
    def testModifiedList1(self):
        for func in funcs:
            nums = [1, 2, 3]
            head = ListNode.fromArray([1, 2, 3, 4, 5])
            self.assertEqual(repr(func(nums=nums, head=head)), "4->5->None")

    def testModifiedList2(self):
        for func in funcs:
            nums = [1]
            head = ListNode.fromArray([1,2,1,2,1,2])
            self.assertEqual(repr(func(nums=nums, head=head)), "2->2->2->None")

    def testModifiedList3(self):
        for func in funcs:
            nums = [5]
            head = ListNode.fromArray([1, 2, 3,4 ])
            self.assertEqual(repr(func(nums=nums, head=head)), "1->2->3->4->None")

if __name__ == "__main__":
    unittest.main()
