"""
1471. The k Strongest Values in an Array
Given an array of integers arr and an integer k.

A value arr[i] is said to be stronger than a value arr[j] if |arr[i] - m| > |arr[j] - m| where m is the median of the array.
if |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than arr[j] if arr[i] > arr[j].

Return a list of strongest k values in the array. Return the answer in any arbitrary order.

Example1:
Input: arr = [1,2,3,4,5], k = 2
Output: [5,1]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also accepted answer.
Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5 > 1.

Example2:
Input: arr = [1,1,3,5,5], k = 2
Output: [5,5]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,5,1,1,3]. The strongest 2 elements are [5, 5].

Example3:
Input: arr = [6,7,11,7,6,8], k = 5
Output: [11,8,6,6,7]
Explanation: Median is 7, the elements of the array sorted by the strongest are [11,8,6,6,7,7].
Any permutation of [11,8,6,6,7] is accepted.

Constraints:
1 <= arr.length <= 10^5
-10^5 <= arr[i] <= 10^5
1 <= k <= arr.length
"""

"""
Note:
1. minHeap: O(nlogn+nlogk) time | O(k) space
2. sort + slice: O(nlogn+nlogn) time | O(n+k) space
3. sort + Two Pointers: O(nlogn+k) time | O(k) space
"""
import heapq
from typing import List
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        if n == 0:
            return []
        m = arr[(n-1)//2]
        minHeap = []
        for num in arr:
            if len(minHeap) < k:
                heapq.heappush(minHeap, (abs(num-m), num))
            else:
                heapq.heappushpop(minHeap, (abs(num-m), num))
        return [num for _, num in minHeap]

    def getStrongest2(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        if n == 0:
            return []
        m = arr[(n-1)//2]
        compares = [(abs(num-m), num) for num in arr]
        compares.sort(reverse=True)
        return [num for _, num in compares[:k]]

    def getStrongest3(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n-1)//2]
        i, j = 0, n-1
        output = []
        while len(output) < k:
            left, right = arr[i], arr[j]
            leftScore, rightScore = abs(left - m), abs(right - m)
            if leftScore > rightScore:
                output.append(left)
                i += 1
            else:
                output.append(right)
                j -= 1
        return output

# Unit Tests
import unittest
funcs = [Solution().getStrongest, Solution().getStrongest2, Solution().getStrongest3]
class TestGetStrongest(unittest.TestCase):
    def testGetStrongest1(self):
        for func in funcs:
            arr = [1,2,3,4,5]
            k = 2
            self.assertEqual(sorted(func(arr=arr, k=k)), sorted([5,1]))

    def testGetStrongest2(self):
        for func in funcs:
            arr = [1,1,3,5,5]
            k = 2
            self.assertEqual(sorted(func(arr=arr, k=k)), sorted([5,5]))

    def testGetStrongest3(self):
        for func in funcs:
            arr = [-7,22,17,3]
            k = 2
            self.assertEqual(sorted(func(arr=arr, k=k)), sorted([22, 17]))


if __name__ == "__main__":
    unittest.main()
