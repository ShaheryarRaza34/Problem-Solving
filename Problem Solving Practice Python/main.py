from problems.CoinChange import coinChange
from problems.LIS import longestIncreasingSubsequence
from problems.LongestPalindromicSubsequence import longestPalindromeSubseq
from problems.LongestCommonSubsequence import longestCommonSubseq
from problems.FirstMissingPositive import firstMissingPositive
from problems.InsertIntoBST import insertIntoBST
from problems.MinimumTimeToCollectApples import minTime
from problems.BoatsToSavePeople import numRescueBoats
from problems.BestTimeToSellStockI import maxProfit
from problems.NumberOfSubarraysOfSizekandAverageLessThanOrEqualThreshold import numberOfSubArrays

print(coinChange([1,5,7,9,11], 16))
print(longestIncreasingSubsequence([3,2,6,4,5,1]))
print(longestPalindromeSubseq('cbbd'))
print(longestCommonSubseq('abcde', 'ace' ))
print(firstMissingPositive([1,2,0]))
print(insertIntoBST(None,2 ))
print(minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,True,True,False,True,True,False]))
print(numRescueBoats([3,2,2,1], 3))
print(maxProfit([7,1,5,3,6,4]))
print(numberOfSubArrays([2,2,2,2,5,5,5,8], 3, 4))