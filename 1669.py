"""
1669. Merge In Between Linked Lists
description: https://leetcode.com/problems/merge-in-between-linked-lists/description/
"""

"""
Note:
1. Intuition: O(n + m) time | O(1) space - where n is the length of list1 and m is the length of list2
"""

class ListNode:
    def __init__(self, val=0, next=None):
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
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = dummy = ListNode(0, list1)
        count = 0
        current = list1
        beforeA, afterB = None, None
        while current:
            if count == a:
                beforeA = prev
            if count == b:
                afterB = current.next
                current.next = None
                break

            prev = current
            count += 1
            current = current.next
        
        prev = ListNode(0, list2)
        current = list2
        while current:
            prev = current
            current = current.next
        
        beforeA.next, prev.next = list2, afterB
        return dummy.next

# Unit Tests
import unittest
funcs = [Solution().mergeInBetween]

class TestMergeInBetween(unittest.TestCase):
    def testMergeInBetween1(self):
        for func in funcs:
            list1 = ListNode.fromArray([10, 1, 13, 6, 9, 5])
            a = 3
            b = 4
            list2 = ListNode.fromArray([1000000, 1000001, 1000002])
            self.assertEqual(repr(func(list1, a, b, list2)), "10->1->13->1000000->1000001->1000002->5->None")

    def testMergeInBetween2(self):
        for func in funcs:
            list1 = ListNode.fromArray([0,1,2,3,4,5,6])
            a = 2
            b = 5
            list2 = ListNode.fromArray([1000000,1000001,1000002,1000003,1000004])
            self.assertEqual(repr(func(list1, a, b, list2)), "0->1->1000000->1000001->1000002->1000003->1000004->6->None")  

if __name__ == "__main__":
    unittest.main()