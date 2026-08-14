# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fastPointer = head
        slowPointer = head

        while fastPointer.next and fastPointer.next.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if slowPointer == fastPointer:
                return True
        return False