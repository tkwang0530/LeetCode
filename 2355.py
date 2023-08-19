"""
2355. Maximum Number of Books You Can Take
description: https://leetcode.com/problems/maximum-number-of-books-you-can-take/description/
"""

"""
Note:
1. Monotonic stack: O(n) time | O(n) space
ref: https://leetcode.com/problems/maximum-number-of-books-you-can-take/solutions/2367084/python3-increasing-stack-only-record-sudden-changes/
image: https://assets.leetcode.com/users/images/71de04b5-8cdb-46b7-a4e3-80215f5124d3_1659404437.4989634.png
"""

from typing import List
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(books)):
            while stack and books[i] <= books[stack[-1][0]] + (i-stack[-1][0]):
                stack.pop()

            prevEnd, prevSum = stack[-1] if stack else [-1, 0]
            h = min(i-prevEnd, books[i])
            top, bottom = books[i], books[i] - h + 1
            currentSum = prevSum + (top+bottom)*h//2
            stack.append([i, currentSum])
            res = max(res, currentSum)
        return res

# Unit Tests
import unittest
funcs = [Solution().maximumBooks]
class TestMaximumBooks(unittest.TestCase):
    def testMaximumBooks1(self):
        for maximumBooks in funcs:
            books = [8,5,2,7,9]
            self.assertEqual(maximumBooks(books=books), 19)

    def testMaximumBooks2(self):
        for maximumBooks in funcs:
            books = [7,0,3,4,5]
            self.assertEqual(maximumBooks(books=books), 12)

    def testMaximumBooks3(self):
        for maximumBooks in funcs:
            books = [8,2,3,7,3,4,0,1,4,3]
            self.assertEqual(maximumBooks(books=books), 13)

if __name__ == "__main__":
    unittest.main()
