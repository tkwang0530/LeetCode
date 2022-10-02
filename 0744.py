"""
744. Find Smallest Letter Greater Than Target
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.
- For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

Example1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"

Example3:
Input: letters = ["c","f","j"], target = "d"
Output: "f"

Constraints:
2 <= letters.length <= 10^4
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""

"""
Note:
1. Binary Search: O(logn) time | O(1) space - where n is the length of array letters
"""




import unittest
import bisect
from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        idx = bisect.bisect_right(letters, target)
        return letters[idx]


# Unit Tests
funcs = [Solution().nextGreatestLetter]


class TestNextGreatestLetter(unittest.TestCase):
    def testNextGreatestLetter1(self):
        for func in funcs:
            letters = ["c", "f", "j"]
            target = "a"
            self.assertEqual(func(letters=letters, target=target), "c")

    def testNextGreatestLetter2(self):
        for func in funcs:
            letters = ["c", "f", "j"]
            target = "c"
            self.assertEqual(func(letters=letters, target=target), "f")


if __name__ == "__main__":
    unittest.main()
