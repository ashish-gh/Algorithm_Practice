



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




def branchSum(root):
    sums = []
    calculateBranchSums(root, root.data, sums)
    return sums

def calculateBranchSums(root, runningSum, sums):
    if not root.left and not root.right:
        sums.append(runningSum)
        return

    if root.left:
        runningSum += root.left.data
        calculateBranchSums(root.left, runningSum, sums)
        runningSum -= root.left.data

    if root.right:
        runningSum += root.right.data
        calculateBranchSums(root.right, runningSum, sums)
        runningSum -= root.right.data

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# inorder(root)

print(branchSum(root))
