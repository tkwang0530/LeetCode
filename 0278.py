"""
278. First Bad Version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example2:
Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 2^31 - 1
"""

"""
Note:
1. Binary Search: O(logn) time | O(1) space
"""

import unittest

def isBadVersion(version: int) -> bool:
        if version >= 4:
            return True
        else:
            return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n + 1
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left



# Unit Tests
funcs = [Solution().firstBadVersion]

class TestFirstBadVersion(unittest.TestCase):
    def testFirstBadVersion1(self):
        for func in funcs:
            self.assertEqual(
                func(n=5), 4)


if __name__ == "__main__":
    unittest.main()
