"""
98. Validate Binary Search Tree
description: https://leetcode.com/problems/validate-binary-search-tree/description/
"""

"""
Note:
1. DFS (postOrder Traversal): O(n) time | O(h) space - where n is the number of nodes in the tree and h is the height of the tree
2. Iterative solution: O(n) time | O(n) space - where n is the number of nodes in the tree
3. Morris Traversal: O(n) time | O(1) space - where n is the number of nodes in the tree
"""



from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # root.val > lowerBound, root.val < upperBound
        def dfs(root, lowerBound, upperBound):
            if not root:
                return True

            validRoot = (root.val > lowerBound) and (root.val < upperBound)
            return validRoot and dfs(root.left, lowerBound, root.val) and dfs(root.right, root.val, upperBound)
        return dfs(root, float("-inf"), float("inf"))
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        previousVal = float("-inf")
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= previousVal:
                return False
            else:
                previousVal = root.val
                root = root.right
        return True

class Solution3:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        current, prev = root, None
        while current:
            if not current.left:
                if prev and prev.val >= current.val:
                    return False
                prev = current
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right != current and predecessor.right:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    if prev and prev.val >= current.val:
                        return False
                    prev = current
                    current = current.right
        return True

# Unit Tests
import unittest
funcs = [Solution().isValidBST, Solution2().isValidBST, Solution3().isValidBST]


class TestIsValidBST(unittest.TestCase):
    def testIsValidBST1(self):
        for isValidBST in funcs:
            root = TreeNode(2, TreeNode(1), TreeNode(3))
            self.assertEqual(isValidBST(root=root), True)

    def testIsValidBST2(self):
        for isValidBST in funcs:
            root = TreeNode(5, TreeNode(1), TreeNode(
                4, TreeNode(3), TreeNode(6)))
            self.assertEqual(isValidBST(root=root), False)


if __name__ == "__main__":
    unittest.main()
