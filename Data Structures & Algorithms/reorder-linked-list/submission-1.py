# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeList = list()
        curr = head

        while curr:
            nodeList.append(curr)
            curr = curr.next
        
        i = 0
        j = len(nodeList) - 1

        
        while i < j:
            nodeList[i].next = nodeList[j]
            i += 1
            if i == j:
                break
            nodeList[j].next = nodeList[i]
            j -= 1
        nodeList[i].next = None


