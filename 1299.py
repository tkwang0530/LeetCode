"""
1299. Replace Elements with Greatest Element on Right Side
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1

After doing so, return the array.

Example1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""

"""
Note:
1. Track maxVal and traverse backward: O(n) time | O(1) space

"""

from typing import List
import unittest
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            arr[i], maxVal = maxVal, max(maxVal, arr[i])
        return arr


# Unit Tests
funcs = [Solution().replaceElements]


class TestReplaceElements(unittest.TestCase):
    def testReplaceElements1(self):
        for func in funcs:
            arr = [17,18,5,4,6,1]
            self.assertEqual(func(arr=arr), [18,6,6,6,1,-1])

    def testReplaceElements2(self):
        for func in funcs:
            arr = [400]
            self.assertEqual(func(arr=arr), [-1])

if __name__ == "__main__":
    unittest.main()
