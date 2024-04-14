"""
404. Sum of Left Leaves
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf that is the left child of another node.

Example1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example2:
Input: root = [1]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""

"""
Note:
1. Recursive DFS (PreOrder Traversal): O(n) time | O(h) space
2. Recursive DFS (PostOrder Traversal): O(n) time | O(h) space
3. Iterative DFS (PreOrder Traversal): O(n) time | O(h) space
4. Iterative BFS: O(n) time | O(n) space
5. PreOrder Morris Traversal: O(n) time | O(1) space
"""

from typing import Optional, List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        container = [0]
        def dfs(node, parent):
            if not node.left and not node.right:
                if parent and parent.left == node:
                    container[0] += node.val
                return

            if node.left:
                dfs(node.left, node)

            if node.right:
                dfs(node.right, node)
        
        dfs(root, None)
        return container[0]

class Solution2:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        result = 0
        if root.left and not root.left.left and not root.left.right:
            result += root.left.val
        
        result += self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        return result

class Solution3:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        result = 0
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                if not node.left.left and not node.left.right:
                    result += node.left.val
                else:
                    stack.append(node.left)
        return result

class Solution4:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                if not node.left.left and not node.left.right:
                    result += node.left.val
                else:
                    queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

class Solution5:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0
        while root:
            if not root.left:
                root = root.right
            elif not root.left.left and not root.left.right:
                result += root.left.val
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    predecessor.right = None
                    root = root.right
        return result

# Unit Tests
import unittest
funcs = [Solution().sumOfLeftLeaves, Solution2().sumOfLeftLeaves, Solution3().sumOfLeftLeaves, Solution4().sumOfLeftLeaves, Solution5().sumOfLeftLeaves]

class TestSumOfLeftLeaves(unittest.TestCase):
    def testSumOfLeftLeaves1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
            self.assertEqual(func(root=root), 24)

    def testSumOfLeftLeaves2(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), 0)

if __name__ == "__main__":
    unittest.main()
