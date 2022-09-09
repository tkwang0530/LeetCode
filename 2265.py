"""
2265. Count Nodes Equal to Average of Subtree
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
Note:
- The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
- A subtree of root is a tree consisting of root and all of its descendants.

Example1:   
Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

Example2:
Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
"""

"""
Note:
1. Recursion (DFS PostOrder Traversal): O(n) time | O(n) space
"""




from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0, 0)  # nodeCount, validCount, sum

            left, right = dfs(root.left), dfs(root.right)
            leftSum, rightSum = left[2], right[2]
            leftNodeCount, rightNodeCount = left[0], right[0]
            leftValidCount, rightValidCount = left[1], right[1]

            nodeCount = leftNodeCount+rightNodeCount+1
            currentSum = root.val + leftSum + rightSum
            validCount = leftValidCount + rightValidCount + \
                (root.val == int(currentSum // nodeCount))
            return nodeCount, validCount, currentSum
        return dfs(root)[1]


# Unit Tests
funcs = [Solution().averageOfSubtree]


class TestAverageOfSubtree(unittest.TestCase):
    def testAverageOfSubtree1(self):
        for func in funcs:
            root = TreeNode(4, TreeNode(8, TreeNode(
                0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))
            self.assertEqual(func(root=root), 5)

    def testAverageOfSubtree2(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), 1)


if __name__ == "__main__":
    unittest.main()
