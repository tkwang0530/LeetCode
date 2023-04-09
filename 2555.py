"""
2555. Maximize Win From Two Segments
There are some prizes on the X-axis. You are given an integer array prizePositions that is sorted in non-decreasing order, where prizePositions[i] is the position of the ith prize. There could be different prizes at the same position on the line. You are also given an integer k.

You are allowed to select two segments with integer endpoints. The length of each segment must be k. You will collect all prizes whose position falls within at least one of the two selected segments (including the endpoints of the segments). The two selected segments may intersect.

For example if k = 2, you can choose segments [1, 3] and [2, 4], and you will win any prize i that satisfies 1 <= prizePositions[i] <= 3 or 2 <= prizePositions[i] <= 4.
Return the maximum number of prizes you can win if you choose the two segments optimally.

Example1:
Input: prizePositions = [1,1,2,2,3,3,5], k = 2
Output: 7
Explanation: In this example, you can win all 7 prizes by selecting two segments [1, 3] and [3, 5].

Example2:
Input: prizePositions = [1,2,3,4], k = 0
Output: 2
Explanation: For this example, one choice for the segments is [3, 3] and [4, 4], and you will be able to get 2 prizes. 

Constraints:
1 <= prizePositions.length <= 10^5
1 <= prizePositions[i] <= 10^9
0 <= k <= 10^9
prizePositions is sorted in non-decreasing order.
"""

"""
Note:
1. SuffixMax + Binary Search: O(nlogn) time | O(n) space - where n is the length of array prizePositions
"""




import unittest
from typing import List
import bisect
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        def calculate(left, right):
            leftIdx = bisect.bisect_left(prizePositions, left)
            rightIdx = bisect.bisect_right(prizePositions, right)
            return rightIdx-leftIdx

        posSet = set()
        posArr = []
        for pos in prizePositions:
            if pos in posSet:
                continue
            posArr.append(pos)
            posSet.add(pos)

        n = len(posArr)
        suffixMax = [0] * n
        suffixMax[-1] = calculate(posArr[-1], posArr[-1]+k)
        for i in range(n-2, -1, -1):
            suffixMax[i] = max(
                suffixMax[i+1], calculate(posArr[i], posArr[i]+k))

        maxWin = 0
        for i in range(n):
            pos = posArr[i]
            nextIdx = bisect.bisect_left(posArr, pos+k+1)
            maxWin = max(
                maxWin,
                calculate(pos, pos+2*k),
                calculate(pos, pos+k) +
                (suffixMax[nextIdx] if nextIdx < n else 0)
            )
        return maxWin


# Unit Tests
funcs = [Solution().maximizeWin]


class TestMaximizeWin(unittest.TestCase):
    def testMaximizeWin1(self):
        for func in funcs:
            prizePositions = [1, 1, 2, 2, 3, 3, 5]
            k = 2
            self.assertEqual(func(prizePositions=prizePositions, k=k), 7)

    def testMaximizeWin2(self):
        for func in funcs:
            prizePositions = [1, 2, 3, 4]
            k = 0
            self.assertEqual(func(prizePositions=prizePositions, k=k), 2)


if __name__ == "__main__":
    unittest.main()
