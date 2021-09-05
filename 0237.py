"""
237. Delete Node in a Linked List
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Example1:
4->"5"->1->9    =>    4->1->9
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example2:
4->5->"1"->9    =>    4->5->9
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Constraints:
The number of nodes in the list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node
"""

"""
Note:
1. copy the value of next node: O(1) time | O(1) space
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
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# Unit Tests
import unittest
funcs = [Solution().deleteNode]

class TestDeleteNode(unittest.TestCase):
    def testDeleteNode1(self):
        for func in funcs:
            head = ListNode.fromArray([4, 5, 1, 9])
            node = head.next
            func(node=node)
            self.assertEqual(repr(head), "4->1->9->None")

    def testDeleteNode2(self):
        for func in funcs:
            head = ListNode.fromArray([4, 5, 1, 9])
            node = head.next.next
            func(node=node)
            self.assertEqual(repr(head), "4->5->9->None")
    


if __name__ == "__main__":
    unittest.main()