"""
21. Merge Two Sorted Lists
Merge Two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example2:
Input: l1 = [], l2 = []
Output: []

Example3:
Input: l1 = [], l2 = [0]
Output: [0]
"""

"""
Note:
1. Three Pointers: O(n) time | O(1) space
2. Recursion: O(n) time | O(n) space
if l1.val < l2.val: l1.next = self.mergeTwoList(l1.next, l2)
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next
        if l1 or l2:
            prev.next = l1 or l2
        return dummy.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next= self.mergeTwoLists(l1, l2.next)
            return l2

# Unit Tests


funcs = [Solution().mergeTwoLists, Solution().mergeTwoLists2]


class TestMergeTwoLists(unittest.TestCase):
    def testMergeTwoLists1(self):
        for func in funcs:
            l1 = ListNode.fromArray([1, 2, 4])
            l2 = ListNode.fromArray([1, 3, 4])
            self.assertEqual(repr(func(l1=l1, l2=l2)), "1->1->2->3->4->4->None")

    def testMergeTwoLists2(self):
        for func in funcs:
            l1 = ListNode.fromArray([])
            l2 = ListNode.fromArray([])
            self.assertEqual(repr(func(l1=l1, l2=l2)), "None")

    def testMergeTwoLists3(self):
        for func in funcs:
            l1 = ListNode.fromArray([])
            l2 = ListNode.fromArray([0])
            self.assertEqual(repr(func(l1=l1, l2=l2)), "0->None")


if __name__ == "__main__":
    unittest.main()
