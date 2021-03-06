"""
145. Binary Tree Postorder Traversal
Given the root of a binary tree, return the postorder traversal of its node's values.

Example1:
        1
           \
            2
          /
        3
Input: root = [1, null, 2, 3]
Output: [3, 2, 1]

Example2:
Input: root = []
Output: []

Example3:
Input: root = [1]
Output: [1]

Example4:
        1
      /
    2
Input: root = [1,2]
Output: [2,1]

Example5:
    1
       \
        2
Input: root = [1,null,2]
Output: [2,1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trival, could you do it iteratively?
"""

"""
Note:
1. Recursion: O(n) time | O(h) space
2. Iteration (PreOrder like traversal then reverse the result): O(n) time | O(h) space
visited root -> right -> left
3. Iteration (track visited node with tuple): O(n) time | O(n) space
4. Iteration (one stack with preNode): O(n) time | O(n) space
5. Morris Traversal: O(n) time | O(1) space
ref: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45648/three-ways-of-iterative-postorder-traversing-easy-explanation
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        self.dfs(root, result)
        return result

    def dfs(self, root: TreeNode, result: List[int]):
        if root.left:
            self.dfs(root.left, result)
        if root.right:
            self.dfs(root.right, result)
        result.append(root.val)

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        result, stack = [], [root]
        if not root:
            return result
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        result, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    result.append(node.val)
                else:
                    # post-order (reversely)
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return result

    def postorderTraversal4(self, root: TreeNode) -> List[int]:
        result, stack = [], []

        if not root:
            return result
        preNode = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1] if stack else None
                if not root.right or root.right == preNode:
                    result.append(root.val)
                    stack.pop()
                    preNode, root = root, None
                else:
                    root = root.right
        return result

    def postorderTraversal5(self, root: TreeNode) -> List[int]:
        result = []

        if not root:
            return result
        
        def reverse(fromNode: TreeNode, toNode: TreeNode) -> None:
            if fromNode == toNode:
                return
            prev, current = fromNode, fromNode.right
            while prev != toNode:
                next = current.right
                current.right = prev
                prev, current = current, next

        dummy = TreeNode(0)
        dummy.left, root = root, dummy
        while root:
            if not root.left:
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    # if we already built the bridge, reverse the list from root.left to predecessor
                    node = predecessor
                    reverse(root.left, predecessor)
                    while node != root.left:
                        result.append(node.val)
                        node = node.right

                    # append node.val again since we are stopping at node = root.left
                    result.append(node.val)

                    # reverse back
                    reverse(predecessor, root.left)
                    predecessor.right = None
                    root = root.right
        return result
        


# Unit Tests
funcs = [Solution().postorderTraversal, Solution(
).postorderTraversal2, Solution().postorderTraversal3, Solution().postorderTraversal4, Solution().postorderTraversal5]


class TestPostorderTraversal(unittest.TestCase):
    def testPostorderTraversal1(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
            self.assertEqual(func(root=root), [3, 2, 1])

    def testPostorderTraversal2(self):
        for func in funcs:
            root = None
            self.assertEqual(func(root=root), [])

    def testPostorderTraversal3(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), [1])

    def testPostorderTraversal4(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2))
            self.assertEqual(func(root=root), [2, 1])

    def testPostorderTraversal4(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2))
            self.assertEqual(func(root=root), [2, 1])


if __name__ == "__main__":
    unittest.main()
