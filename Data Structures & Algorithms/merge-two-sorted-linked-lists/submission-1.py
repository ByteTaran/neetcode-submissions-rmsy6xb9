# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        newList = currNew = ListNode()

        while curr1 and curr2:
            if curr1.val < curr2.val:
                currNew.next = curr1
                curr1 = curr1.next
            else:
                currNew.next = curr2
                curr2 = curr2.next
            currNew = currNew.next
        
        currNew.next = curr1 or curr2

        return newList.next