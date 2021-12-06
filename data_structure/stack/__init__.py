class Node:
    def __init__(self, data, next=None):
        self. data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data=data, next=None)
            self.head= node
        else:
            node = Node(data=data, next=self.head)
            self.head= node

    def add(self, data):
        self.insert_at_beginning(data=data)
    
    def pop(self):
        if self.head is None:
            return        
        self.head = self.head.next
    
    def print(self):
        iter = self.head
        while iter:
            print(iter.data)
            iter = iter.next

st = Stack()
st.add(1)
st.add(3)
st.add(5)
print("all elements")
st.print()

print("pop first element and print")
st.pop()
st.print()