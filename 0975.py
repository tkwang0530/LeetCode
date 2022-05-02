"""
975. Odd Even Jump
You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:
- During odd-numbered jumps, you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
- During even-numbered jumps, you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
- It may be the case that for some index i, there are no legal jumps.

A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.

Example1:
Input: arr = [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
From starting index i = 4, we have reached the end already.
In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
jumps.

Example2:
Input: arr = [2,3,1,1,4]
Output: 3
Explanation: 
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal to arr[0].
During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2] is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3
During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3] is the smallest value in [arr[3], arr[4]] that is greater than or equal to arr[2].
We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
number of jumps.

Example3:
Input: arr = [5,1,3,4,2]
Output: 3
Explanation: We can reach the end from starting indices 1, 2, and 4.

Constraints:
1 <= arr.length <= 2 * 10^4
0 <= arr[i] < 10^5
"""

"""
Note:
1. SortedList + DP: O(nlogn) time | O(n) space - where n is the length of arr
2. Monotonic increasing stack + DP: O(n) time | O(n) space - where n is the length of arr
"""
from typing import List

from sortedcontainers import SortedList
class Solution(object):
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        smaller = SortedList()
        bigger = SortedList()

        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True

        for i in range(n-1, -1, -1):
            # bigger
            idx = bigger.bisect_right((arr[i], i))
            if idx < len(bigger):
                odd[i] = even[bigger[idx][1]]
            bigger.add((arr[i], i))

            # smaller
            idx = smaller.bisect_right((-arr[i], i))
            if idx < len(smaller):
                even[i] = odd[smaller[idx][1]]
            smaller.add((-arr[i], i))
        return sum(odd)

    def oddEvenJumps2(self, arr: List[int]) -> int:
        n = len(arr)
        bigger = [-1] * n
        stack = []
        sortedArr = sorted((arr[i], i) for i in range(n))

        # e.g. [(10, 0), (12, 2), (13, 1), (14, 3), (15, 4)]
        for _, i in sortedArr:
            while stack and stack[-1] < i:
                bigger[stack.pop()] = i
            stack.append(i)

        smaller = [-1] * n
        stack = []
        sortedArr = sorted((-arr[i], i) for i in range(n))
        for _, i in sortedArr:
            while stack and stack[-1] < i:
                smaller[stack.pop()] = i
            stack.append(i)
        
        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True
        for i in range(n-1, -1, -1):
            # bigger
            idx = bigger[i]
            if idx >= 0:
                odd[i] = even[idx]
            
            # smaller
            idx = smaller[i]
            if idx >= 0:
                even[i] = odd[idx]
        return sum(odd)

# Unit Tests
import unittest
funcs = [Solution().oddEvenJumps, Solution().oddEvenJumps2]

class TestOddEvenJumps(unittest.TestCase):
    def testOddEvenJumps1(self):
        for func in funcs:
            arr = [10,13,12,14,15]
            self.assertEqual(func(arr=arr), 2)

    def testOddEvenJumps2(self):
        for func in funcs:
            arr = [2,3,1,1,4]
            self.assertEqual(func(arr=arr), 3)

    def testOddEvenJumps3(self):
        for func in funcs:
            arr = [5,1,3,4,2]
            self.assertEqual(func(arr=arr), 3)

if __name__ == "__main__":
    unittest.main()
