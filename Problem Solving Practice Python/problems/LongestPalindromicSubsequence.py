
'''
516. Longest Palindromic Subsequence
Medium
Topics
Companies
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.

'''


def longestPalindromeSubseq(s:str) -> int:

    reverse  = s[::-1]
    memory = [[None for i in range((len(s)+1))]for j in range((len(s)+1))]
     
    for i in range(len(s)+1):
        for j in range(len(s)+1):
            if i == 0 or j == 0 :
                memory[i][j] = 0
            elif s[i-1] == reverse[j-1]:
                memory[i][j] = 1 + memory[i-1][j-1]
            else:
                memory[i][j] = max(memory[i-1][j], memory[i][j-1])
    return memory[-1][-1]
