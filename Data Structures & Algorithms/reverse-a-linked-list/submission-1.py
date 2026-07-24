# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        prevNode = None

        while curr:
            temp = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = temp

        return prevNode