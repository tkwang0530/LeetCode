"""
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.

Examples:
    Given 1->2->3->4->5, k = 2, the answer is 4->5->1->2->3.
    Given 0->1->2, k = 4, the answer is 2->0->1.

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
"""

"""
Note:
O(n) time | O(1) space
1. find the old tail and new tail
2. connect the new tail to the head of the linked list
3. assign None to the new tail.next
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


# O(n) time | O(1) space
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        oldTail = head
        newTail = head
        if oldTail is None:
            return None

        length = 1
        while oldTail.next is not None:
            oldTail = oldTail.next
            length += 1

        k = k % length
        count = 1
        while count < length - k:
            newTail = newTail.next
            count += 1

        oldTail.next = head
        newHead = newTail.next
        newTail.next = None
        return newHead


# Unit Tests
import unittest


class TestRotateRight(unittest.TestCase):
    def testRotate1(self):
        func = Solution().rotateRight
        head = ListNode.fromArray([1, 2, 3, 4, 5])
        self.assertEqual(repr(func(head=head, k=2)), "4->5->1->2->3")

    def testRotate2(self):
        func = Solution().rotateRight
        head = ListNode.fromArray([0, 1, 2])
        self.assertEqual(repr(func(head=head, k=4)), "2->0->1")


if __name__ == "__main__":
    unittest.main()