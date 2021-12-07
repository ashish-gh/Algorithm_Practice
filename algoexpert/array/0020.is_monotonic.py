# Problem Statement
# -------------------

# Write a function that takes an array of integers and returns a boolean representation whether 
# an arary is monotonic. An array is said to to be monotonic if its elements from left to right 
# are entirely non-increasing or entirely non-decreasing

# Sample Input: [-1, -5, -10, -1100, -1100, -1102, -9001]

# Sample Output: True

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# O(n) time | O(1) space
def isMonotonic(array):
    isIncreasing = True
    isDecreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            isIncreasing = False
        
        if array[i] >  array[i-1]:
            isDecreasing = False
    
    return isDecreasing or isIncreasing

arr = [1,2,3,4,4,4,4,4,5,5,6,100,124]
print(isMonotonic(arr))