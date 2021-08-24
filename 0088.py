"""
88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9

Follow up: Can you come up with an algorithm that runs in O(m+n) time ?
"""

"""
Note:
1. Two Pointers + backward traverse: O(m+n) time | O(1) space
"""




from typing import List
import unittest
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx = m + n-1
        idx1 = m - 1
        idx2 = n - 1
        while idx1 >= 0 or idx2 >= 0:
            value1 = nums1[idx1] if idx1 >= 0 else float("-inf")
            value2 = nums2[idx2] if idx2 >= 0 else float("-inf")
            if value1 > value2:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            idx -= 1
        



# Unit Tests
funcs = [Solution().merge]


class TestMerge(unittest.TestCase):
    def testMerge1(self):
        for func in funcs:
            nums1 = [1,2,3,0,0,0]
            m = 3
            nums2 = [2,5,6]
            n = 3
            func(nums1=nums1, m=m, nums2=nums2, n=n)
            self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def testMerge2(self):
        for func in funcs:
            nums1 = [1]
            m = 1
            nums2 = []
            n = 0
            func(nums1=nums1, m=m, nums2=nums2, n=n)
            self.assertEqual(nums1, [1])

    def testMerge3(self):
        for func in funcs:
            nums1 = [0]
            m = 0
            nums2 = [1]
            n = 1
            func(nums1=nums1, m=m, nums2=nums2, n=n)
            self.assertEqual(nums1, [1])

if __name__ == "__main__":
    unittest.main()
