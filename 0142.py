"""
142. Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return None

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Example1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?

Constraints:
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
"""

"""
Note:
1. Fast-Slow pointer: O(n) time | O(1) space
when fast meet slow, reset the fast to the head, and make it slower
S = X = P + Q => 2X = 2P + 2Q
F = 2X = P + Q + R + P
=> P = R
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
    def detectCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                break
        if not fast or not fast.next:
            return None
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

# Unit Tests

funcs = [Solution().detectCycle]


class TestDetectCycle(unittest.TestCase):
    def testDetectCycle1(self):
        for func in funcs:
            head = ListNode.fromArray([3, 2, 0, -4])
            head.next.next.next.next = head.next
            self.assertEqual(func(head=head).val, 2)

    def testDetectCycle2(self):
        for func in funcs:
            head = ListNode.fromArray([1, 2])
            head.next.next = head
            self.assertEqual(func(head=head).val, 1)

    def testDetectCycle3(self):
        for func in funcs:
            head = ListNode.fromArray([1])
            self.assertEqual(func(head=head), None)


if __name__ == "__main__":
    unittest.main()
