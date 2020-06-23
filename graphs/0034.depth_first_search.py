# Problem Statement
# -------------------

# You are given a Node class that has a name and an array of optional children Nodes. 
# When put together, Nodes form a simple tree-like structure. Implement the breadthFirstSearch method 
# on the Node class, which takes in an empty array, traverses the tree using the Breadth-rst Search approach 
# (specically navigating the tree from left to right), stores all of the Nodes' names in the input array, and 
# returns it. 

# Sample input: A 
#             B C D 
#            E F   G H 
#           I      J K 

# Sample output: ["A","B","C","D","E","F","G","H","I","J","K"]

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))

    # O(v + e) time | O(v) space 
    def depthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)

        return array
        
result = []
test = Node("A")
test.addChild("B")
test.addChild("C")
test.addChild("D")
test.children[0].addChild("E")
test.children[0].addChild("F")
test.children[2].addChild("G")
test.children[2].addChild("H")

print(test.depthFirstSearch(result))
