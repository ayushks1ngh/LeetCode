class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        vals = []

        while list1:
            vals.append(list1.val)
            list1 = list1.next

        while list2:
            vals.append(list2.val)
            list2 = list2.next

        vals.sort()

        dummy = ListNode(0)
        curr = dummy

        for v in vals:
            curr.next = ListNode(v)
            curr = curr.next

        return dummy.next
        