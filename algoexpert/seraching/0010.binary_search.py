
# Binary Search
# ---------------

# Problem Statement
# Write a function that takes in a sorted array of integers as well as a target integer. 
# The function should use the Binary Search algorithm to find if the target number is contained in the array 
# and should return its index if it is, otherwise -1.

# Sample input: [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33

# Sample output: 3


# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 

# METHOD 1: RECURSIVE METHOD
# O(log(n)) Time | O(log(n)) Space
def binarySearch(arrary, target):
    return binarySearchHelper(arrary, target, 0, len(arrary) -1)

def binarySearchHelper(arrary, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = arrary[middle]

    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(arrary, target, left, middle -1)
    else:
        return binarySearchHelper(arrary, target, middle +1, right)

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 

# METHOD 2: ITERATIVE METHOD
# O(log(n)) Time | O(1) Space
def binarySearch_i(arrary, target):
    left = 0
    right = len(arrary) - 1

    while left <= right:
        middle = (left + right) // 2
        potentialMatch = arrary[middle]

        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1



arrary = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print(binarySearch(arrary, target))
print(binarySearch_i(arrary, target))