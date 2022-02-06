"""
769. Max Chunks To Make Sorted
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Example1:
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example2:
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Constraints:
n == arr.length
1 <= n <= 10
0 <= arr[i] < n
All the elements of arr are unique.
"""

"""
Note:
1. Greedy Algorithm: O(n) time | O(1) space - where n is the length of arr
Iterate the array, if the max(arr[0] - arr[i]) = i,
then we can split the array into two chunks at this index.

2. Monotonic increase stack: O(n) time | O(n) space - where n is the length of arr
"""

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        currentMax, total = -1, 0
        for i, num in enumerate(arr):
            currentMax = max(currentMax, num)
            total += 1 if currentMax == i else 0
        return total

    def maxChunksToSorted2(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            largest = num
            while stack and stack[-1] > num:
                largest = max(largest, stack.pop())
            stack.append(largest)
        
        return len(stack)

# Unit Tests
import unittest
funcs = [Solution().maxChunksToSorted, Solution().maxChunksToSorted2]


class TestMaxChunksToSorted(unittest.TestCase):
    def testMaxChunksToSorted1(self):
        for func in funcs:
            arr = [4,3,2,1,0]
            self.assertEqual(func(arr=arr), 1)

    def testMaxChunksToSorted2(self):
        for func in funcs:
            arr = [1,0,2,3,4]
            self.assertEqual(func(arr=arr), 4)

    def testMaxChunksToSorted3(self):
        for func in funcs:
            arr = [1, 0, 2, 4, 3]
            self.assertEqual(func(arr=arr), 3)
            
if __name__ == "__main__":
    unittest.main()