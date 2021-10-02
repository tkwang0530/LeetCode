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

2. count up hill length and down hill length for every point: O(n) time | O(1) space
(1) take one forward pass to count up hill length (to every point).
(2) take another backward pass to count down hill length (from every point).
(3) a pass to find max(up[i] + down[i] + 1) where up[i] and down[i] should be positives.

3. count up hill length and down hill length for every point (one pass): O(n) time | O(1) space
(1) count up and down during the traversal
(2) reset up and down to zero when A[i-1] == A[i] or down > 0 and A[i-1] < A[i]
"""

from  typing import List
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        peakIdx = 1
        longestPeakLength = 0
        while peakIdx <= len(arr) - 2:
            isPeak = arr[peakIdx-1] < arr[peakIdx] and arr[peakIdx] > arr[peakIdx+1]
            if not isPeak:
                peakIdx += 1
                continue
            
            left, right = peakIdx - 1, peakIdx + 1
            while left-1 >= 0 and arr[left-1] < arr[left]:
                left -= 1
            while right+1 <= len(arr) - 1 and arr[right+1] < arr[right]:
                right += 1
            longestPeakLength = max(longestPeakLength, right - left + 1)
            peakIdx = right
        return longestPeakLength

    def longestMountain2(self, arr: List[int]) -> int:
        up, down = [0] * len(arr), [0] * len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]: up[i] = up[i-1] + 1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i+1]: down[i] = down[i+1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])

    def longestMountain3(self, arr: List[int]) -> int:
        longestPeakLength = up = down = 0
        for i in range(1, len(arr)):
            if down and arr[i-1] < arr[i] or arr[i-1] == arr[i]: up = down = 0
            up += arr[i-1] < arr[i]
            down += arr[i-1] > arr[i]
            if up and down:
                longestPeakLength = max(longestPeakLength, up+down+1)
        return longestPeakLength

# Unit Tests
import unittest
funcs = [Solution().longestMountain, Solution().longestMountain2, Solution().longestMountain3]


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
