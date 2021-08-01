"""
1570. Dot Product of Two Sparse Vectors
Given two sparse vectors, compute their dot product.

Implement class SparseVector:
- SparseVector(nums) Initializes the object with the vector nums
- dotProduct(vec) Compute the doct product between the instance of SparseVector and vec

A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example1:
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Example2:
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Example3:
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6

Constraints:
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100
"""

"""
Note:
1. HashMap: O(n) time | O(n) space
"""




import unittest
from typing import List
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonZero = {}
        for idx, val in enumerate(nums):
            if val != 0:
                self.nonZero[idx] = val
    
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for key, val in self.nonZero.items():
            if key in vec.nonZero:
                result += val * vec.nonZero[key]
        return result



# Unit Tests

class TestSparseVector(unittest.TestCase):
    def testSparseVector1(self):
        nums1 = [1,0,0,2,3]
        nums2 = [0,3,0,4,0]
        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        self.assertEqual(v1.dotProduct(v2), 8)

    def testSparseVector2(self):
        nums1 = [0,1,0,0,0]
        nums2 = [0,0,0,0,2]
        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        self.assertEqual(v1.dotProduct(v2), 0)

    def testSparseVector3(self):
        nums1 = [0,1,0,0,2,0,0]
        nums2 = [1,0,0,0,3,0,4]
        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        self.assertEqual(v1.dotProduct(v2), 6)


if __name__ == "__main__":
    unittest.main()
