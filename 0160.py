"""
160. Intersection of Two Linked Lists
Given the head of two singly linked-lists headA and headB, return the node at which lists intersect. If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:
 a1 -> a2 -> c1 -> c2 -> c3
                    |
b1 -> b2 -> b3  

Constraints:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?
"""

"""
Note:
O(n) time | O(1) space
1. two pointer: currentA and currentB (start from headA and headB)
2. for the first round, keep move forward until hit the Null, and then reset to the other head
3. for the second round, keep move forward until they points to the same node.
4. if the two linked lists have no intersection at all, then the meeting pointer in second iteration must be the tail node of both lists, which is null.
"""


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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        currentA, currentB = headA, headB
        while currentA != currentB:
            currentA = headB if not currentA else currentA.next
            currentB = headA if not currentB else currentB.next
        return currentA


# Unit Tests
import unittest


class TestGetIntersectionNode(unittest.TestCase):
    def testGetIntersectionNode1(self):
        func = Solution().getIntersectionNode
        headA = ListNode.fromArray([4, 1, 8, 4, 5])
        headB = ListNode.fromArray([5, 6, 1])
        headB.next.next.next = headA.next.next
        self.assertEqual(repr(func(headA=headA, headB=headB)), "8->4->5")

    def testGetIntersectionNode2(self):
        func = Solution().getIntersectionNode
        headA = ListNode.fromArray([1, 9, 1, 2, 4])
        headB = ListNode.fromArray([3])
        headB.next = headA.next.next.next
        self.assertEqual(repr(func(headA=headA, headB=headB)), "2->4")

    def testGetIntersectionNode3(self):
        func = Solution().getIntersectionNode
        headA = ListNode.fromArray([1, 9, 1, 2, 4])
        headB = ListNode.fromArray([3, 4, 0, 1, 7])
        self.assertEqual(repr(func(headA=headA, headB=headB)), "None")


if __name__ == "__main__":
    unittest.main()