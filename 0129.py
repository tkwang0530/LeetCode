"""
129. Sum Root to Leaf Numbers
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
- For example, the root-to-leaf path 1->2->3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example1:
        1
      /   \
    2     3 
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example2:
               4
            /      \
          9         0
        /   \
      5      1        
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""

"""
Note:
1. Recursive DFS: O(n) time | O(h) space
2. Iterative DFS: O(n) time | O(h) space
3. Iterative BFS: O(n) time | O(n) space
"""




from typing import List
from collections import deque
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = [0]
        self.dfs(root, 0, result)
        return result[0]

    def dfs(self, root: TreeNode, temp: int, result: List[int]):
        if not root.left and not root.right:
            result[0] += temp * 10 + root.val
            return
        if root.left:
            self.dfs(root.left, temp * 10 + root.val, result)
        if root.right:
            self.dfs(root.right, temp * 10 + root.val, result)
        return

    def sumNumbers2(self, root: TreeNode) -> int:
        total = 0
        if not root:
            return 0
        stack = [(root, 0)]
        while stack:
            node, currentSum = stack.pop()
            currentSum += node.val
            if not node.left and not node.right:
                total += currentSum
            else:
                currentSum *= 10
                if node.right:
                    stack.append((node.right, currentSum))
                if node.left:
                    stack.append((node.left, currentSum))
        return total

    def sumNumbers3(self, root: TreeNode) -> int:
        queue, result = deque([]), 0
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                result += node.val
            if node.left:
                node.left.val += node.val * 10
                queue.append(node.left)

            if node.right:
                node.right.val += node.val * 10
                queue.append(node.right)
        return result


# Unit Tests
funcs = [Solution().sumNumbers, Solution().sumNumbers2, Solution().sumNumbers3]


class TestSumNumbers(unittest.TestCase):
    def testSumNumbers1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2), TreeNode(3))
            self.assertEqual(func(root=root), 25)

    def testSumNumbers2(self):
        for func in funcs:
            root = TreeNode(4, TreeNode(
                9, TreeNode(5), TreeNode(1)), TreeNode(0))
            self.assertEqual(func(root=root), 1026)


if __name__ == "__main__":
    unittest.main()
