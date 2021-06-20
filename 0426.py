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
1. DFS (Boundary Walk): O(n) time | O(h) space
param(pred): 
pred to store the predeccessor
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
        pred = [dummy]
        self.dfs(root, pred)
        pred[0].right = dummy.right  # head
        dummy.right.left = pred[0]
        return dummy.right

    def dfs(self, treeNode: TreeNode, pred: List[TreeNode]):
        if treeNode.left is not None:
            self.dfs(treeNode.left, pred)
        treeNode.left = pred[0]
        pred[0].right = treeNode
        pred[0] = treeNode
        if treeNode.right is not None:
            self.dfs(treeNode.right, pred)


# Unit Tests


class TestTreeToDoublyList(unittest.TestCase):
    def testTreeToDoublyList1(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
        func = Solution().treeToDoublyList
        newRoot = func(root=root)
        self.assertEqual(newRoot.val, 1)
        self.assertEqual(newRoot.right.val, 2)
        self.assertEqual(newRoot.right.right.val, 3)
        self.assertEqual(newRoot.right.right.right.val, 4)
        self.assertEqual(newRoot.right.right.right.right.val, 5)
        self.assertEqual(newRoot.right.right.right.right.right.val, 1)


if __name__ == "__main__":
    unittest.main()
