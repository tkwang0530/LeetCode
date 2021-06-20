"""
147. Insertion Sort List
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
The step of the insertion sort algorithm:
1. Insertion sort iterates, consuming one iput element each repetition and growing a sorted ouput list.
2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
3. It repeats until no iput elements remain.

Examples:
    Given -1->5->3->4->0, the answer is -1->0->3->4->5.
    Given 4->2->1->3, the answer is 1->2->3->4.

Constraints:
The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
"""

"""
Note:
O(n) time | O(1) space
1. two pointer: head and current (start from dummy)
2. if current and current.val is larger then the head.val, reset the current to dummy, otherwise, keep move current forward until its next val is larger or equal to head.val
3. insert the head between current and current.next 
"""
from typing import Tuple


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


# O(n^2) time | O(1) space
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        current = dummy = ListNode(0)
        while head:
            # if current is not None and current.val is larger than the head.val, we have to reset current to the start (dummy)
            if current and current.val > head.val:
                current = dummy

            # otherwise, keep moving current, until we find current.next.val is larger or equal to the head.val
            while current.next and current.next.val < head.val:
                current = current.next

            # insert the head into the potition we found
            current.next, current.next.next, head = (
                head,
                current.next,
                head.next,
            )
        return dummy.next


# Unit Tests
import unittest


class TestInsertionSortList(unittest.TestCase):
    def testInsertionSortList1(self):
        func = Solution().insertionSortList
        head = ListNode.fromArray([-1, 5, 3, 4, 0])
        self.assertEqual(repr(func(head=head)), "-1->0->3->4->5")

    def testInsertionSortList2(self):
        func = Solution().insertionSortList
        head = ListNode.fromArray([4, 2, 1, 3])
        self.assertEqual(repr(func(head=head)), "1->2->3->4")


if __name__ == "__main__":
    unittest.main()