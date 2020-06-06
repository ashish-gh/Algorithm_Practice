#  ARRAY


# METHOD 1  : USING TWO OF FOR LOOP 
# SPACE TIME COMPLEXITY
# TIME COMPLEXITY : O(N^2) : AS WE HAVE TO GO THROUGH EVERY ELEMENT IN THE ARRAY 
# SPACE COMPLEXITY : O(1) 


def twoNumberSum_1(array, targetSum):
    for i in range(len(array) -1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    
    return []

num = [3,5,8,-4,11,1,-1,6]
target = 10

# print(twoNumberSum_1(num, target))


# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 

# METHOD 2 : USING HASH TABLE
# SPACE TIME COMPLEXITY:
#  TIME COMPLEXITY: O(N) : N : LENGTH OF THE ARRAY 
#  SPACE COMPLEXITY: O(N) : 

def twoNumberSum_2(array, targetSum):
    # declaring hash table
    nums ={}

    for num in array:
        
        if targetSum - num in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True    
    return []

print(twoNumberSum_2(num, target))


# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 

# METHOD 2 : USING SORTING ALGORITHM
# SPACE TIME COMPLEXITY:
#  TIME COMPLEXITY: O(N LOG N) : N : LENGTH OF THE ARRAY 
#  SPACE COMPLEXITY: O(N) : 

def twoNumberSum_3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left +=1
        elif currentSum > targetSum:
            right -= 1
    
    return []

# print(twoNumberSum_3(num, target))