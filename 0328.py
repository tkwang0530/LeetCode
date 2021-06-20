"""
328. Odd Even Linked List
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input
Example1:
1->2->3->4->5 => 1->3->5->2->4
Example2:
2->1->3->5->6->4->7 => 2->3->6->7->1->5->4

Constraints:
The number of nodes in the linked list is in the range [0, 10^4]
-10^6 <= Node.val <= 10^6
Follow up: Could you solve it in O(1) space complexity and O(nodes) time complexity?
"""

"""
Note:
O(n) time | O(1) space
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        currentOdd = head
        currentEven = dummy = ListNode(0)
        while currentOdd and currentOdd.next and currentOdd.next.next:
            oddNext = currentOdd.next.next
            currentEven.next = currentOdd.next
            currentOdd.next = oddNext
            currentEven.next.next = None
            currentOdd = oddNext
            currentEven = currentEven.next

        if currentOdd and currentOdd.next:
            currentEven.next = currentOdd.next

        currentOdd.next = dummy.next
        return head


# Unit Tests
import unittest


class TestOddEvenList(unittest.TestCase):
    def testOddEvenList1(self):
        func = Solution().oddEvenList
        head = ListNode.fromArray([1, 2, 3, 4, 5])
        self.assertEqual(repr(func(head=head)), "1->3->5->2->4")

    def testOddEvenList2(self):
        func = Solution().oddEvenList
        head = ListNode.fromArray([2, 1, 3, 5, 6, 4, 7])
        self.assertEqual(repr(func(head=head)), "2->3->6->7->1->5->4")

    def testOddEvenList3(self):
        func = Solution().oddEvenList
        head = None
        self.assertEqual(repr(func(head=head)), "None")

    def testOddEvenList4(self):
        func = Solution().oddEvenList
        head = ListNode.fromArray([2])
        self.assertEqual(repr(func(head=head)), "2")


if __name__ == "__main__":
    unittest.main()