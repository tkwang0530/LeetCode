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
1. Tree Construction - Slow-Fast Pointers: O(nlogn) time | O(logn) space
2. DFS (track head and tail of each sub tree): O(nlogn) time | O(logn) space
3. Convert linked list to array then do PreOrder Traversal: O(n) time | O(n) space
"""

from typing import List
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

    def sortedListToBST2(self, head: ListNode) -> TreeNode:
        if not head:
            return head
        return self.dfs(head, None)
    
    def dfs(self, head: ListNode, tail: ListNode) -> TreeNode:
        fast = slow = head
        if head == tail:
            return None
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        
        root = TreeNode(slow.val)
        root.left = self.dfs(head, slow)
        root.right = self.dfs(slow.next, tail)
        return root

    def sortedListToBST3(self, head: ListNode) -> TreeNode:
        arr = self.convertToArray(head)
        return self.dfs2(arr, 0, len(arr) - 1)
    
    def convertToArray(self, head) -> List[int]:
        result = []
        if not head:
            return result
        while head:
            result.append(head.val)
            head = head.next
        return result
    
    def dfs2(self, arr, left, right) -> TreeNode:
        if left > right:
            return None
        mid = left + (right - left) // 2
        root = TreeNode(arr[mid])
        root.left = self.dfs2(arr, left, mid-1)
        root.right = self.dfs2(arr, mid + 1, right)
        return root

# Unit Tests
import unittest
class TestSortedListToBST(unittest.TestCase):
    # TODO: UNITTEST
    def testSortedListToBST1(self):
        pass


if __name__ == "__main__":
    unittest.main()
