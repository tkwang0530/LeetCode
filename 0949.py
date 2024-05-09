
"""
949. Largest Time for Given Digits
description: https://leetcode.com/problems/largest-time-for-given-digits/description/
"""

"""
Note:
1. Permutation: O(24) time | O(24) space
"""

from typing import List
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort()
        n = len(arr)
        def permutation() -> List[str]:
            output = []
            def dfs(i):
                if i == n:
                    output.append("".join([str(num) for num in arr]))
                for j in range(i, n):
                    if j > i and arr[j]==arr[j-1]:
                        continue
                    arr[i], arr[j] = arr[j], arr[i]
                    dfs(i+1)
                    arr[i], arr[j] = arr[j], arr[i]
            dfs(0)
            return output
        
        largestMinutes = 0
        latest = ""
        for candidate in permutation():
            hours, minutes = int(candidate[0:2]), int(candidate[2:])
            if not (0 <= hours <= 23) or not (0 <= minutes <= 59):
                continue
            currentMinutes = 60 * hours + minutes
            if largestMinutes <= currentMinutes:
                largestMinutes = currentMinutes
                strHours = ("0" if hours < 10 else "") + str(hours)
                strMinutes = ("0" if minutes < 10 else "") + str(minutes)
                latest = strHours+":"+strMinutes
        return latest
# Unit Tests
import unittest
funcs = [Solution().largestTimeFromDigits]

class TestLargestTimeFromDigits(unittest.TestCase):
    def testLargestTimeFromDigits1(self):
        for largestTimeFromDigits in funcs:
            arr = [1,2,3,4]
            self.assertEqual(largestTimeFromDigits(arr=arr), "23:41")

    def testLargestTimeFromDigits2(self):
        for LargestTimeFromDigits in funcs:
            arr = [5,5,5,5]
            self.assertEqual(LargestTimeFromDigits(arr=arr), "")

if __name__ == "__main__":
    unittest.main()