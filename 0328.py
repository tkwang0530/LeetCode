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
1. Two Pointers: O(n) time | O(1) space
2. Two Pointers2: O(n) time | O(1) space
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

    def oddEvenList2(self, head: ListNode) -> ListNode:
        odd = dummyOdd = ListNode(0)
        even = dummyEven  = ListNode(0)
        
        toggle = False
        while head:
            if toggle:
                even.next = head
                even, head = head, head.next
                even.next = None
            else:
                odd.next = head
                odd, head = head, head.next
                odd.next = None
            toggle = not toggle
        
        odd.next = dummyEven.next
        return dummyOdd.next

# Unit Tests
import unittest
funcs = [Solution().oddEvenList, Solution().oddEvenList2]

class TestOddEvenList(unittest.TestCase):
    def testOddEvenList1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 3, 4, 5])
            self.assertEqual(repr(func(head=head)), "1->3->5->2->4->None")

    def testOddEvenList2(self):
        for func in funcs:
            head = ListNode.fromArray([2, 1, 3, 5, 6, 4, 7])
            self.assertEqual(repr(func(head=head)), "2->3->6->7->1->5->4->None")

    def testOddEvenList3(self):
        for func in funcs:
            head = None
            self.assertEqual(repr(func(head=head)), "None")

    def testOddEvenList4(self):
        for func in funcs:
            head = ListNode.fromArray([2])
            self.assertEqual(repr(func(head=head)), "2->None")


if __name__ == "__main__":
    unittest.main()