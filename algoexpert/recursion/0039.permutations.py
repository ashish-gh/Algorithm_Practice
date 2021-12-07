# Permutations
# -------------

# Sample input: [1,2,3]
# Sample output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# UpperBound O(n^2*n!) time | O(n*n!) space
def getPermutations(array):
    permutations  = []
    permutationHelper(array, [], permutations)
    return permutations

def permutationHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPermutation = currentPermutation + [array[i]]
            permutationHelper(newArray, newPermutation, permutations)


array = [1,2,3]
print(getPermutations(array))            
