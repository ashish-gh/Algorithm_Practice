# METHOD 1  : USING WHILE LOOP
# SPACE TIME COMPLEXITY
# TIME COMPLEXITY : O(N) 
# SPACE COMPLEXITY : O(1) 

def validate_subsequence_1(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if sequence[seqIdx] == array[arrIdx]:
            seqIdx +=1
        arrIdx +=1
    
    return seqIdx == len(sequence)


array = [5,1,22,25,6,-1,8,10,11,7]
sequence = [1,6,-1,10]

print(validate_subsequence_1(array, sequence))

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 

# METHOD 2  : USING FOR LOOP
# SPACE TIME COMPLEXITY
# TIME COMPLEXITY : O(N) 
# SPACE COMPLEXITY : O(1) 


def validate_subsequence_2(array, sequence):

    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx +=1
        
    return seqIdx == len(sequence)


print(validate_subsequence_2(array, sequence))
