"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

"""
Note:
1. Three Pointers with carry: O(max(m, n)) time | O(max(m,n)) space
"""




import unittest
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    # TEST ONLY
    def __repr__(self):
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        currentNode = dummy

        while l1 is not None or l2 is not None or carry != 0:
            valueOne = l1.val if l1 is not None else 0
            valueTwo = l2.val if l2 is not None else 0
            sumOfValue = valueOne + valueTwo + carry
            newValue = sumOfValue % 10
            carry = sumOfValue // 10

            newNode = ListNode(newValue)
            currentNode.next = newNode
            currentNode = newNode
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return dummy.next


# Unit Tests
funcs = [Solution().addTwoNumbers]


class TestAddTwoNumbers(unittest.TestCase):
    def testAddTwoNumbers1(self):
        for func in funcs:
            l1 = ListNode.fromArray([2, 4, 7, 1])
            l2 = ListNode.fromArray([9, 4, 5])
            self.assertEqual(repr(func(l1, l2)), "1->9->2->2")

    def testAddTwoNumbers2(self):
        for func in funcs:
            l1 = ListNode(0)
            l2 = ListNode(0)
            self.assertEqual(repr(func(l1, l2)), "0")


if __name__ == "__main__":
    unittest.main()
