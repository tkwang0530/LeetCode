"""
669. Trim a Binary Search Tree
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

Example1:   
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Example2:
Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^4
The value of each node in the tree is unique.
root is guaranteed to be a valid binary search tree.
0 <= low <= high <= 10^4
"""

"""
Note:
1. Iterative BFS : O(n) time | O(n) space - where n is the number of nodes in the tree
2. Recursive DFS (PostOrder Traversal): O(n) time | O(n) space - where n is the number of nodes in the tree
"""




from typing import Optional
import unittest
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        queue = collections.deque([(root, None)])
        while queue:
            node, preNode = queue.popleft()
            isLower = node.val < low
            isHigher = node.val > high
            if not isLower and not isHigher:
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
                continue

            if preNode:
                if isLower:
                    preNode.left = node.right
                    if node.right:
                        queue.append((node.right, preNode))
                else:
                    preNode.right = node.left
                    if node.left:
                        queue.append((node.left, preNode))
            else:
                if isLower:
                    root.left = None
                    root = node.right
                else:
                    root.right = None
                    root = node.left
                if root:
                    queue.append((root, None))
        return root

    def trimBST2(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self.trimBST2(root.right, low, high)
        elif root.val > high:
            return self.trimBST2(root.left, low, high)

        root.left = self.trimBST2(root.left, low, high)
        root.right = self.trimBST2(root.right, low, high)
        return root


# Unit Tests
funcs = [Solution().trimBST, Solution().trimBST2]


class TestTrimBST(unittest.TestCase):
    def testTrimBST1(self):
        for func in funcs:
            node0 = TreeNode(0)
            node1 = TreeNode(1)
            node2 = TreeNode(2)
            node1.left, node1.right = node0, node2
            self.assertEqual(func(root=node1, low=1, high=2), node1)
            self.assertEqual(None, node1.left)
            self.assertEqual(node2, node1.right)

    def testTrimBST2(self):
        for func in funcs:
            node0 = TreeNode(0)
            node1 = TreeNode(1)
            node2 = TreeNode(2)
            node3 = TreeNode(3)
            node4 = TreeNode(4)
            node3.left, node3.right = node0, node4
            node0.right = node2
            node2.left = node1
            self.assertEqual(func(root=node3, low=1, high=3), node3)
            self.assertEqual(None, node3.right)
            self.assertEqual(node2, node3.left)
            self.assertEqual(node1, node2.left)
            self.assertEqual(None, node2.right)
            self.assertEqual(None, node1.right)
            self.assertEqual(None, node1.left)


if __name__ == "__main__":
    unittest.main()
