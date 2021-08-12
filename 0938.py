"""
938. Range Sum of BST
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high]

Example1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:
The number of nodes in the tree is in the range [1, 2 * 10^4].
1 <= Node.val <= 10^5
1 <= low <= high <= 10^5
All Node.val are unique
"""

"""
Note:
1. Recursive solution: O(n) time | O(n) space
2. Iterative solution: O(n) time | O(n) space
3. Morris traversal: O(n) time | O(1) space
"""




from typing import List, Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result = [0]
        self.dfs(root, low, high, result)
        return result[0]

    def dfs(self, root: TreeNode, low: int, high: int, result: List[int]) -> None:
        if low <= root.val and root.val <= high:
            result[0] += root.val
        if low <= root.val and root.left:
            self.dfs(root.left, low, high, result)
        if root.val <= high and root.right:
            self.dfs(root.right, low, high, result)

    def rangeSumBST2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result, stack = 0, [root]
        while len(stack) > 0:
            node = stack.pop()
            if low <= node.val and node.val <= high:
                result += node.val
            if node.val <= high and node.right:
                stack.append(node.right)
            if low <= node.val and node.left:
                stack.append(node.left)

        return result

    def rangeSumBST3(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result = 0
        while root:
            if not root.left or root.val < low:
                if root.val > high:
                    return result
                if low <= root.val and root.val <= high:
                    result += root.val
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = root
                    if root.val <= high:
                        result += root.val
                    root = root.left
                else:
                    predecessor.right = None
                    root = root.right
        return result

# Unit Tests
funcs = [Solution().rangeSumBST, Solution().rangeSumBST2, Solution().rangeSumBST3]


class TestRangeSumBST(unittest.TestCase):
    def testRangeSumBST1(self):
        for func in funcs:
            root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None,TreeNode(18)))
            self.assertEqual(func(root=root, low=7, high=15), 32)

    def testRangeSumBST2(self):
        for func in funcs:
            root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))), TreeNode(15, TreeNode(13), TreeNode(18)))
            self.assertEqual(func(root=root, low=6, high=10), 23)


if __name__ == "__main__":
    unittest.main()
