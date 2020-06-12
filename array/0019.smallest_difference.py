# Problem Statement
# -------------------

# Write a function that takes in two non-empty arrays of integers. 
# The function should nd the pair of numbers (one from the rst array, 
# one from the second array) whose absolute difference is closest to zero. 
# The function should return an array containing these two numbers, with the 
# number from the rst array in the rst position. Assume that there will only be 
# one pair of numbers with the smallest difference. 
# 
# 
# Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17] 
# Sample output: [28, 26]


# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# O(n log n) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    oneIdx = 0
    twoIdx = 0 
    smallestDiff = float("inf")
    currentNumberDiff = float("inf")
    smallestPair = []

    while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
        firstNum = arrayOne[oneIdx]
        secondNum = arrayTwo[twoIdx]
        if firstNum == secondNum:
            return [firstNum, secondNum]
        elif firstNum < secondNum:
            currentNumberDiff = secondNum - firstNum
            oneIdx += 1
        elif secondNum < firstNum:
            currentNumberDiff = firstNum - secondNum
            twoIdx += 1
        
        if smallestDiff > currentNumberDiff:
            smallestDiff = currentNumberDiff
            smallestPair =  [firstNum, secondNum]

    return smallestPair

print(smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]))
