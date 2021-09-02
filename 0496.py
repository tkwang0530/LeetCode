"""
496. Next Greater Element I
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the "next greater element" of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

Constraints:
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 10^4
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.

Follow up: Could you find an O(nums1.length + nums2.length) Solution?
"""

"""
Notes:
1. Using Stack: O(n + m) time | O(m) space
(1) Prepare the nextGreaterElements Hash Table <num, nextGreaterElement> from traversing the nums2 backward
(2) during traversing, while the current value is larger than the value on the top of the stack (if exist), pop the top element out
(3) after that, add the key value pair to the Hash Table
(4) append the current index to the stack
"""
from typing import List
class Solution(object):
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] # store the indices
        nextGreaterElements = {} # <num, newGreaterElement>
        result = []

        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                stack.pop()
            nextGreaterElements[nums2[i]] = -1 if len(stack) == 0 else nums2[stack[-1]]
            stack.append(i)
        
        for num in nums1:
            result.append(nextGreaterElements[num])
        return result


# Unit Tests
import unittest
funcs = [Solution().nextGreaterElement]

class TestNextGreaterElement(unittest.TestCase):
    def testNextGreaterElement1(self):
        for func in funcs:
            nums1 = [4,1,2]
            nums2 = [1,3,4,2]
            self.assertEqual(func(nums1=nums1, nums2=nums2), [-1, 3, -1])

    def testNextGreaterElement2(self):
        for func in funcs:
            nums1 = [2,4]
            nums2 = [1,2,3,4]
            self.assertEqual(func(nums1=nums1, nums2=nums2), [3, -1])


if __name__ == "__main__":
    unittest.main()