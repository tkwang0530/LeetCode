"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
Return the following binary tree:
        3
      /    \
    9     20
           /   \
         15     7  
"""

"""
Note:
1. Tree Construction - Top Down: O(n) time | O(n + h) space
preorder: self left right
inorder: left self right
preprocessing: map a value to its index in inorder list
lookup: { 9: 0, 3: 1, 15:2, 20:3, 7:4}
2. Iteration with stack: O(n) time | O(n) space
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i
        return self.buildTreeHelper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, lookup)
    
    def buildTreeHelper(self, preorder, startP, endP, inorder, startI, endI, lookup) -> TreeNode:
        if startP > endP:
            return None
        root = TreeNode(preorder[startP])
        rootIndex = lookup[root.val]
        numLeft = rootIndex - startI
        root.left = self.buildTreeHelper(preorder, startP + 1, startP + numLeft, inorder, startI, rootIndex - 1, lookup)
        root.right = self.buildTreeHelper(preorder, startP + numLeft + 1, endP, inorder, rootIndex + 1, endI, lookup)
        return root

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i
        
        value = preorder[0]
        root = TreeNode(value)
        stack = [root]

        for i in range(1, len(preorder)):
            value = preorder[i]
            node = TreeNode(value)

            if lookup[value] < lookup[stack[-1].val]:
                # the new node is on the left of the last node,
                # so it must be its left child (that's the way inorder works)
                stack[-1].left = node
            else:
                # the new node is on the right of the last node,
                # so it must be the right child of either the last node or one of the last node's ancestors.
                # pop the stack until we either run out of ancestors
                # or the node at the top of the stack is to the right of the new node
                parent = None
                while len(stack) > 0 and lookup[value] > lookup[stack[-1].val]:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        return root

# Unit Tests
funcs = [Solution().buildTree, Solution().buildTree2]

class TestBuildTree(unittest.TestCase):
    def testBuildTree1(self):
        for func in funcs:
            preorder = [3, 9, 20, 15, 7]
            inorder = [9, 3, 15, 20, 7]
            buildedTreeRoot = func(preorder=preorder, inorder=inorder)
            self.assertEqual(buildedTreeRoot.val, 3)
            self.assertEqual(buildedTreeRoot.left.val, 9)
            self.assertEqual(buildedTreeRoot.right.val, 20)
            self.assertEqual(buildedTreeRoot.right.left.val, 15)
            self.assertEqual(buildedTreeRoot.right.right.val, 7)

    def testBuildTree2(self):
        for func in funcs:
            preorder = [1, 2, 3]
            inorder = [3, 2, 1]
            buildedTreeRoot = func(preorder=preorder, inorder=inorder)
            self.assertEqual(buildedTreeRoot.val, 1)
            self.assertEqual(buildedTreeRoot.left.val, 2)
            self.assertEqual(buildedTreeRoot.right, None)
            self.assertEqual(buildedTreeRoot.left.left.val, 3)
            self.assertEqual(buildedTreeRoot.left.right, None)


if __name__ == "__main__":
    unittest.main()
