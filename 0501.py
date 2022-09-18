"""
501. Find Mode in Binary Search Tree
Given the root of a binary search tree (BST) with duplicates, return all mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.

Example1:   
Input: root = [1,null,2,2]
Output: [2]

Example2:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

"""
Note:
1. Recursive DFS (Preorder Traversal): O(n) time | O(n) space - where n is the number of nodes in the tree
"""




from typing import List, Optional
import collections
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        valCount = collections.defaultdict(int)

        def dfs(root, valCount):
            if not root:
                return
            valCount[root.val] += 1
            dfs(root.left, valCount)
            dfs(root.right, valCount)

        dfs(root, valCount)
        maxCount = max(valCount.values())
        output = []
        for val, count in valCount.items():
            if count == maxCount:
                output.append(val)
        return output

    def findMode2(self, root: Optional[TreeNode]) -> List[int]:
        maxCount = 0
        current = root
        largestVals = []
        container = [float("-inf"), 0]

        def handleValue(val: int, largestVals: List[int], container: List[int]):
            nonlocal maxCount
            if container[0] == val:
                container[1] += 1
            else:
                container[0] = val
                container[1] = 1

            if container[1] > maxCount:
                maxCount = container[1]
                largestVals.clear()
                largestVals.append(val)
            elif container[1] == maxCount:
                largestVals.append(val)

        while current:
            if not current.left:
                handleValue(current.val, largestVals, container)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right != current and predecessor.right:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    handleValue(current.val, largestVals, container)
                    current = current.right

        return largestVals


# Unit Tests
funcs = [Solution().findMode, Solution().findMode2]


class TestFindMode(unittest.TestCase):
    def testFindMode1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(2)))
            self.assertEqual(func(root=root), [2])

    def testFindMode2(self):
        for func in funcs:
            root = TreeNode(0)
            self.assertEqual(func(root=root), [0])


if __name__ == "__main__":
    unittest.main()
