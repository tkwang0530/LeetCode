"""
141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Example1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""

"""
Note:
1. Fast-Slow pointer: O(n) time | O(1) space
find if the fast pointer could catch up the slow pointer
2. Using Dictionary: O(n) time | O(n) space
3. Using node.val as marker: O(n) time | O(1) space
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


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


# Unit Tests

funcs = [Solution().hasCycle]


class TestHasCycle(unittest.TestCase):
    def testHasCycle1(self):
        for func in funcs:
            head = ListNode.fromArray([3, 2, 0, -4])
            head.next.next.next.next = head.next
            self.assertEqual(func(head=head), True)

    def testHasCycle2(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2])
            head.next.next = head
            self.assertEqual(func(head=head), True)

    def testHasCycle3(self):
        for func in funcs:
            head = ListNode.fromArray([1])
            self.assertEqual(func(head=head), False)


if __name__ == "__main__":
    unittest.main()
