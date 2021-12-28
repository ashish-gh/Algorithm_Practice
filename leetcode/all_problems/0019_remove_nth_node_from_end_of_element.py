# Question asked on: Microsoft

# Given a head of linked list, remove nth node from the end of the list and return its head.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Method
# Two pointer technique

# Solution 

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def removenthnode(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # while number is greater that zero and there is valid right pointer
        while n > 0 and right:
            # shift right pointer by one and decrease n by one 
            right = right.next  
            n -= 1
        # keep shifting until the right reaches the end 
        while right:
            left = left.next
            right = right.next
        
        # delete the next node 
        # which basicall means shifting the pointer of the node
        left.next = left.next.next 
        return dummy.next


# inpute
# ListNode  = [1,2,3,4,5]
# n = 2