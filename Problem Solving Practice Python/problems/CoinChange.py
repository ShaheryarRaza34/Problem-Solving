import sys
def coinChange(coins:list, amount:int):
    
    memory = [sys.maxsize]*(amount+1)
    memory[0] = 0

    for number in range(1, amount+1):
        for coin in coins:
            if coin <= number and memory[number - coin] != sys.maxsize:
                memory[number] = min(memory[number], 1 + memory[number - coin])
    return -1 if memory[amount] == sys.maxsize else memory[amount]
    

