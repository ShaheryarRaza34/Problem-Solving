'''
Is Palindrome
Solved 
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = "".join(c.lower() for c in s if c.isalnum())
        

        first, second = 0, len(new_string)-1

        while first <= second:
            if new_string[first] == new_string[second]:
                first +=1 
                second -= 1
            else:
                return False
        return True
        