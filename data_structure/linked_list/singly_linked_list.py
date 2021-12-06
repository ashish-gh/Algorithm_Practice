# issues with arrays
# 

# solve by linked-list 
# - you don't have to pre-allocate the memory
# - insertion is easier
# - 

#############
################################
#############




class Node:
    def __init__(self, data, next: None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        iter = self.head
        all_data = ""
        while iter:
            all_data += str(iter.data) + "-->" if iter.next else str(iter.data)
            iter = iter.next
        print(all_data)
    
    def get_length(self):
        count = 0
        iter = self.head
        while iter:
            count +=1
            iter = iter.next
        return count
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        iter = self.head
        while iter.next:
            iter = iter.next        
        iter.next = Node(data, None)
    
    def insert_at(self, index, data):
        if index < 0  or index > self.get_length():
            raise Exception("Invalid index")
        
        if index ==0:
            self.insert_at_beginning(data=data)
        
        count = 0
        iter = self.head
        while iter:
            if count == index -1:
                node = Node(data, iter.next)
                iter.next = node
                break                
            count +=1
            iter = iter.next
    def remove_at(self, index):
        if index<0 or index > self.get_length():
            raise Exception("Invalid index")        
        if index ==0:
            self.head = self.head.next
        
        count = 0
        iter = self.head
        while iter:
            if count == index -1:
                iter.next = iter.next.next
                break
            count +=1
            iter = iter.next
    
    def insert_values(self, datas):
        for data in datas:
            self.insert_at_end(data)
    
    def prepend(self, data):
        if self.head is None:
            node = Node(data=data, next=None)
            self.head = node
        else:
            node = Node(data=data, next=self.head)
            self.head = node
        
    def print_append(self):
        all_data = []
        iter = self.head
        while iter:
            all_data.append(iter.data)
            iter = iter.next
        print(all_data)
    

        

# insert_at_beginning(), insert_at_end(), insert_at(), remove_at(), insert_all(), print_all(),


    
if __name__ == '__main__':
    ll = LinkedList()
    # ll.prepend(0)
    # ll.prepend(3)
    # ll.prepend(23)
    ll.append(1)
    ll.append(3)
    ll.append(4)
    ll.append(2)
    ll.append(3)
    # ll.append(4)
    # ll.prepend(5)
    ll.print_append()

