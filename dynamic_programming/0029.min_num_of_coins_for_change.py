def minNoOfCoinsForChange(n, denoms):
    numsOfCoins = [float("inf") for amount in range(n+1)]
    numsOfCoins[0] = 0 
    for denom in denoms:
        for amount in range(n+1):
            if denom <= amount:
                numsOfCoins[amount] = min(numsOfCoins[amount], 1+ numsOfCoins[amount - denom])

    return numsOfCoins[n] if numsOfCoins[n] != float("inf") else -1

n = 7
denoms = [3,5]
print(minNoOfCoinsForChange(n, denoms))