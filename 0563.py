"""
563. Binary Tree Tilt
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

Example1:
Input: root = [1,2,3]
Output: 1
Explanation: 
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1

Example2:
Input: root = [4,2,9,3,5,null,7]
Output: 15
Explanation: 
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 5 : |0-0| = 0 (no children)
Tilt of node 7 : |0-0| = 0 (no children)
Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15

Example3:
Input: root = [21,7,14,1,1,2,2,3,3]
Output: 9
"""

"""
Note:
1. Recursive DFS(PostOrder Traversal): O(n) time | O(h) space - where n is the number of nodes in the tree and h is the height of the tree
"""




from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0  # (sum, sumOftilt)

            leftSum, leftTilt = dfs(node.left)
            rightSum, rightTilt = dfs(node.right)
            return node.val+leftSum+rightSum, abs(leftSum-rightSum) + leftTilt + rightTilt
        return dfs(root)[1]


# Unit Tests
funcs = [Solution().findTilt]


class TestFindTilt(unittest.TestCase):
    def testFindTilt1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2), TreeNode(3))
            self.assertEqual(func(root=root), 1)

    def testFindTilt2(self):
        for func in funcs:
            root = TreeNode(4, TreeNode(2, TreeNode(
                3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))
            self.assertEqual(func(root=root), 15)

    def testFindTilt3(self):
        for func in funcs:
            root = TreeNode(21, TreeNode(7, TreeNode(1, TreeNode(3), TreeNode(
                3)), TreeNode(1)), TreeNode(14, TreeNode(2), TreeNode(2)))
            self.assertEqual(func(root=root), 9)


if __name__ == "__main__":
    unittest.main()
