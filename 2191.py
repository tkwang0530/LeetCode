"""
2191. Sort the Jumbled Numbers
description: https://leetcode.com/problems/sort-the-jumbled-numbers/description/
"""

"""
Note:
1. Sort + HashMap: O(nlogn) time | O(10) space - where n is the length of nums
"""


from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        digitMap = {i: num for i, num in enumerate(mapping)}
        def convert(num):
            numStr = str(num)
            newNumChars = []
            for numChar in numStr:
                num = int(numChar)
                newNumChars.append(str(digitMap[num]))
            
            return int("".join(newNumChars))

        nums.sort(key=lambda x: convert(x))
        return nums

# Unit Tests
import unittest
funcs = [Solution().sortJumbled]

class TestSortJumbled(unittest.TestCase):
    def testSortJumbled1(self):
        for func in funcs:
            mapping = [8,9,4,0,2,1,3,5,7,6]
            nums = [991,338,38]
            self.assertEqual(func(mapping=mapping, nums=nums), [338, 38, 991])

    def testSortJumbled2(self):
        for func in funcs:
            mapping = [0,1,2,3,4,5,6,7,8,9]
            nums = [789,456,123]
            self.assertEqual(func(mapping=mapping, nums=nums), [123, 456, 789])


if __name__ == "__main__":
    unittest.main()
