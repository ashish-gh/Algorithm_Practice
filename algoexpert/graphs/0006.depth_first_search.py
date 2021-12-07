# Depth First Search
# -------------------

# Problem Statement
# You are given a Node class that has a name and an array of optional children Nodes. 
# When put together, Nodes form a simple tree-like structure. Implement the depthFirstSearch method
#  on the Node class, which takes in an empty array, traverses the tree using the Depth-rst Search approach 
# (specically navigating the tree from left to right), stores all the of the Nodes' names in the input array, and returns it.

# Sample input: A / |
# B C D / \ /
# E F G H / \
# I J K 
# Sample output: ["A","B","E","F","I","J","C","D","G","K","H"]

# Explanation
# We can use a Stack here


# COMPLEXITY ANALYSIS : O(v+e) time | O(v) space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


result1 = []
test1 = Node("A")
test1.addChild("B").addChild("C")
test1.children[0].addChild("D")
print(test1.depthFirstSearch(result1))

result2 = []
test2 = Node("A")
test2.addChild("B").addChild("C").addChild("D").addChild("E")
test2.children[1].addChild("F")
print(test2.depthFirstSearch(result2))