# METHOD 1  : RECURSIVE 
# AVERAGE : O(Log(n)) time | O(log(n))  space
# WORST : O(n) time | O(n) space

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    
    if abs(target - closest ) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest


# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 


# METHOD 1  : RECURSIVE 
# AVERAGE : O(Log(n)) time | O(1)  space
# WORST : O(n) time | O(1) space


def findClosestValueInBst_2(tree, target):
    return findClosestValueInBstHelper_2(tree, target, float("inf"))

def findClosestValueInBstHelper_2(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            closest = currentNode.left
        elif target > currentNode.right:
            closest = currentNode.right
        else:
            break
    return closest