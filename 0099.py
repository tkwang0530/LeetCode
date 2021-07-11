"""
99. Recover Binary Search Tree
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure

Followup: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

Example1:
            1                  3
          /                   /    
       3                  1     
         \                    \
           2                    2
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example2:
         3                  2
       /    \              /    \
    1       4          1       4
            /                    /
          2                    3      
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:
The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1
"""

"""
Note:
1. modified Morris traversal: O(n) time | O(1) space
for normal binary search tree  1, 2, 3, 4, 5
there are two main cases:
(1) swap happened on adjacent nodes => 1, 2, 4, 3, 5. In this case, we have only one oddity: 4 and 3 => candidates = [(4, 3)]
(2)swap happened on not adjacent nodes =>  1, 2, 5, 4, 3. In this case we have two oddities: 5 and 4; 4 and 3. => candidates = [(5, 4), (4, 3)]
But in both cases, it's okay to run candidates[0][0].val, candidates[-1][1].val = candidates[-1][1].val, candidates[0][0].val
"""




import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        current, previous, candidates = root, TreeNode(float("-inf")), []
        while current:
            if not current.left:
                if current.val < previous.val:
                    candidates.append((previous, current))
                previous = current
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right != current and predecessor.right is not None:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    if current.val < previous.val:
                        candidates.append((previous, current))
                    previous = current
                    current = current.right
        candidates[0][0].val, candidates[-1][1].val = candidates[-1][1].val, candidates[0][0].val


# Unit Tests
funcs = [Solution().recoverTree]


class TestRecoverTree(unittest.TestCase):
    def testRecoverTree1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
            func(root=root)
            self.assertEqual(root.val, 3)
            self.assertEqual(root.left.val, 1)
            self.assertEqual(root.right, None)
            self.assertEqual(root.left.left, None)
            self.assertEqual(root.left.right.val, 2)


if __name__ == "__main__":
    unittest.main()
