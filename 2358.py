"""
2358. Maximum Number of Groups Entering a Competition
You are given a positive integer array grades which represents the grades of students in a university. You would like to enter all these students into a competition in ordered non-empty groups, such that the ordering meets the following conditions:
- The sum of the grades of students in the i-th group is less than the sum of the grades of students in the (i + 1)-th group, for all groups (except the last).
- The total number of students in the i-th group is less than the total number of students in the (i + 1)-th group, for all groups (except the last).

Return the maximum number of groups that can be formed.

Example1:
Input: grades = [10,6,12,7,3,5]
Output: 3
Explanation: The following is a possible way to form 3 groups of students:
- 1st group has the students with grades = [12]. Sum of grades: 12. Student count: 1
- 2nd group has the students with grades = [6,7]. Sum of grades: 6 + 7 = 13. Student count: 2
- 3rd group has the students with grades = [10,3,5]. Sum of grades: 10 + 3 + 5 = 18. Student count: 3
It can be shown that it is not possible to form more than 3 groups.

Example2:
Input: grades = [8,8]
Output: 1
Explanation: We can only form 1 group, since forming 2 groups would lead to an equal number of students in both groups.

Constraints:
1 <= grades.length <= 10^5
1 <= grades[i] <= 10^5
"""

"""
Note:
1. Solve equation by binary search: O(log(sqrt(2*n))) time | O(1) space
2. Solve equation by formula: O(1) time | O(1) space
"""
from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        # find x, satisfies x*(x+1) = n*2
        left, right = 1, int((2*n)**0.5)+1
        while left < right:
            mid = left + (right - left) // 2
            res = mid * (mid+1)
            if res < n*2:
                left = mid + 1
            elif res == n*2:
                return mid
            else:
                right = mid
        return left - 1

    def maximumGroups2(self, grades: List[int]) -> int:
        n = len(grades)
        # find x, satisfies x**2+x-2n = 0 (A=1,B=1,C=-2n)
        return int((-1+(1-4*1*(-2 * n))**0.5) // 2)

# Unit Tests
import unittest
funcs = [Solution().maximumGroups, Solution().maximumGroups2]

class TestMaximumGroups(unittest.TestCase):
    def testMaximumGroups1(self):
        for func in funcs:
            grades = [10,6,12,7,3,5]
            self.assertEqual(func(grades=grades), 3)

    def testMaximumGroups2(self):
        for func in funcs:
            grades = [8,8]
            self.assertEqual(func(grades=grades), 1)

if __name__ == "__main__":
    unittest.main()