'''
The task is to find the length of the longest subsequence in a given array of integers such that 
all elements of the subsequence are sorted in strictly ascending order.
'''



def longestIncreasingSubsequence(sequence):

    memory = [1]*(len(sequence))

    for i in range(1,len(sequence)):
        for j in range(i):
            if (sequence[j] < sequence[i]):
                memory[i] = max(memory[i], memory[j]+1)
    return max(memory)