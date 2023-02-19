"""
1574. Shortest Subarray to be Removed to Make Array Sorted
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

Example1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.

Constraints:
1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
"""

"""
Note:
1. Two pointers: O(n) time | O(1) space - where n is the length of array arr

2. Binary Search: O(nlogn) time | O(1) space - where n is the length of array arr
"""




from  typing import List
import unittest
import bisect
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left < right and arr[left+1] >= arr[left]:
            left += 1

        if left == right:
            return 0

        while right > left and arr[right-1] <= arr[right]:
            right -= 1

        minRemove = min(n-(left+1), right)

        # merge left subarray and right subarray
        for i in range(left+1):
            if arr[i] <= arr[right]:
                minRemove = min(minRemove, right - (i+1))
            elif right < n-1:  # choose a larger right
                right += 1
            else:
                break
        return minRemove

    def findLengthOfShortestSubarray2(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left < right and arr[left+1] >= arr[left]:
            left += 1

        if left == right:
            return 0

        while right > left and arr[right-1] <= arr[right]:
            right -= 1

        minRemove = min(n-(left+1), right)

        for i in range(left+1):
            idx = bisect.bisect_left(arr, x=arr[i], lo=right)
            minRemove = min(minRemove, idx - (i + 1))
        return minRemove


# Unit Tests
funcs = [Solution().findLengthOfShortestSubarray,
         Solution().findLengthOfShortestSubarray2]


class TestFindLengthOfShortestSubarray(unittest.TestCase):
    def testFindLengthOfShortestSubarray1(self):
        for func in funcs:
            arr = [1, 2, 3, 10, 4, 2, 3, 5]
            self.assertEqual(func(arr=arr), 3)

    def testFindLengthOfShortestSubarray2(self):
        for func in funcs:
            arr = [5, 4, 3, 2, 1]
            self.assertEqual(func(arr=arr), 4)

    def testFindLengthOfShortestSubarray3(self):
        for func in funcs:
            arr = [1, 2, 3]
            self.assertEqual(func(arr=arr), 0)


if __name__ == "__main__":
    unittest.main()
