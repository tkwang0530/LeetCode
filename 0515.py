"""
515. Find Largest Value in Each Tree Row
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed)

Example1:
            1
          /   \
        3     2
      /    \      \
    5      3      9 
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example2:
Input: root = [1,2,3]
Output: [1,3]

Example3:
Input: root = [1]
Output: [1]

Example4:
Input: root = [1,null,2]
Output: [1,2]
"""

"""
Note:
1. Iterative BFS: O(n) time | O(n) space
"""



from collections import deque
from typing import List, Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while len(queue) > 0:
            maxValue = float("-inf")
            queueLength = len(queue)
            for _ in range(queueLength):
                node = queue.popleft()
                maxValue = max(maxValue, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(maxValue)
        return result

# Unit Tests
funcs = [Solution().largestValues]


class TestLargestValues(unittest.TestCase):
    def testLargestValues1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
            self.assertEqual(func(root=root), [1, 3, 9])

    def testLargestValues2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2), TreeNode(3))
            self.assertEqual(func(root=root), [1, 3])

    def testLargestValues3(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), [1])

    def testLargestValues4(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2))
            self.assertEqual(func(root=root), [1, 2])


if __name__ == "__main__":
    unittest.main()
