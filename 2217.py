"""
2217. Find Palindrome With Fixed Length
Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]-th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

Example1:
Input: queries = [1,2,3,4,5,90], intLength = 3
Output: [101,111,121,131,141,999]
Explanation:
The first few palindromes of length 3 are:
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
The 90th palindrome of length 3 is 999.

Example2:
Input: queries = [2,4,6], intLength = 4
Output: [1111,1331,1551]
Explanation:
The first six palindromes of length 4 are:
1001, 1111, 1221, 1331, 1441, and 1551.

Constraints:
1 <= queries.length <= 5 * 10^4
1 <= queries[i] <= 10^9
1 <= intLength <= 15
"""

"""
Note:
1. Convert to String: O(n) time | O(1) space - where n is the length of queries
"""


import unittest
from  typing import List
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def findFirstNumberStr(n):
            if n == 1:
                return "1"
            if n == 2:
                return "11"
            return "1" + (n-2) * "0" + "1"
        
        out = []
        for query in queries:
            
            isOdd = intLength % 2 == 1
            idx = intLength // 2 if not isOdd else intLength // 2 + 1
            initNum = int(findFirstNumberStr(intLength)[:idx])
            
            num = initNum + query - 1
            leng = len(str(initNum))
            if query > 9 * 10 ** (leng - 1):
                out.append(-1)
                continue
            if isOdd:
                left = str(num)[:-1]
                right = left[::-1]
                numStr = left + str(num)[-1] + right 
            else:
                numStr = str(num) + str(num)[::-1]
            out.append(int(numStr))
        return out


# Unit Tests

funcs = [Solution().kthPalindrome]


class TestLongestWPI(unittest.TestCase):
    def testLongestWPI1(self):
        for func in funcs:
            queries = [1,2,3,4,5,90]
            intLength = 3
            self.assertEqual(func(queries=queries, intLength=intLength), [101,111,121,131,141,999])

    def testLongestWPI2(self):
        for func in funcs:
            queries = [2,4,6]
            intLength = 4
            self.assertEqual(func(queries=queries, intLength=intLength), [1111,1331,1551])

if __name__ == "__main__":
    unittest.main()
