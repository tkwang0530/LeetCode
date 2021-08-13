"""
958. Check Completeness of a Binary Tree
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2^h nodes inclusive at the last level h.

Example1:
            1                                       
         /       \                            
       2          3                
    /     \        /
 4        5    6         
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example2:
            1                                       
         /       \                            
       2          3                
    /     \          \
 4        5         7
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Constraints:
The number of nodes in the tree is in the range [1, 100]
1 <= Node.val <= 1000
"""

"""
Note:
1. Iterative BFS: O(n) time | O(n) space
Track the hasNone property
"""


from collections import deque
from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        hasNone = False
        while len(queue) > 0:
            node = queue.popleft()
            if not node:
                hasNone = True
                continue
            if hasNone:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True



# Unit Tests
funcs = [Solution().isCompleteTree]


class TestIsCompleteTree(unittest.TestCase):
    def testIsCompleteTree1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
            self.assertEqual(func(root=root), True)

    def testIsCompleteTree2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None,TreeNode(7)))
            self.assertEqual(func(root=root), False)


if __name__ == "__main__":
    unittest.main()
