"""
1105. Filling Bookcase Shelves.
You are given an array books where books[i] = [thickness_i, height_i] indicates the thickness and height of the i-th book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.
- For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Example1:
Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.

Example2:
Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4

Constraints:
1 <= books.length <= 1000
1 <= thickness_i <= shelfWidth <= 1000
1 <= height_i <= 1000
"""

"""
Note:
1. dfs + memo: O(nw) time | O(nw) space - where n is the length of books and w is shelfWidth

2. dfs + memo: O(nw) time | O(n) space - where n is the length of books

3. DP: O(nw) time | O(n) space - where n is the length of books
"""

from typing import List
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

    def minHeightShelves2(self, books: List[List[int]], shelfWidth: int) -> int:
        memo = {}
        def dfs(i):
            if i == len(books):
                return 0
            
            if i in memo:
                return memo[i]
            
            currentWidth = 0
            currentHeight = 0
            result = float("inf")

            for j in range(i, len(books)):
                currentWidth += books[j][0]
                if currentWidth > shelfWidth:
                    break
                currentHeight = max(currentHeight, books[j][1])
                result = min(result, currentHeight+dfs(j+1))
            
            memo[i] = result
            return memo[i]
        return dfs(0)

    def minHeightShelves3(self, books: List[List[int]], shelfWidth: int) -> int:
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
funcs = [Solution().minHeightShelves, Solution().minHeightShelves2, Solution().minHeightShelves3]

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