
# O(d) time | O(1) space
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.ancestor = None 

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
    

def youngestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDepth(descendantOne, topAncestor) 
    depthTwo = getDepth(descendantTwo, topAncestor)

    if depthOne > depthTwo:
        return backTrack(descendantOne, descendantTwo, depthOne - depthTwo)
    else: 
        return backTrack(descendantTwo, descendantOne, depthTwo - depthOne)



def getDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        if descendant.ancestor is None:
            return depth 
        
        depth += 1
        descendant = descendant.ancestor    
    return depth
    

def backTrack(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    
    return lowerDescendant
        

#                a
#              /  \ 
#             b    c
#           /  \    
#         d     e
#       /  \
#      f    g
# 
# 
# 
# 
bst = BinaryTree("a")

bst.root.left = Node("b")
bst.root.ancestor = bst.root

bst.root.right = Node("c")
bst.root.ancestor = bst.root

bst.root.left.left = Node("d")
bst.root.left.left.ancestor =  bst.root.left

bst.root.left.right = Node("e")
bst.root.left.right.ancestor = bst.root.left

bst.root.left.left.left = Node("f")
bst.root.left.left.left.ancestor = bst.root.left.left

bst.root.left.left.right = Node("g")
bst.root.left.left.right.ancestor = bst.root.left.left

yca = youngestCommonAncestor(bst.root, bst.root.left , bst.root.left.left.right).data
print("Youngest common ancestor of b and g is: {} ".format(yca))
