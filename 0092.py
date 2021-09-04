"""
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space
2. Two Pointers (one pass): O(n) time | O(1) space
"""



from typing import Optional, Tuple
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        beforeStart = dummy = ListNode(0)
        dummy.next = head
        while right > 0:
            left -= 1
            right -= 1
            
            if left == 1:
                beforeStart = head
            elif left == 0:
                start = head
            
            if right == 0:
                end = head
                afterEnd = head.next
            head = head.next
        
        end.next = None
        
        
        reversedHead, reversedTail = self.reverse(start)
        beforeStart.next = reversedHead

        
        reversedTail.next = afterEnd
        return dummy.next
        
    
    def reverse(self, head) -> Tuple[ListNode]: # head and tail of the reversed linked list
        prev = dummy = ListNode(0)
        dummy.next = head
        while head:
            next = head.next
            head.next = prev
            prev, head = head, next
        return (prev, dummy.next)

    
    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        beforeStart = dummy = ListNode(0)
        dummy.next = head
        while left > 0:
            left -= 1
            right -= 1
            if left == 1:
                beforeStart = head
            elif left == 0:
                start = head
            head = head.next
        
        prev = start
        while right > 0:
            right -= 1
            next = head.next
            head.next = prev
            prev, head = head, next
        
        beforeStart.next = prev
        start.next = head
        return dummy.next
            



# Unit Tests
funcs = [Solution().reverseBetween, Solution().reverseBetween2]
class TestReverseBetween(unittest.TestCase):
    def testReverseBetween1(self):
        for func in funcs:
            head = ListNode.fromArray([1,2,3,4,5])
            left = 2
            right = 4
            self.assertEqual(repr(func(head=head,left=left,right=right)), "1->4->3->2->5->None")

    def testReverseBetween2(self):
        for func in funcs:
            head = ListNode.fromArray([5])
            left = 1
            right = 1
            self.assertEqual(repr(func(head=head,left=left,right=right)), "5->None")

if __name__ == "__main__":
    unittest.main()
