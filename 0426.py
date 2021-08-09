"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. 

For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer to its successor. You should return the pointer to the smallest element of the linked list.

Note: 
prev -> left, next -> right
inorder traversal of BST gives sorted list
Example1:
Input: root = [4, 2, 5, 1, 3], 
            4
         /      \
      2          5
    /   \ 
  1     3           

Outputs: [1, 2, 3, 4, 5] (circular doubly linked list) (5 should connect to 1)
"""

"""
Note:
1. Recursive DFS: O(n) time | O(h) space
use prev to store the predeccessor
2. Iterative DFS: O(n) time | O(h) space
3. Morris traversal: O(n) time | O(1) space
"""




from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        dummy = TreeNode(None)
        prev = [dummy]
        self.dfs(root, prev)
        prev[0].right = dummy.right  # head
        dummy.right.left = prev[0]
        return dummy.right

    def dfs(self, treeNode: TreeNode, prev: List[TreeNode]):
        if treeNode.left is not None:
            self.dfs(treeNode.left, prev)
        treeNode.left = prev[0]
        prev[0].right = treeNode
        prev[0] = treeNode
        if treeNode.right is not None:
            self.dfs(treeNode.right, prev)

    def treeToDoublyList2(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        prev = dummy = TreeNode(0)
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            prev.right = node
            node.left = prev

            prev = node
            node = node.right
        dummy.right.left = prev
        prev.right = dummy.right
        return dummy.right

    def treeToDoublyList3(self, root: TreeNode) -> TreeNode:
        current = root
        prev = dummy = TreeNode(0)
        while current is not None:
            if current.left is None:
                prev.right = current
                current.left = prev
                prev = current
                current = current.right
            else:
                # find the predecessor
                predecessor = current.left
                while predecessor.right != current and predecessor.right is not None:
                    predecessor = predecessor.right

                # if right node is None then go left after establishing link from predecessor to current
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:  # left is already visit. Go right after visiting current.
                    predecessor.right = None
                    prev.right = current
                    current.left = prev
                    prev = current
                    current = current.right
        dummy.right.left = prev
        prev.right = dummy.right
        return dummy.right


# Unit Tests
funcs = [Solution().treeToDoublyList, Solution().treeToDoublyList2, Solution().treeToDoublyList3]
class TestTreeToDoublyList(unittest.TestCase):
    def testTreeToDoublyList1(self):
        for func in funcs:
            root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
            newRoot = func(root=root)
            self.assertEqual(newRoot.val, 1)
            self.assertEqual(newRoot.right.val, 2)
            self.assertEqual(newRoot.right.right.val, 3)
            self.assertEqual(newRoot.right.right.right.val, 4)
            self.assertEqual(newRoot.right.right.right.right.val, 5)
            self.assertEqual(newRoot.right.right.right.right.right.val, 1)


if __name__ == "__main__":
    unittest.main()
