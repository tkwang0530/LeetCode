"""
929. Unique Email Addresses
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

if you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".

It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

Example1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example2:
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

Constraints:
1 <= emails.length <= 100
1 <= emails[i].length <= 100
email[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
"""

""" 
1. HashTable: O(nm) time | O(n+m) space - where n is the length of the emails and m is the longest emails[i]
"""


import unittest
from typing import List
class Solution(object):
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            localName, domainName = email.split("@")
            emailSet.add((self.getFinalLocalName(localName), domainName))
        return len(emailSet)
            
    def getFinalLocalName(self, localName: str) -> str:
        chars = []
        for char in localName:
            if char.isalpha():
                chars.append(char)
            elif char == "+":
                break
        return "".join(chars)


# Unit Tests
funcs = [Solution().numUniqueEmails]


class TestNumUniqueEmails(unittest.TestCase):
    def testNumUniqueEmails1(self):
        for func in funcs:
            emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
            self.assertEqual(func(emails=emails), 2)

    def testNumUniqueEmails2(self):
        for func in funcs:
            emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
            self.assertEqual(func(emails=emails), 3)

if __name__ == "__main__":
    unittest.main()
