"""
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example1:
            2
          /    \
        1       3
Input: root = [2, 1, 3]
Output: true

Example2:
            5
        /        \
      1          4
                /    \
              3       6
Input: root = [5, 1, 4, null, null, 3, 6]
Output: false
Explanation: The node's value is 5 but its right child's value is 4.
"""

"""
Note:
1. Recursive solution: O(n) time | O(n) space
validateBstHelper(root, minValue, maxValue)
2. Iterative solution: O(n) time | O(n) space
3. Morris Traversal: O(n) time | O(1) space
4. DFS: O(n) time | O(n) space
"""



from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validateBstHelper(root, float("-inf"), float("inf"))

    def validateBstHelper(self, root: TreeNode, minValue, maxValue) -> bool:
        if root is None:
            return True
        rootIsValid = root.val < maxValue and root.val > minValue
        leftIsValid = self.validateBstHelper(root.left, minValue, root.val)
        rightIsValid = self.validateBstHelper(root.right, root.val, maxValue)
        return rootIsValid and leftIsValid and rightIsValid

    def isValidBST2(self, root: TreeNode) -> bool:
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

    def isValidBST3(self, root: TreeNode) -> bool:
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
    
    def isValidBST4(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        result = [None, True] # [prevNode, isValid]
        self.dfs(root, result)
        return result[1]
    
    def dfs(self, root, result):
        if not root or not result[1]:
            return
        
        self.dfs(root.left, result)
        if result[0] and result[0].val >= root.val:
            result[1] = False
            return
        result[0] = root
        self.dfs(root.right, result)

# Unit Tests
import unittest
funcs = [Solution().isValidBST, Solution().isValidBST2, Solution().isValidBST3, Solution().isValidBST4]


class TestIsValidBST(unittest.TestCase):
    def testIsValidBST1(self):
        for func in funcs:
            root = TreeNode(2, TreeNode(1), TreeNode(3))
            self.assertEqual(func(root=root), True)

    def testIsValidBST2(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(1), TreeNode(
                4, TreeNode(3), TreeNode(6)))
            self.assertEqual(func(root=root), False)


if __name__ == "__main__":
    unittest.main()
