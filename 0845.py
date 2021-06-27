"""
845. Longest Mountain in Array
You may recall that an array arr is a mountain array if and only if:
- arr.length >= 3
- There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that
    - arr[0] < arr[1] < ... < arr[i-1] < arr[i]
    - arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Example1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example2:
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^4

Follow up:
Can you solve it using only one pass?
Can you solve it in O(1) space?
"""

"""
Note:
1. find peak + expand: O(n) time | O(1) space
"""




import unittest
from  typing import List
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longestPeakLength = 0
        i = 1
        while i < len(arr) - 1:
            isPeak = arr[i-1] < arr[i] and arr[i] > arr[i+1]
            if not isPeak:
                i += 1
                continue
            leftIdx = i - 2
            while leftIdx >= 0 and arr[leftIdx] < arr[leftIdx + 1]:
                leftIdx -= 1
            rightIdx = i + 2
            while rightIdx < len(arr) and arr[rightIdx] < arr[rightIdx - 1]:
                rightIdx += 1

            currentPeakLength = rightIdx - leftIdx - 1
            longestPeakLength = max(longestPeakLength, currentPeakLength)
            i = rightIdx

        return longestPeakLength

# Unit Tests


funcs = [Solution().longestMountain]


class TestIsMonotonic(unittest.TestCase):
    def testLongestMountain1(self):
        for func in funcs:
            arr = [2, 1, 4, 7, 3, 2, 5]
            self.assertEqual(func(arr=arr), 5)

    def testLongestMountain2(self):
        for func in funcs:
            arr = [2, 2, 2]
            self.assertEqual(func(arr=arr), 0)

    def testLongestMountain3(self):
        for func in funcs:
            arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
            self.assertEqual(func(arr=arr), 11)


if __name__ == "__main__":
    unittest.main()
