'''
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
Solved
Medium
Topics
Companies
Hint
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.
'''

def numberOfSubArrays(arr, k, threshold):
    end = k
    current_sum = sum(arr[:k])
    sub_arrays = 0
    while end < len(arr):
        if current_sum / k >= threshold:
            sub_arrays += 1
        current_sum += arr[end] - arr[end-k]
        end += 1
# to check the window which holds the last element of the array in the window        
    if current_sum / k >= threshold:
        sub_arrays += 1
    return sub_arrays

    