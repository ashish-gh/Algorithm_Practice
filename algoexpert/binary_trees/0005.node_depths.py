



class BinaryTree:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.data,)
        inorder(root.right)
 
def insert( node, data):
 
    # If the tree is empty, return a new node
    if node is None:
        return BinaryTree(data)

    # Otherwise recur down the tree
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node


# METHOD 1  : RECURIVE METHOD
# COMPLEXITY ANALYSIS : O(n) time | O(H) space: H: height of the binary tree

def nodeDepths_1(root, depth=0):
    if root is None:
        return 0
    
    return depth + nodeDepths_1(root.left, depth+1)+ nodeDepths_1(root.right, depth+1)



# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 

# METHOD 2  : ITERATIVE METHOD
# COMPLEXITY ANALYSIS : O(n) time | O(H) space: H: height of the binary tree

def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo['node'], nodeInfo['depth']
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumOfDepths






root = None
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 1)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)
root = insert(root, 9)

# inorder(root)
print(nodeDepths(root))
print(nodeDepths_1(root))