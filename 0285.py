"""
285. Inorder Successor in BST
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val

Example1:
       2
     /   \
    1     3 
Input: root = [2, 1, 3], p = 1
Output: 2
Explanation: 1's in-order successor is 2. Note that both p and the return value is of TreeNode type.

Example2:
             5
          /     \
        3        6
      /    \
    2       4
  /
1
Input: root = [5, 3, 6, 2, 4, null, null, 1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
"""

"""
Note:
1. Recursion: O(h) time | O(h) space
2. Iterative: O(h) time | O(1) space
3. Recursion: (successorContainer): O(h) time | O(h) space
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        # return self.helper(root, p)
        if not root:
            return
        if root.val > p.val:
            return self.inorderSuccessor(root.left, p) or root
        else:
            return self.inorderSuccessor(root.right, p)

    def inorderSuccessor2(self, root: TreeNode, p: TreeNode) -> TreeNode:
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

    def inorderSuccessor3(self, root: TreeNode, p: TreeNode) -> TreeNode:
        result = [None]
        self.inorderSuccessorHelper(root, p, result)
        return result[0]

    def inorderSuccessorHelper(self, root: TreeNode, p: TreeNode, result: List[TreeNode]):
        if not root:
            return
        if root.val > p.val:
            result[0] = root
            self.inorderSuccessorHelper(root.left, p, result)
        else:
            self.inorderSuccessorHelper(root.right, p, result)

        # Unit Tests
funcs = [Solution().inorderSuccessor, Solution().inorderSuccessor2,
         Solution().inorderSuccessor3]


class TestInorderSuccessor(unittest.TestCase):
    def testInorderSuccessor1(self):
        for func in funcs:
            p = TreeNode(1)
            targetNode = root = TreeNode(2, p, TreeNode(3))
            self.assertEqual(func(root=root, p=p), targetNode)

    def testInorderSuccessor2(self):
        p = TreeNode(6)
        root = TreeNode(5, TreeNode(3, TreeNode(
            2, TreeNode(1)), TreeNode(4)), p)
        for func in funcs:
            root = TreeNode(1, TreeNode(2))
            self.assertEqual(func(root=root, p=p), None)


if __name__ == "__main__":
    unittest.main()
