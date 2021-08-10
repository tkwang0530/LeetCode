"""
86. Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200]
-100 <= Node.val <= 100
-200 <= x <= 200
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space
2 Dummy Nodes
2. Recursion with List: O(n) time | O(n) space
3. Recursion with Tuple: O(n) time | O(n) space
"""



from typing import List, Tuple
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = dummySmall = ListNode(0)
        large = dummyLarge = ListNode(0)
        while head:
            if head.val < x:
                small.next = head
                small, head = head, head.next
            else:
                large.next = head
                large, head = head, head.next
        large.next = None
        small.next = dummyLarge.next
        return dummySmall.next

    def partition2(self, head: ListNode, x: int) -> ListNode:
        dummySmall = ListNode(0)
        dummyLarge = ListNode(0)
        pair = [dummySmall, dummyLarge]
        self.helper(head, pair, x)
        small, large = pair
        small.next = dummyLarge.next
        large.next = None
        return dummySmall.next
        
    def helper(self, head: ListNode, pair: List[ListNode], x: int) -> None:
        if not head:
            return
        if head.val < x:
            pair[0].next = head
            pair[0] = pair[0].next
        else:
            pair[1].next = head
            pair[1] = pair[1].next
        self.helper(head.next, pair, x)

    def partition3(self, head: ListNode, x: int) -> ListNode:
        small = dummySmall = ListNode(0)
        large = dummyLarge = ListNode(0)
        small, large = self.helper2(head, small, large, x)
        small.next = dummyLarge.next
        large.next = None
        return dummySmall.next
        
    def helper2(self, head: ListNode, small: ListNode, large: ListNode, x: int) -> Tuple[ListNode, ListNode]:
        if not head:
            return (small, large)
        if head.val < x:
            small.next = head
            small = small.next
        else:
            large.next = head
            large = large.next
        return self.helper2(head.next, small, large, x)



# Unit Tests
funcs = [Solution().partition, Solution().partition2, Solution().partition3]


class TestPartition(unittest.TestCase):
    def testPartition1(self):
        for func in funcs:
            head = ListNode.fromArray([1,4,3,2,5,2])
            x = 3
            self.assertEqual(repr(func(head=head,x=x)), "1->2->2->4->3->5->None")

    def testPartition2(self):
        for func in funcs:
            head = ListNode.fromArray([2,1])
            x = 2
            self.assertEqual(repr(func(head=head,x=x)), "1->2->None")

    def testPartition3(self):
        for func in funcs:
            head = None
            x = 2
            self.assertEqual(repr(func(head=head,x=x)), "None")


if __name__ == "__main__":
    unittest.main()
