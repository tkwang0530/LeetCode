"""
1361. Validate Binary Tree Nodes
description: https://leetcode.com/problems/validate-binary-tree-nodes/description/
"""

"""
Note:
1. BFS+HashTable: O(n) time | O(n) space
"""

import collections
from typing import List
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        childrenNodes = set(leftChild+rightChild)

        foundRoot = False
        for node in range(n):
            if node not in childrenNodes and not foundRoot:
                root = node
                foundRoot = True
            elif node not in childrenNodes:
                return False
        
        visited = set()
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            
            visited.add(node)
            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])
            
        return len(visited) == n

# Unit Tests
import unittest
funcs = [Solution().validateBinaryTreeNodes]

class TestValidBinaryTreeNodes(unittest.TestCase):
    def testValidBinaryTreeNodes1(self):
        for validBinaryTreeNodes in funcs:
            n = 4
            leftChild = [1,-1,3,-1]
            rightChild = [2,-1,-1,-1]
            self.assertEqual(validBinaryTreeNodes(n=n, leftChild=leftChild, rightChild=rightChild), True)

    def testValidBinaryTreeNodes2(self):
        for validBinaryTreeNodes in funcs:
            n = 4
            leftChild = [1,-1,3,-1]
            rightChild = [2,3,-1,-1]
            self.assertEqual(validBinaryTreeNodes(n=n, leftChild=leftChild, rightChild=rightChild), False)

    def testValidBinaryTreeNodes3(self):
        for validBinaryTreeNodes in funcs:
            n = 2
            leftChild = [1,0]
            rightChild = [-1,-1]
            self.assertEqual(validBinaryTreeNodes(n=n, leftChild=leftChild, rightChild=rightChild), False)

if __name__ == "__main__":
    unittest.main()