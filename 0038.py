"""
38. Count and Say
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

- countAndSay(1) == "1"
- countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":
two 3's, three 2's, one 5. and one 1
23 + 32 + 15 + 11
"23321511"

Example1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Constraints:
1 <= n <= 30
"""

"""
Note:
1. one while loop: O(2^n) time | O(1) space
2. Nested while loop: O(2^n) time | O(1) space
3. Recursion: O(2^n) time | O(n) space
"""




import unittest
class Solution(object):
    def countAndSay(self, n: int) -> str:
        numberStr = "1"
        for _ in range(n-1):
            numberStr = self.say(numberStr)
        return numberStr

    def say(self, numberStr: str) -> str:
        previous, count, chars, idx = numberStr[0], 1, [], 1
        while idx < len(numberStr):
            current = numberStr[idx]
            if current == previous:
                count += 1
            else:
                chars.append(str(count) + previous)
                previous = current
                count = 1
            idx += 1
        chars.append(str(count) + previous)
        return "".join(chars)

    def countAndSay2(self, n: int) -> str:
        numberStr = "1"
        for _ in range(n-1):
            numberStr = self.say2(numberStr)
        return numberStr

    def say2(self, numberStr: str) -> str:
        idx, chars = 0, []
        while idx < len(numberStr):
            count = 1
            while idx + 1 < len(numberStr) and numberStr[idx+1] == numberStr[idx]:
                count += 1
                idx += 1
            chars.append(str(count) + numberStr[idx])
            idx += 1
        return "".join(chars)

    def countAndSay3(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.say(self.countAndSay3(n-1))


# Unit Tests
funcs = [Solution().countAndSay, Solution().countAndSay2, Solution().countAndSay3]


class TestCountAndSay(unittest.TestCase):
    def testCountAndSay1(self):
        for func in funcs:
            self.assertEqual(
                func(n=1), "1")

    def testCountAndSay2(self):
        for func in funcs:
            self.assertEqual(
                func(n=4), "1211")


if __name__ == "__main__":
    unittest.main()
