"""
2583. Kth Largest Sum in a Binary Tree
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

Example1:
Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.

Example2:
Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.

Constraints:
2 <= n <= 10^5
1 <= Node.val <= 10^6
1 <= k <= n
"""

"""
Note:
1. minHeap + Layer order traversal: O(n + hlogk) Time | O(n+k) space - where n is the number of node in the tree and h is the height of the tree
"""




import unittest
import heapq
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        currentArr = [root]
        minHeap = []

        while currentArr:
            nextArr = []
            currentLevelSum = sum([node.val for node in currentArr])

            if len(minHeap) == k:
                heapq.heappushpop(minHeap, currentLevelSum)
            else:
                heapq.heappush(minHeap, currentLevelSum)

            for node in currentArr:
                if node.left:
                    nextArr.append(node.left)
                if node.right:
                    nextArr.append(node.right)

            currentArr = nextArr
        return minHeap[0] if len(minHeap) == k else -1


# Unit Tests
funcs = [Solution().kthLargestLevelSum]


class TestKthLargestLevelSum(unittest.TestCase):
    def testKthLargestLevelSum1(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(
                6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7)))
            k = 2
            self.assertEqual(func(root=root, k=k), 13)

    def testKthLargestLevelSum2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(3)))
            k = 1
            self.assertEqual(func(root=root, k=k), 3)


if __name__ == "__main__":
    unittest.main()
