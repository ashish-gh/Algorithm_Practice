# Questions on : Microsoft

# Question
# Merge two sorted lists


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None 
    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
 
    # Method to add element to list
    def addToList(self, newData):
        newNode = ListNode(val=newData)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
 



class Solution:
    def merge_two_sorted_list(self, l1: ListNode, l2: ListNode)-> ListNode:
        # dummy node so don't have to worry about inserting to empty list
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next            
            tail = tail.next
        # find the non-empty list and insert the remaining to the list
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next


def main():
    listA = LinkedList()
    listB = LinkedList()
    listA.addToList(1)
    listA.addToList(2)
    listA.addToList(4)
    listB.addToList(1)
    listB.addToList(3)
    listB.addToList(4)
    print(listB.printList())
    # sl = Solution()
    # print(sl.merge_two_sorted_list(listA,listB))
        

if __name__ == "__main__":
    main()