"""
1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Example1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example2:
Input: arr = [1,2]
Output: false

Example3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

"""
Note:
1. HashTable: O(n) time | O(n) space
"""

import collections
from  typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        countSet = set()
        for count in counter.values():
            if count in countSet:
                return False
            countSet.add(count)
        return True

# Unit Tests
import unittest
funcs = [Solution().uniqueOccurrences]

class TestUniqueOccurrences(unittest.TestCase):
    def testUniqueOccurrences1(self):
        for func in funcs:
            arr = [1,2,2,1,1,3]
            self.assertEqual(func(arr=arr), True)

    def testUniqueOccurrences2(self):
        for func in funcs:
            arr = [1,2]
            self.assertEqual(func(arr=arr), False)

    def testUniqueOccurrences3(self):
        for func in funcs:
            arr = [-3,0,1,-3,1,1,1,-3,10,0]
            self.assertEqual(func(arr=arr), True)


if __name__ == "__main__":
    unittest.main()
