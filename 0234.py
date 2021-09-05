"""
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome.

Example1:
1->2->2->1
Input: head = [1,2,2,1]
Output: true

Example2:
1->2
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space
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
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = fast = dummy = ListNode(0)
        dummy.next = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        l2 = slow.next
        slow.next = None
        l1 = dummy.next
        
        l2 = self.reverse(l2)
        while l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
    
    def reverse(self, head) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev, head = head, next
        return prev

# Unit Tests
import unittest
funcs = [Solution().isPalindrome]

class TestIsPalindrome(unittest.TestCase):
    def testIsPalindrome1(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 2, 1])
            self.assertEqual(func(head=head), True)

    def testIsPalindrome2(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2, 3, 2, 1])
            self.assertEqual(func(head=head), True)

    def testIsPalindrome3(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2])
            self.assertEqual(func(head=head), False)

    def testIsPalindrome4(self):
        for func in funcs:
            head = ListNode.fromArray([1])
            self.assertEqual(func(head=head), True)
    


if __name__ == "__main__":
    unittest.main()