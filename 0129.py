"""
129. Sum Root to Leaf Numbers
description: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
"""

"""
Note:
1. Recursive DFS: O(n) time | O(h) space
2. Recursive DFS (PostOrder Traversal): O(n) time | O(h) space
ref: https://leetcode.com/problems/sum-root-to-leaf-numbers/solutions/1556417/c-python-recursive-iterative-dfs-bfs-morris-traversal-o-1-beats-100
3. Iterative DFS: O(n) time | O(h) space
4. Iterative BFS: O(n) time | O(n) space
"""




from typing import Optional
from collections import deque
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        container = [0]
        def dfs(root, preVal):
            if not root.left and not root.right:
                container[0] += preVal*10+root.val

            if root.left:
                dfs(root.left, preVal*10+root.val)
            if root.right:
                dfs(root.right, preVal*10+root.val)
        dfs(root, 0)
        return container[0]

class Solution2:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, result):
            if not root:
                return 0
            result = result * 10 + root.val
            if not root.left and not root.right:
                return result
            return dfs(root.left, result) + dfs(root.right, result)

        return dfs(root, 0)
    
class Solution3:
    def sumNumbers(self, root: TreeNode) -> int:
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

class Solution4:
    def sumNumbers(self, root: TreeNode) -> int:
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
funcs = [Solution().sumNumbers, Solution2().sumNumbers, Solution3().sumNumbers, Solution4().sumNumbers]


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
