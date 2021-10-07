"""
572. Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree "tree" is a tree that consists of a node in tree and all of this node's descendants. The tree "tree" could also be considered as a subtree of itself.

Example1:
            3                  
         /     \            
       4       5            4
      /  \                   /  \
    1    2                1   2
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4
"""

"""
Note:
1. Recursion: O(mn) time | O(m) space - where m is the number of nodes in the 1st tree and n is the number of nodes in the 2nd tree
Note that the Space complexity is O(height of 1st tree) and the worse case is O(m)
"""

import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: return True
        if not s: return False
        
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

# Unit Tests
funcs = [Solution().isSubtree]


class TestIsSameTree(unittest.TestCase):
    def testIsSameTree1(self):
        for func in funcs:
            s = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
            t = TreeNode(4, TreeNode(1), TreeNode(2))
            self.assertEqual(func(s=s, t=t), True)

    def testIsSameTree2(self):
        for func in funcs:
            s = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
            t = TreeNode(4, TreeNode(1), TreeNode(2))
            self.assertEqual(func(s=s, t=t), False)

if __name__ == "__main__":
    unittest.main()
