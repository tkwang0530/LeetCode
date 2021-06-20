"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

Examples:
    Given 1->2->3->4, the answer is 2->1->4->3.
    Given null, the answer is null.
    Given 1->null, the answer is 1->null.

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

Follow up:
Can you solve the problem without modifying the values in the list's nodes?
(i.e., only nodes themselves may be changed.)
"""

"""
Note:
To be continued
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


# O(n) time | O(1) space
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head
        current = head
        if not current or not current.next:
            return current
        while current is not None and current.next is not None:
            prev.next = current.next
            current.next = current.next.next
            prev.next.next = current
            current = current.next
            prev = prev.next.next
        return dummy.next


# Unit Tests
import unittest


class TestSwapPairs(unittest.TestCase):
    def testSwapPairs1(self):
        func = Solution().swapPairs
        head, head.next, head.next.next, head.next.next.next = (
            ListNode(1),
            ListNode(2),
            ListNode(3),
            ListNode(4),
        )
        self.assertEqual(repr(func(head=head)), "2->1->4->3")

    def testSwapPairs2(self):
        func = Solution().swapPairs
        head = None
        self.assertEqual(repr(func(head=head)), "None")

    def testSwapPairs3(self):
        func = Solution().swapPairs
        head = ListNode(1)
        self.assertEqual(repr(func(head=head)), "1")


if __name__ == "__main__":
    unittest.main()