import sys
'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''
def coinChange(coins:list, amount:int):
    
    memory = [sys.maxsize]*(amount+1)
    memory[0] = 0

    for number in range(1, amount+1):
        for coin in coins:
            if coin <= number and memory[number - coin] != sys.maxsize:
                memory[number] = min(memory[number], 1 + memory[number - coin])
    return -1 if memory[amount] == sys.maxsize else memory[amount]
    

