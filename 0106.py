"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example1:
        3
     /      \
   9       20
           /    \
        15     7      
Input: inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3]
Output: [3,9,20,null,null,15,7]

Example2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each Value of postorder also appears inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to the the postorder traversal of the tree.
"""

"""
Note:
1. Tree Construction - Top Down: O(n) time | O(n + h) space
inorder: left self right
postorder: left right self
preprocessing: map a value to its index in inorder list
lookup: { 9: 0, 3: 1, 15:2, 20:3, 7:4}
"""


from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i
        return self.buildTreeHelper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, lookup)

    def buildTreeHelper(self, inorder, startI, endI, postorder, startP, endP, lookup) -> TreeNode:
        if startI > endI:
            return
        root = TreeNode(postorder[endP])
        rootIndex = lookup[root.val]
        numLeft = rootIndex - startI
        root.left = self.buildTreeHelper(inorder, startI, rootIndex-1, postorder, startP, startP + numLeft - 1, lookup)
        root.right = self.buildTreeHelper(inorder, rootIndex + 1, endI, postorder, startP + numLeft, endP - 1, lookup)
        return root
        

# Unit Tests
import unittest
funcs = [Solution().buildTree]

def inorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    result = []
    def dfs(root):
        if root.left:
            dfs(root.left)
        result.append(root.val)
        if root.right:
            dfs(root.right)
    dfs(root)
    return result

def postorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    result = []
    def dfs(root):
        if root.left:
            dfs(root.left)
        if root.right:
            dfs(root.right)
        result.append(root.val)
    dfs(root)
    return result
        

class TestBuildTree(unittest.TestCase):
    def testBuildTree1(self):
        for func in funcs:
            inorder = [9,3,15,20,7]
            postorder = [9,15,7,20,3]
            root = func(inorder=inorder, postorder=postorder)
            self.assertEqual(inorderTraversal(root), inorder)
            self.assertEqual(postorderTraversal(root), postorder)

    def testBuildTree1(self):
        for func in funcs:
            inorder = [-1]
            postorder = [-1]
            root = func(inorder=inorder, postorder=postorder)
            self.assertEqual(inorderTraversal(root), inorder)
            self.assertEqual(postorderTraversal(root), postorder)


if __name__ == "__main__":
    unittest.main()
