"""
2178. Maximum Split of Positive Even Integers
You are given an integer finalSum. Split it into a sum of maximum number of unique positive even integers.
- For example, given finalSum = 12, the following spilits are valid (unique positive even integers summing up to finalSum): (12), (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.

Return a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for finalSum, return an empty list.

You may return the integers in any order.

Example1:
Input: finalSum = 12
Output: [2,4,6]
Explanation: The following are valid splits: (12), (2 + 10), (2 + 4 + 6), and (4 + 8).
(2 + 4 + 6) has the maximum number of integers, which is 3. Thus, we return [2,4,6].
Note that [2,6,4], [6,2,4], etc. are also accepted.

Example2:
Input: finalSum = 7
Output: []
Explanation: There are no valid splits for the given finalSum.
Thus, we return an empty array.

Example3:
Input: finalSum = 28
Output: [6,8,2,12]
Explanation: The following are valid splits: (2 + 26), (6 + 8 + 2 + 12), and (4 + 24). 
(6 + 8 + 2 + 12) has the maximum number of integers, which is 4. Thus, we return [6,8,2,12].
Note that [10,2,4,12], [6,2,4,16], etc. are also accepted.

Constraints:
1 <= finalSum <= 10^10
"""

"""
Note:
1. Math: O(log(S)) time | O(log(S)) space - where S is the given integer finalSum
"""




import unittest
from typing import List
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        n = int((-1+(1 ^ 2+4*finalSum)**0.5)/2*1)
        result = [2*i for i in range(1, n+1)]
        currentSum = (2+2+(n-1)*2)*n // 2
        result[-1] += finalSum - currentSum
        return result


# Unit Tests
funcs = [Solution().maximumEvenSplit]


class TestMaximumEvenSplit(unittest.TestCase):
    def testMaximumEvenSplit1(self):
        for func in funcs:
            finalSum = 12
            self.assertEqual(func(finalSum=finalSum), [2, 4, 6])

    def testMaximumEvenSplit2(self):
        for func in funcs:
            finalSum = 7
            self.assertEqual(func(finalSum=finalSum), [])

    def testMaximumEvenSplit3(self):
        for func in funcs:
            finalSum = 28
            self.assertEqual(func(finalSum=finalSum), [2, 4, 6, 16])


if __name__ == "__main__":
    unittest.main()
