"""
143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:
L0 -> L1 -> ... -> Ln-1 -> Ln

Reorder the list to be on the following form:
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 10^4]
1 <= Node.val <= 1000
"""

"""
Note:
1. Two Pointers + toggle: O(n) time | O(1) space
(1) split to two list using fast slow pointers technique
(2) reverse the right sub list
(3) connect to two lists together
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
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        l2 = slow.next
        slow.next = None
        l1 = head
        
        l2 = self.reverse(l2)
        
        current = dummy = ListNode(0)
        toggle = True
        while l1 and l2:
            if toggle:
                current.next = l1
                current, l1 = l1, l1.next
            else:
                current.next = l2
                current, l2 = l2, l2.next
            toggle = not toggle
        
        current.next = l1 or l2
        head = dummy.next
        return 
    
    def reverse(self, head) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev, head = head, next
        return prev

# Unit Tests

funcs = [Solution().reorderList]


class TestReorderList(unittest.TestCase):
    def testReorderList1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 3, 4])
            func(head=head)
            self.assertEqual(repr(head), "1->4->2->3->None")

    def testReorderList2(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 3, 4, 5])
            func(head=head)
            self.assertEqual(repr(head), "1->5->2->4->3->None")


if __name__ == "__main__":
    unittest.main()
