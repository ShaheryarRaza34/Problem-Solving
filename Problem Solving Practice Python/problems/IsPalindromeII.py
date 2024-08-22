'''
680. Valid Palindrome II
Solved
Easy
Topics
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        first, second= 0, len(s) - 1
        def helper(arr):
            return arr == arr[::-1]

        while first < second:
            if s[first] != s[second]:
                return (helper(s[first+1: second+1]) or helper(s[first:second]))
            first, second = first+1, second-1
        return True
        