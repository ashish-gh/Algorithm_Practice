# Question in Facebook:

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None 

    def printList(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
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
    def merge_k_sorted_lists(self, lists: List[ListNode]) -> ListNode:
        print(f"Merging sorting linked lists . .. ")
        if not lists or len(lists) == 0: return None        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # here we have to check for odd number of linked list 
                l2 = lists[i +1] if (i + 1) > len(lists) else None
                # if the second list is empty it does not impact the mergeing algo
                two_merged = self.merge_two_sorted_lists(l1, l2)
                merged_lists.append(self.merge_two_sorted_lists(l1, l2))
            lists = merged_lists
        return lists[0]


    def merge_two_sorted_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else: 
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next

def print_(l):
    print("--------")
    l.printList()
    print("\n------------")

def main():
    print("Linked list one")
    L1 = LinkedList()
    L1.addToList(1)
    L1.addToList(2)
    print_(L1)

    print("Linked list two")
    L2 = LinkedList()
    L2.addToList(1)
    L2.addToList(3)
    L2.addToList(4)
    L2.addToList(6)
    print_(L2)

    merged_lsts = [L1, L2]
    sol = Solution()
    sol.merge_k_sorted_lists(lists=merged_lsts)
    
   
    
    


if __name__ == "__main__":
    main()