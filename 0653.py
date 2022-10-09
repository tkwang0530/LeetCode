"""
653. Two Sum IV - Input is a BST
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example1:   
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 10^4]
-10^4 <= Node.val <= 10^4
root is guaranteed to be a valid binary search tree.
-10^5 <= k <= 10^5
"""

"""
Note:
1. Recursive DFS (Inorder Traversal) + Two Pointers: O(n) time | O(n) space - where n is the number of nodes in the tree
"""




from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)
        left = 0
        right = len(inorder) - 1
        while left < right:
            current = inorder[left] + inorder[right]
            if current == k:
                return True
            elif current > k:
                right -= 1
            else:
                left += 1
        return False


# Unit Tests
funcs = [Solution().findTarget]


class TestFindTarget(unittest.TestCase):
    def testFindTarget1(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(3, TreeNode(
                2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
            k = 9
            self.assertEqual(func(root=root, k=k), True)

    def testFindTarget2(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(3, TreeNode(
                2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
            k = 28
            self.assertEqual(func(root=root, k=k), False)


if __name__ == "__main__":
    unittest.main()
