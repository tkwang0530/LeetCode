"""
2326. Spiral Matrix IV
You are given two integers m and n, which represent the dimensions of a matrix.
You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

Example1:
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

Example2:
Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.

Constraints:
1 <= m, n <= 10^5
1 <= m * n <= 10^5
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
"""

"""
Note:
1. Brute-Force: O(mn) time | O(mn) space
"""

from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    # TEST ONLY
    def __repr__(self):
        return f"{self.val}->{self.next}"

    @classmethod
    def fromArray(cls, arr):
        if arr is None:
            return None
        idx = 0
        length = len(arr)
        dummy = cls(0)
        current = dummy
        while idx < length:
            current.next = cls(arr[idx])
            current = current.next
            idx += 1
        return dummy.next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1] * n for _ in range(m)]
        current = head
        top, down, left, right = 0, m-1, 0, n-1
        while current:
            for col in range(left, right+1):
                if not current:
                    break
                mat[top][col] = current.val
                current = current.next
            
            if not current:
                break
                
            for row in range(top+1, down+1):
                if not current:
                    break
                mat[row][right] = current.val
                current = current.next
            
            if not current:
                break
                
            for col in reversed(range(left, right)):
                if not current:
                    break
                mat[down][col] = current.val
                current = current.next
                
            if not current:
                break
                
            for row in reversed(range(top+1, down)):
                if not current:
                    break
                mat[row][left] = current.val
                current = current.next

            top += 1
            down -= 1
            left += 1
            right -= 1
        return mat

# Unit Tests
import unittest
funcs = [Solution().spiralMatrix]
class TestSpiralMatrix(unittest.TestCase):
    def testSpiralMatrix1(self):
        for func in funcs:
            m = 3
            n = 5
            head = ListNode.fromArray([3,0,2,6,8,1,7,9,4,2,5,5,0])
            self.assertEqual(func(m=m, n=n, head=head), [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]])

    def testSpiralMatrix2(self):
        for func in funcs:
            m = 1
            n = 4
            head = ListNode.fromArray([0,1,2])
            self.assertEqual(func(m=m, n=n, head=head), [[0,1,2,-1]])

if __name__ == "__main__":
    unittest.main()
