class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = []

        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        idx = len(nodes) - n

        if idx == 0:
            return head.next

        nodes[idx - 1].next = nodes[idx].next

        return head