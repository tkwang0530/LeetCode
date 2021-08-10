"""
82. Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
The number of nodes in the list is in the range [0, 300]
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

"""
Note:
1. Two Pointers(prev, head): O(n) time | O(1) space 
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                # Loop until head point to the last duplicates
                while head and head.next and head.val == head.next.val:
                    head = head.next

                # prev.next and head will be the new no duplicate node
                head = head.next
                prev.next = head 
            else:
                prev = prev.next
                head = head.next
        return dummy.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        if head.val != head.next.val:
            head.next = self.deleteDuplicates2(head.next)
            return head
        else:
            while head and head.next and head.val == head.next.val:
                head = head.next

            # head.next will be the new no duplicate node
            return self.deleteDuplicates2(head.next)

# Unit Tests
funcs = [Solution().deleteDuplicates, Solution().deleteDuplicates2]


class TestDeleteDuplicates(unittest.TestCase):
    def testDeleteDuplicates1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 3, 3, 4, 4, 5])
            self.assertEqual(repr(func(head=head)), "1->2->5->None")

    def testDeleteDuplicates2(self):
        for func in funcs:
            head = ListNode.fromArray([1, 1, 1, 2, 3])
            self.assertEqual(repr(func(head=head)), "2->3->None")


if __name__ == "__main__":
    unittest.main()
