"""
116. Populating Next Right Pointers in Each Node
You are given a perfect binary tree where all leaves are on the same level, and every parents has two children. The binary tree has the following definition:
struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example2:
Input: root = []
Output: []
"""

"""
Note:
1. Recursion: O(n) time | O(logn) space
2. Iteration: O(n) time | O(1) space
keep track the startNode
"""

import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: TreeNode) -> TreeNode:
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

    def connect2(self, root: TreeNode) -> TreeNode:
        startNode = root
        while startNode:
            current = startNode
            while current:
                if current.left:
                    current.left.next = current.right
                if current.right and current.next:
                    current.right.next = current.next.left
                current = current.next
            startNode = startNode.left
        return root

# Unit Tests
funcs = [Solution().connect, Solution().connect2]


class TestConnect(unittest.TestCase):
    def testConnect1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
            root = func(root)
            self.assertEqual(root.next, None)
            self.assertEqual(root.left.next, root.right)
            self.assertEqual(root.right.next, None)
            self.assertEqual(root.left.left.next, root.left.right)
            self.assertEqual(root.left.right.next, root.right.left)
            self.assertEqual(root.right.left.next, root.right.right)
            self.assertEqual(root.right.right.next, None)

    def testConnect2(self):
        for func in funcs:
            root = None
            root = func(root)
            self.assertEqual(root, None)

if __name__ == "__main__":
    unittest.main()
