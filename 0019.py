"""
19. Remove Nth Node from End of List
Given a linked list, remove the n-th node from the end of list and return its head
For example, the following two linked lists begin to intersect at node c1:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5

Follow up:
Could you do this in one pass?
"""

"""
Note:
1. Brute force: O(n) time | O(1) space
first find the length of linked list, then remove the (L-n+1)th node. 

2. Slow-fast pointer: O(n) time | O(1) space
when fast pointer points to the last node, slow pointer points to the previous node of the last nth node.
"""




import unittest
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next

        length -= n
        current = dummy
        while length > 0:
            length -= 1
            current = current.next

        current.next = current.next.next
        return dummy.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while n > 0:
            fast = fast.next
            n -= 1

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


# Unit Tests
funcs = [Solution().removeNthFromEnd, Solution().removeNthFromEnd2]


class TestRemoveNthFromEnd(unittest.TestCase):
    def testRemoveNthFromEnd1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 3, 4, 5])
            self.assertEqual(repr(func(head=head, n=2)), "1->2->3->5")

    def testRemoveNthFromEnd2(self):
        for func in funcs:
            head = ListNode.fromArray([1])
            self.assertEqual(repr(func(head=head, n=1)), "None")

    def testRemoveNthFromEnd3(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2])
            self.assertEqual(repr(func(head=head, n=1)), "1")


if __name__ == "__main__":
    unittest.main()
