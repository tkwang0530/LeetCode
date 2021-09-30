"""
725. Split Linked List in Parts
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

Example1:
1->2->3
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example2:
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

Constraints:
The number of nodes in the list is in the range [0, 1000]
0 <= Node.val <= 1000
1 <= k <= 50
"""

"""
Note:
1. Quotient and Remainder: O(n) time | O(n/k) space
"""

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

from typing import Optional, List
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [None] * k
        if not head:
            return result
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        quotient = length // k
        remainder = length % k
        listSizes = ([quotient+1] * remainder) + ([quotient] * (k - remainder))
        current = head
        for i, listSize in enumerate(listSizes):
            result[i] = current
            if not current:
                continue
            prev = None
            while current and listSize:
                prev = current
                current = current.next
                listSize -= 1
            prev.next = None
        return result


# Unit Tests
import unittest
funcs = [Solution().splitListToParts]

class TestSpliltListToParts(unittest.TestCase):
    def testSpliltListToParts1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 3])
            k = 5
            self.assertEqual([repr(head) for head in func(head=head, k=k)], ["1->None", "2->None", "3->None", "None", "None"])

    def testSpliltListToParts2(self):
        for func in funcs:
            head = ListNode.fromArray([1,2,3,4,5,6,7,8,9,10])
            k = 3
            self.assertEqual([repr(head) for head in func(head=head, k=k)], ["1->2->3->4->None", "5->6->7->None", "8->9->10->None"])

if __name__ == "__main__":
    unittest.main()
