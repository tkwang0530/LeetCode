"""
1105. Filling Bookcase Shelves.
description: https://leetcode.com/problems/filling-bookcase-shelves/description/
"""

"""
Note:
1. dfs + memo: O(nw) time | O(nw) space - where n is the length of books and w is shelfWidth

2. dfs + memo: O(nw) time | O(n) space - where n is the length of books

3. DP: O(nw) time | O(n) space - where n is the length of books
"""

from typing import List
import functools
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        memo = {}
        def dfs(i, space, currentHeight):
            if i >= len(books):
                return currentHeight
            if (i, space) in memo:
                return memo[(i, space)]
            
            # put current book on the next level of shelf
            minHeight = currentHeight + dfs(i+1, shelfWidth - books[i][0], books[i][1])
            # if the book could be put on this level, try to put it
            if books[i][0] <= space:
                minHeight = min(minHeight, dfs(i+1, space - books[i][0], max(currentHeight, books[i][1])))
            
            memo[(i, space)] = minHeight
            return memo[(i, space)]
        
        return dfs(0, shelfWidth, 0)

class Solution2:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return 0
            
            currentWidth = 0
            currentHeight = 0
            minHeight = float("inf")
            for j in range(i, n):
                currentWidth += books[j][0]
                if currentWidth > shelfWidth:
                    break
                currentHeight = max(currentHeight, books[j][1])
                minHeight = min(minHeight, currentHeight+dfs(j+1))
            return minHeight

        return dfs(0)

class Solution3:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            currentWidth = 0
            currentHeight = 0
            result = float("inf")
            
            for j in range(i, n):
                currentWidth += books[j][0]
                if currentWidth > shelfWidth:
                    break
                currentHeight = max(currentHeight, books[j][1])
                result = min(result, currentHeight+dp[j+1])
            dp[i] = result
        return dp[0]

# Unit Tests
import unittest
funcs = [Solution().minHeightShelves, Solution2().minHeightShelves, Solution3().minHeightShelves]

class TestMinHeightShelves(unittest.TestCase):
    def testMinHeightShelves1(self):
        for func in funcs:
            books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
            shelf_width = 4
            self.assertEqual(func(books=books, shelfWidth=shelf_width), 6)

    def testMinHeightShelves2(self):
        for func in funcs:
            books = [[1,3],[2,4],[3,2]]
            shelfWidth = 6
            self.assertEqual(func(books=books, shelfWidth=shelfWidth), 4)

if __name__ == "__main__":
    unittest.main()