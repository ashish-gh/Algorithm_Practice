# Problem Statement
# -----------------

# Write a function that takes in a non-empty array of integers and returns the maximum sum that
#  can be obtained by summing up all the numbers in a non-empty subarray of the input array. 
# A subarray must only contain adjacent numbers. 


# Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] 
# 
# Sample output: 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# O(n) time | O(1) space 
def kadanesAlgorithm(array):
    maxEndHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndHere = max(num, maxEndHere +num)
        maxSoFar = max(maxSoFar, maxEndHere)
    
    return maxSoFar

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] 
print(kadanesAlgorithm(array))


    
    