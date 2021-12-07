
# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
class BinaryTree:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

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

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# METHOD 1: ITERATIVE
# O(n) time | O(n) space
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
            
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# METHOD 2: RECURSIVE
# O(n) time | O(d) space
def invertBinaryTree_re(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)



root = None
root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 8)
root = insert(root, 9)


print((root))