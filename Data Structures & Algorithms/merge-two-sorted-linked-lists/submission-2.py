# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        curr1 = list1
        curr2 = list2

        if curr1.val <= curr2.val:
            resNode = ListNode(curr1.val)
            resCurr = resNode
            curr1 = curr1.next
        else:
            resNode = ListNode(curr2.val)
            resCurr = resNode
            curr2 = curr2.next
        
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                resCurr.next = curr1
                
                curr1 = curr1.next
                resCurr = resCurr.next
            else:
                resCurr.next = curr2
                curr2 = curr2.next
                resCurr = resCurr.next
        
        if curr1:
            resCurr.next = curr1
        
        if curr2:
            resCurr.next = curr2
        
        return resNode