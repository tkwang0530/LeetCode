"""
1530. Number of Good Leaf Nodes Pairs
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Example1:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.


Example2:
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.

Example3:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Constraints:
The number of nodes in the tree is in the range [1, 2^10].
1 <= Node.val <= 100
1 <= distance <= 10
"""

"""
Note:
1. DFS (Bottom up): O(100n) time | O(n) space - where n is the number of nodes
"""

import unittest, collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        goodPairs = 0     
        def dfs(node):
            nonlocal goodPairs
            if not node:
                return {}
            if not node.left and not node.right:
                return {1:1}
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            sortedLeft = sorted(left.keys())
            sortedRight = sorted(right.keys())
            
            for l in sortedLeft:
                for r in sortedRight:
                    if l + r > distance:
                        break
                    goodPairs += left[l] * right[r]
            
            result = {key+1: left.get(key, 0) + right.get(key, 0) for key in range(1, distance) if left.get(key, 0) + right.get(key, 0) > 0}
                
            return result
        dfs(root)
        return goodPairs

# Unit Tests
funcs = [Solution().countPairs]

class TestCountPairs(unittest.TestCase):
    def testCountPairs1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
            distance = 3
            self.assertEqual(func(root=root, distance=distance), 1)

    def testCountPairs2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
            distance = 3
            self.assertEqual(func(root=root, distance=distance), 2)

    def testCountPairs3(self):
        for func in funcs:
            root = TreeNode(7, TreeNode(1, TreeNode(6), None), TreeNode(4, TreeNode(5), TreeNode(3, None, TreeNode(2))), )
            distance = 3
            self.assertEqual(func(root=root, distance=distance), 1)

if __name__ == "__main__":
    unittest.main()
