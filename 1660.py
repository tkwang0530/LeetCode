"""
1660. Correct a Binary Tree
You have a binary tree with a small defect. There is exactly one invalid node where its right child incorrectly points to another node at the same depth but to the invalid node's right.

Given the root of the binary tree with this defect, root, return the root of the binary tree after removing this invalid node and every node underneath it (minus the node it incorrectly points to).

Example1:
Input: root = [1,2,3], fromNode = 2, toNode = 3
Output: [1,null,3]
Explanation: The node with value 2 is invalid, so remove it.

Example2:
Input: root = [8,3,1,7,null,9,4,2,null,null,null,5,6], fromNode = 7, toNode = 4
Output: [8,3,1,null,null,9,4,null,null,5,6]
Explanation: The node with value 7 is invalid, so remove it and the node underneath it, node 2.

Constraints:
- The number of nodes in the tree is in the range [3, 10^4].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- fromNode != toNode
- fromNode and toNode will exist in the tree and will be on the same depth.
- toNode is to the right of fromNode.
- fromNode.right is null in the initial tree from the test data.
"""

"""
Note:
1. Iterative BFS: O(n) time | O(n) space - where n is the number of nodes in the tree
"""


import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([(root, None)])
        visited = set([root])
        while queue:
            node, parent = queue.popleft()
            if node.right:
                if node.right in visited:
                    if parent.right == node:
                        parent.right = None
                    else:
                        parent.left = None
                    return root
                visited.add(node.right)
                queue.append((node.right, node))
            if node.left:
                visited.add(node.left)
                queue.append((node.left, node))
        return root


# Unit Tests
import unittest
funcs = [Solution().correctBinaryTree]

class TestCorrectBinaryTree(unittest.TestCase):
    def testCorrectBinaryTree1(self):
        for func in funcs:
            node2 = TreeNode(2)
            node3 = TreeNode(3)
            root = TreeNode(1, node2, node3)
            node2.right = node3
            root = func(root=root)
            self.assertEqual(root.val, 1)
            self.assertEqual(root.left, None)
            self.assertEqual(root.right.val, 3)

    def testCorrectBinaryTree2(self):
        for func in funcs:
            node4 = TreeNode(4, TreeNode(5), TreeNode(6))
            node7 = TreeNode(7, TreeNode(2))
            root = TreeNode(8, TreeNode(3, node7), TreeNode(1, TreeNode(9), node4))
            node7.right = node4
            root = func(root=root)
            self.assertEqual(root.val, 8)
            self.assertEqual(root.left.val, 3)
            self.assertEqual(root.left.left, None)
            self.assertEqual(root.left.right, None)
            self.assertEqual(root.right.val, 1)
            self.assertEqual(root.right.left.val, 9)
            self.assertEqual(root.right.right.val, 4)
            self.assertEqual(root.right.right.left.val, 5)
            self.assertEqual(root.right.right.right.val, 6)

if __name__ == "__main__":
    unittest.main()
