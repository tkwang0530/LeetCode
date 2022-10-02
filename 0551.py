"""
551. Student Attendance Record I
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

Example1:
Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

Example2:
Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

Constraints:
1 <= s.length <= 1000
s[i] is either 'A', 'L', or 'P'.
"""

"""
Note:
1. Brute-Force: O(n) time | O(1) space - where n is the length of string s
"""




import unittest
class Solution:
    def checkRecord(self, s: str) -> bool:
        absents = 0
        lates = 0
        prev = "$"
        for char in s:
            if char == "L" and prev != "L":
                lates = 1
            elif char == "L":
                lates += 1
            elif char == "A":
                absents += 1

            if absents == 2 or lates == 3:
                return False

            prev = char
        return True


# Unit Tests
funcs = [Solution().checkRecord]


class TestCheckRecord(unittest.TestCase):
    def testCheckRecord1(self):
        for func in funcs:
            s = "PPALLP"
            self.assertEqual(func(s=s), True)

    def testCheckRecord2(self):
        for func in funcs:
            s = "PPALLL"
            self.assertEqual(func(s=s), False)


if __name__ == "__main__":
    unittest.main()
