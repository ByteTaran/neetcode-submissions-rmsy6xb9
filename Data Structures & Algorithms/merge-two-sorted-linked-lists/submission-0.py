# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        c1 = list1
        c2 = list2

        newNode = cNew = ListNode()

        while c1 and c2:
            if c1.val > c2.val:
                cNew.next = c2
                c2 = c2.next
            else:
                cNew.next = c1
                c1 = c1.next
            cNew = cNew.next
        
        cNew.next = c1 or c2

        return newNode.next