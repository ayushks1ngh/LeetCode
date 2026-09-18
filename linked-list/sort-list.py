# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # isn;t this very simple
        l = []
        curr = head
        while head:
            l.append(head.val)
            head = head.next
        
        l.sort()
        count = 0
        head = curr
        while head:
            head.val = l[count]
            head = head.next
            count += 1
        
        return curr
        