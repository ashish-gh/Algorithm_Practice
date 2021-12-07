#Problem Statement
#-----------------

# Write a function that takes an n x m two-dimensional array(that can be square-shaped when n == n)
# returns one-dimensional arary of all the array'e elements in spiral order.

# Sample Input 
    # array = [
    #    [1,2,3,4],
    #    [12,13,14,5],
    #    [11,16,15,6],
    #    [10,9,8,7]
    # ]

# Sample Output: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# METHOD 1: ITERATIVE
# O(n) time | O(n) space
def spiralTravrsal(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1
    while startRow <= endRow and startCol <= endCol:

        for col in range(startCol, endCol +1):
            result.append(array[startRow][col])
        
        for row in range(startRow + 1, endRow + 1):
           result.append(array[row][endCol])
        
        for col in reversed(range(startCol, endCol)):
           result.append(array[endRow][col])
        
        for row in reversed(range(startRow +1, endRow)):
           result.append(array[row][startCol])

        startRow +=1
        endRow -= 1
        startCol +=1
        endCol -=1
    return result

array = [
    [1,2,3,4],
    [12,13,14,5],
    [11,16,15,6],
    [10,9,8,7]
]

print(spiralTravrsal(array))

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# METHOD 2: RECURSIVE

def spiralTravrsal_1(array):
    result = []
    spiralFill(array, 0, len(array)-1, 0, len(array[0])-1, result)
    return result

def spiralFill(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return
    
    for col in range(startCol, endCol +1):
        result.append(array[startRow][col])
    
    for row in range(startRow +1, endRow+1):
        result.append(array[row][endCol])
    
    for col in reversed(range(startCol, endCol)):
        result.append(array[endRow][col])
    
    for row in reversed(range(startRow +1, endRow)):
        result.append(array[row][startCol])
    
    spiralFill(array, startRow +1, endRow -1, startCol +1, endCol -1, result)

print(spiralTravrsal_1(array))

