class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None:
            return head 

        odd = head
        even = head.next
        ehead = even

        while even != None and even.next != None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = ehead

        return head