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
"""

"""
Note:
1. Iteration (Three Pointers): O(n) time | O(1) space
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
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            firstNode = head
            secondNode = head.next
            prev.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            prev, head = firstNode, firstNode.next
        return dummy.next

    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        firstNode = head
        secondNode = head.next
        firstNode.next = self.swapPairs(secondNode.next)
        secondNode.next = firstNode
        return secondNode


# Unit Tests
funcs = [Solution().swapPairs, Solution().swapPairs2]


class TestSwapPairs(unittest.TestCase):
    def testSwapPairs1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 3, 4])
            self.assertEqual(repr(func(head=head)), "2->1->4->3->None")

    def testSwapPairs2(self):
        for func in funcs:
            head = None
            self.assertEqual(repr(func(head=head)), "None")

    def testSwapPairs3(self):
        for func in funcs:
            head = ListNode(1)
            self.assertEqual(repr(func(head=head)), "1->None")


if __name__ == "__main__":
    unittest.main()
