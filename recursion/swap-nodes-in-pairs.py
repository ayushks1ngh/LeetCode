class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        prev = None
        curr = head

        while curr and curr.next:

            first = curr
            second = curr.next

            first.next = second.next
            second.next = first

            if prev:
                prev.next = second

            prev = first
            curr = first.next

        return head