"""
1367. Linked List in Binary Tree
description: https://leetcode.com/problems/linked-list-in-binary-tree/description/
"""

"""
Note:
1. dfs+memo: O(nm) time | O(nm) space - where n is the number of nodes in the tree and m is the number of nodes in the linked list
"""




from collections import deque
import functools
from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        @functools.lru_cache(None)
        def dfs(listNode, treeNode) -> bool:
            if not listNode:
                return True
            if not treeNode:
                return False

            hasSubPath = False
            
            # skip
            hasSubPath = hasSubPath or dfs(head, treeNode.left) or dfs(head, treeNode.right)

            # use if match
            if listNode.val == treeNode.val:
                hasSubPath = hasSubPath or dfs(listNode.next, treeNode.left) or dfs(listNode.next, treeNode.right)

            return hasSubPath
        return dfs(head, root)

# Unit Tests
funcs = [Solution().isSubPath]


class TestIsSubPath(unittest.TestCase):
    def testIsSubPath1(self):
        for func in funcs:
            head = ListNode(4, ListNode(2, ListNode(8)))
            root = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
            self.assertEqual(func(head=head, root=root), True)
    
    def testIsSubPath2(self):
        for func in funcs:
            head = ListNode(1, ListNode(4, ListNode(2, ListNode(6))))
            root = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
            self.assertEqual(func(head=head, root=root), True)

    def testIsSubPath3(self):
        for func in funcs:
            head = ListNode(1, ListNode(4, ListNode(2, ListNode(6, ListNode(8)))))
            root = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
            self.assertEqual(func(head=head, root=root), False)


if __name__ == "__main__":
    unittest.main()
