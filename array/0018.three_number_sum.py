# Problem Statement
# -----------------

# Write a function that takes in a non-empty array of distinct integers and an integer
#  representing a target sum. The function should nd all triplets in the array that sum 
# up to the target sum and return a two-dimensional array of all these triplets. 
# The numbers in each triplet should be ordered in ascending order, and the triplets 
# themselves should be ordered in ascending order with respect to the numbers they hold. 
# If no three numbers sum up to the target sum, the function should return an empty array.

# Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0

# Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]


# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# O(n^2) time | O(n) space
def threeNumberSum(array, target):
    array.sort()
    triplet = []
    for i in range(len(array) - 2):
        left = i +1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == target:
                triplet.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
    
    return triplet

array =[12,3,1,2,6,-6,5,-8]
target  = 0
print(threeNumberSum(array, target))
