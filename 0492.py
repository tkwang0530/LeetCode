"""
492. Construct the Rectangle
A web developer needs to know how to design a web page's size. So, given a specific rectangular web page's area, your job by now is to design a rectangular web page, whose length L and with W satisfy the following requirements:
1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than then the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.

Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

Example1:
Input: area = 4
Output: [2,2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

Example2:
Input: area = 37
Output: [37,1]

Example3:
Input: area = 122122
Output: [427,286]

Constraints:
1 <= area <= 10^7
"""

"""
Note:
1. Brute-Force: O(sqrt(area)) time | O(1) space
"""




from typing import List
import unittest
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for n in range(int(area**0.5), 0, -1):
            if area % n == 0:
                return [area//n, n]


# Unit Tests
funcs = [Solution().constructRectangle]


class TestConstructRectangle(unittest.TestCase):
    def testConstructRectangle1(self):
        for func in funcs:
            area = 4
            self.assertEqual(func(area=area), [2, 2])

    def testConstructRectangle2(self):
        for func in funcs:
            area = 37
            self.assertEqual(func(area=area), [37, 1])

    def testConstructRectangle3(self):
        for func in funcs:
            area = 122122
            self.assertEqual(func(area=area), [427, 286])


if __name__ == "__main__":
    unittest.main()
