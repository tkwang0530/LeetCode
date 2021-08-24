"""
1089. Duplicate Zeros
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 9
"""

"""
Note:
1. using list.insert: O(n^2) time | O(1) space
2. count zeros: O(n) time | O(1) space
(1) count total zeros numbers (zeroes)
(2) start from the back and adjust items to correct locations
(3) if the item is zero, we have to dynamically change the number of zeroes, and then duplicate it
"""




from typing import List
import unittest
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] != 0:
                i += 1
            else:
                arr.insert(i + 1, 0)
                i += 2
                arr.pop()
    
    def duplicateZeros2(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0


# Unit Tests
funcs = [Solution().duplicateZeros]


class TestDuplicateZeros(unittest.TestCase):
    def testDuplicateZeros1(self):
        for func in funcs:
            arr = [1,0,2,3,0,4,5,0]
            func(arr=arr)
            self.assertEqual(arr, [1,0,0,2,3,0,0,4])

    def testDuplicateZeros2(self):
        for func in funcs:
            arr = [1,2,3]
            func(arr=arr)
            self.assertEqual(arr, [1,2,3])

if __name__ == "__main__":
    unittest.main()
