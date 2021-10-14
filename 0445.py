"""
445. Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

"""
Note:
1. Three Pointers with carry: O(n+m+max(n, m)) time | O(max(n, m)) space
Reverse input lists first
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        carry = 0
        dummy = ListNode(0)
        while carry or l1 or l2:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            currentSum = value1 + value2 + carry
            carry = currentSum // 10
            newNode = ListNode(currentSum % 10)
            newNode.next = dummy.next
            dummy.next = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        
    def reverseList(self, head) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev, head = head, next
        return prev


# Unit Tests
import unittest
funcs = [Solution().addTwoNumbers]

class TestAddTwoNumbers(unittest.TestCase):
    def testAddTwoNumbers1(self):
        for func in funcs:
            l1 = ListNode.fromArray([7, 2, 4, 3])
            l2 = ListNode.fromArray([5, 6, 4])
            self.assertEqual(repr(func(l1, l2)), "7->8->0->7->None")

    def testAddTwoNumbers2(self):
        for func in funcs:
            l1 = ListNode.fromArray([2, 4, 3])
            l2 = ListNode.fromArray([5, 6, 4])
            self.assertEqual(repr(func(l1, l2)), "8->0->7->None")

    def testAddTwoNumbers3(self):
        for func in funcs:
            l1 = ListNode.fromArray([0])
            l2 = ListNode.fromArray([0])
            self.assertEqual(repr(func(l1, l2)), "0->None")


if __name__ == "__main__":
    unittest.main()
