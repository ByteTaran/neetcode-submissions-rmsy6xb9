# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        curr = slow.next
        prev = None
        slow.next = prev
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        right = prev
        left = head

        while left and right:
            tempLeft = left.next
            tempRight = right.next

            left.next = right
            right.next = tempLeft
                

            left = tempLeft
            right = tempRight
        

        
