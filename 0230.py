"""
230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Example1:
        3
      /    \
    1       4
       \
        2

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example2:
                        5
                    /       \
                  3         6
                /    \
             2        4
           /
        1
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

"""
Note:
1. Iterative (DFS Inorder Traveral): O(n) time | O(h) space
2. Recursive (DFS Inorder Traveral): O(n) time | O(h) space
3. Morris Traversal: O(n) time | O(1) space
"""


from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        node = root
        while len(stack) > 0 or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                break
            node = node.right
        return node.val

    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        result = [0, k] # [value, curretK]
        self.dfs(root, result)
        return result[0]
    
    def dfs(self, node: TreeNode, result: List[int]) -> None:
        if result[1] < 0:
            return
        if node.left:
            self.dfs(node.left, result)
        
        result[1] -= 1
        if result[1] == 0:
            result[0] = node.val
        
        if node.right:
            self.dfs(node.right, result)

    def kthSmallest3(self, root: TreeNode, k: int) -> int:
        node = root
        while node:
            if not node.left:
                k -= 1
                if k == 0:
                    break
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    k -= 1
                    if k == 0:
                        break
                    node = node.right
        return node.val


# Unit Tests
funcs = [Solution().kthSmallest, Solution().kthSmallest2, Solution().kthSmallest3]


class TestKthSmallestl(unittest.TestCase):
    def testKthSmallestl1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
            self.assertEqual(func(root=root, k=1), 1)

    def testKthSmallestl2(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(3, TreeNode(
                2, TreeNode(1)), TreeNode(4)), TreeNode(6))
            self.assertEqual(func(root=root, k=3), 3)


if __name__ == "__main__":
    unittest.main()
