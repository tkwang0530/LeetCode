"""
1395. Count Number of Teams
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example3:
Input: rating = [1,2,3,4]
Output: 4

Constraints:
n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 10^5
All the integers in rating are unique
"""

"""
Note:
1. One SortedList: O(n^2) time | O(n) space - where n is the length of rating
2. Two SortedLists: O(nlogn) time | O(n) space - where n is the length of rating
"""
from typing import List

from sortedcontainers import SortedList
class Solution(object):
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        smaller = SortedList()
        smallers = [0] * n
        for i in range(n-1, -1, -1):
            rate = rating[i]
            smallerCount = smaller.bisect_right(rate)
            smallers[i] = smallerCount
            smaller.add(rate)
        
        total = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                if rating[i] < rating[j]:
                    total += n-(j+1)-smallers[j]
                else:
                    total += smallers[j]
        return total

    def numTeams2(self, rating: List[int]) -> int:
        n = len(rating)
        rightSmaller = SortedList()
        leftSmaller = SortedList()
        rightSmallers = [0] * n
        leftSmallers = [0] * n
        for i in range(n-1, -1, -1):
            rate = rating[i]
            smallerCount = rightSmaller.bisect_right(rate)
            rightSmallers[i] = smallerCount
            rightSmaller.add(rate)

        for i in range(n):
            rate = rating[i]
            smallerCount = leftSmaller.bisect_right(rate)
            leftSmallers[i] = smallerCount
            leftSmaller.add(rate)
        
        total = 0
        for j in range(1, n-1):
            rightGreater = n-(j+1)-rightSmallers[j]
            leftGreater = j - leftSmallers[j]

            total += leftSmallers[j] * rightGreater
            total += leftGreater * rightSmallers[j]
        return total

# Unit Tests
import unittest
funcs = [Solution().numTeams, Solution().numTeams2]

class TestNumTeams(unittest.TestCase):
    def testNumTeams1(self):
        for func in funcs:
            rating = [2,5,3,4,1]
            self.assertEqual(func(rating=rating), 3)

    def testNumTeams2(self):
        for func in funcs:
            rating = [2,1,3]
            self.assertEqual(func(rating=rating), 0)

    def testNumTeams3(self):
        for func in funcs:
            rating = [1,2,3,4]
            self.assertEqual(func(rating=rating), 4)

if __name__ == "__main__":
    unittest.main()
