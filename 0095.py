"""
95. Unique Binary Search Trees II
description: https://leetcode.com/problems/unique-binary-search-trees-ii/description/
"""

"""
Note:
1. Recursion (DFS - PostOrder Traversal)
"""

import functools
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @functools.lru_cache(None)
        def dfs(lowerBound, upperBound):
            if lowerBound > upperBound:
                return [None]

            output = []
            for rv in range(lowerBound, upperBound+1):
                for left in dfs(lowerBound, rv-1):
                    for right in dfs(rv+1, upperBound):
                        root = TreeNode(rv, left, right)
                        output.append(root)
            return output

        return dfs(1, n)
