"""
114. Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.

- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example1:
            1                                       
         /     \                            
       2        5                
    /     \         \
 3         4        6          
1 -> 2 -> 3 -> 4 -> 5 -> 6       
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example2:
Input: root = []
Output: []

Example3:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""

"""
Note:
1. Iterative DFS: O(n) time | O(h) space
2. Modified Morris Traversal: O(n) time | O(1) space
3. Built preorder value list then build flatten Binary Tree: O(n) time | O(n) space
"""



from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # TEST ONLY
    def __repr__(self) -> str:
        return f"{self.val}->{self.right}"


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return root
        current = TreeNode(0)
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            current.left = None
            current.right = node
            current = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def flatten2(self, root: TreeNode) -> None:
        if not root:
            return root
        current = root
        while current:
            if current.left:
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = current.right
                current.right = current.left
                current.left = None
            current = current.right

    def flatten3(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder = []
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        prev = root
        root.left, root.right = None, None
        for i in range(1, len(preorder)):
            prev.right = TreeNode(preorder[i])
            prev = prev.right



# Unit Tests
funcs = [Solution().flatten, Solution().flatten2, Solution().flatten3]


class TestFlatten(unittest.TestCase):
    def testFlatten1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
            func(root=root)
            self.assertEqual(repr(root), "1->2->3->4->5->6->None")

    def testFlatten2(self):
        for func in funcs:
            root = None
            func(root=root)
            self.assertEqual(repr(root), "None")

    def testFlatten3(self):
        for func in funcs:
            root = TreeNode(0)
            func(root=root)
            self.assertEqual(repr(root), "0->None")


if __name__ == "__main__":
    unittest.main()
