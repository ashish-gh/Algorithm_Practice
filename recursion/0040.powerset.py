# Powerset
# -----------------

# Sample input: [1,2,3]
# Sample output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 

# Method 1: Iterative method
# O(n*2^n) time | O(n*2^n) space

def powerSet(array):
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [element])
    return subsets
    
array =[1,2,3] 
print(powerSet(array))