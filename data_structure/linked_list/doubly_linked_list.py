class Node:
    def __init__(self, data, next: None, prev: None):
        self.data = data
        self.next = None
        self.prev = None

#  insert_at_beginning(), insert_at_end(), insert_at(), remove_at(), insert_all(), print_all(),

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head, prev=None)
        self.head = node
    
    def prepend(self, data):
        """
        Add elements to linked list at the beginning 
        Two cases:
            1. if the linked list is empty
            2. if the linked list has some elements
        """

        # if linked list is empty
        print(self.head)
        if self.head is None:
            print("empty")
            node = Node(data=data, next=self.head, prev=None)
            self.head = node
        else:
            # if linked list has some elements
            print("linked list has some elemets >")
            iter = self.head
            while iter.next:
                print(iter.data)
                iter = iter.next

    
        
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.prepend(1)
    dll.prepend(2)
