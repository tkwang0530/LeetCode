"""
1026. Maximum Difference Between Node and Ancestor
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = | a.val - b.val | and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Example1:
             8                                       
         /       \                            
       3          10                
    /     \            \
 1        6            14
        /     \           /
       4      7       13 
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example2:
        1
           \
            2
               \
                 0
               /
             3  
Input: root = [1,null,2,null,0,3]
Output: 3

Constraints:
The number of nodes in the tree is in the range [2, 5000]
0 <= Node.val <= 10^5
"""

"""
Note:
1. Recursive DFS (preorder): O(n) time | O(h) space
track the minVal and maxVal
result = [0] # [maxDiff]
dfs(node, minVal, maxVal, result)
2. Iterative DFS (preorder): O(n) time | O(h) space
"""


from typing import Optional, List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = [0] # [maxDiff]
        self.dfs(root, root.val, root.val, result)
        return result[0]
    def dfs(self, node: TreeNode, maxVal: int, minVal: int, result: List[int]):
        result[0] = max(result[0], abs(maxVal - node.val), abs(minVal - node.val))
        maxVal = max(maxVal, node.val)
        minVal = min(minVal, node.val)
        
        if node.left:
            self.dfs(node.left, maxVal, minVal, result)
        if node.right:
            self.dfs(node.right, maxVal, minVal, result)

    def maxAncestorDiff2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxDiff = 0
        stack = [(root, root.val, root.val)] # (node, maxVal, minVal)
        while len(stack) > 0:
            node, maxVal, minVal = stack.pop()
            maxDiff = max(maxDiff, abs(maxVal - node.val), abs(minVal - node.val))
            maxVal = max(maxVal, node.val)
            minVal = min(minVal, node.val)
            if node.right:
                stack.append((node.right, maxVal, minVal))
            if node.left:
                stack.append((node.left, maxVal, minVal))
        return maxDiff

# Unit Tests
funcs = [Solution().maxAncestorDiff, Solution().maxAncestorDiff2]


class TestMaxAncestorDiff(unittest.TestCase):
    def testMaxAncestorDiff1(self):
        for func in funcs:
            root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
            self.assertEqual(func(root=root), 7)

    def testMaxAncestorDiff2(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3))))
            self.assertEqual(func(root=root), 3)


if __name__ == "__main__":
    unittest.main()
