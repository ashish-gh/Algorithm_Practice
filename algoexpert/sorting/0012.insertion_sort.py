# Insetin Sort
# -----------

# Problem Statement
# Write a function that takes in an array of integers and returns a sorted version of that array. 
# Use the Insetin Sort algorithm to sort the array.

# Sample input: [8, 5, 2, 9, 5, 6, 3] 
# Sample output: [2, 3, 5, 5, 6, 8, 9]
# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 


# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -=1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
         
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7] 
print(insertionSort(array))