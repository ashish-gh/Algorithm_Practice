#Problem Statement
#-----------------

# Write a function that takes an array of integers and returns an array of 
# length 2 representing the largest range of integers contained in an array.
# A range of number is defined as the set of numbers that comes right after the other number in the set of real integers. 

# Sample Input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

# Sample Output = [0, 7]


# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# O(n) time | O(n) space
def largestRange(array):
    bestRange = []
    nums = {}
    longestRange = 0
    for num in array:
        nums[num] = True
    
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        
        while left in nums:
            nums[left] = False 
            currentLength += 1 
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1 
            right += 1

        if currentLength > longestRange:
            longestRange = currentLength
            bestRange = [left +1, right -1]

    return bestRange


array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array)) 