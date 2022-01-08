"""
690. Employee Importance
You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.

Example1:
Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.

Example2:
Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
Output: -3
Explanation: Employee 5 has an importance value of -3 and has no direct subordinates.
Thus, the total importance value of employee 5 is -3.

Constraints:
1 <= employees.length <= 2000
1 <= employees[i].id <= 2000
All employees[i].id are unique.
-100 <= employees[i].importance <= 100
One employee has at most one direct leader and may have several subordinates.
The IDs in employees[i].subordinates are valid IDs.
"""

""" 
1. Bottom-Up dfs: O(n) time | O(n) space - where n is the number of employees
"""

from typing import List
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        idEmployeeDict = {}
        for employee in employees:
            idEmployeeDict[employee.id] = employee
        
        
        def getImportanceByEmployeeId(id):
            employee = idEmployeeDict[id]
            total = employee.importance
            for subEmpId in employee.subordinates:
                total += getImportanceByEmployeeId(subEmpId)
            return total

        return getImportanceByEmployeeId(id)


# Unit Tests
import unittest
funcs = [Solution().getImportance]

class TestGetImportance(unittest.TestCase):
    def testGetImportance1(self):
        for func in funcs:
            employees = [Employee(1, 5, [2, 3]),Employee(2,3,[]), Employee(3,3,[])]
            id = 1
            self.assertEqual(func(employees=employees, id=id), 11)

    def testGetImportance2(self):
        for func in funcs:
            employees = [Employee(1, 2, [5]),Employee(5,-3,[])]
            id = 5
            self.assertEqual(func(employees=employees, id=id), -3)

if __name__ == "__main__":
    unittest.main()
