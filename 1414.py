"""
1414. Find the Minimum Number of Fibonacci Numbers Whose Sum is K
Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. The same Fibonacci number can be used multiple times.

The Fibonacci numbers are defined as:
F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 for n > 2.

Example1:
Input: k = 7
Output: 2 
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.

Example2:
Input: k = 10
Output: 2 
Explanation: For k = 10 we can use 2 + 8 = 10.

Example3:
Input: k = 19
Output: 3 
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.

Constraints:
1 <= k <= 10^9
"""

"""
Note:
1. Greedy + Binary Search: O(logk^2) time | O(logk) space
"""
import bisect
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibNums = [1, 1]
        while fibNums[-1] + fibNums[-2] <= k:
            fibNums.append(fibNums[-1] + fibNums[-2])
        
        count = 0
        index = len(fibNums)
        while k > 0:
            index = bisect.bisect_right(fibNums, k, 0, index) - 1
            k -= fibNums[index]
            count += 1
            
        return count


# Unit Tests
import unittest
funcs = [Solution().findMinFibonacciNumbers]


class TestFindMinFibonacciNumbers(unittest.TestCase):
    def testFindMinFibonacciNumbers1(self):
        for func in funcs:
            k = 7
            self.assertTrue(func(k=k), 2)

    def testFindMinFibonacciNumbers2(self):
        for func in funcs:
            k = 10
            self.assertTrue(func(k=k), 2)

    def testFindMinFibonacciNumbers3(self):
        for func in funcs:
            k = 19
            self.assertTrue(func(k=k), 3)

if __name__ == "__main__":
    unittest.main()
