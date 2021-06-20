"""
109. Convert Sorted List to Binary Search Tree
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example1:
Input: head = [-10, -3, 0, 5, 9]
One possible answer is: [0, -3, 9, -10, null, 5]
-10 -> -3 -> 0 -> 5 -> 9
        0
      /    \
    -3     9
    /       /
-10     5  
"""

"""
Note:
1. Tree Construction - Slow-Fast Pointers: O(n) time | O(n) space
"""




from typing import List
import unittest
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        if pre:
            pre.next = None  # cut down the left child
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


# Unit Tests


class TestSortedListToBST(unittest.TestCase):
    # TODO: UNITTEST
    def testSortedListToBST1(self):
        head = ListNode(-10, ListNode(-3,
                        ListNode(0, ListNode(5, ListNode(9)))))
        func = Solution().sortedListToBST
        pass


if __name__ == "__main__":
    unittest.main()
