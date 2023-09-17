"""
894. All Possible Full Binary Trees
description: https://leetcode.com/problems/all-possible-full-binary-trees/description/
"""

""" 
1. Divide and conquer: O(2^n) time | O(2^n) space
"""

import functools
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # dfs returns the list of fbt with n nodes
        @functools.lru_cache(None)
        def dfs(n):
            if n == 0:
                return []
            elif n == 1:
                return [TreeNode(0)]
            
            output = []
            for leftCount in range(n): # 0 - (n-1)
                rightCount = n - 1 - leftCount
                leftRes = dfs(leftCount)
                rightRes = dfs(rightCount)

                for t1 in leftRes:
                    for t2 in rightRes:
                        output.append(TreeNode(0, t1, t2))
            return output

        return dfs(n)
