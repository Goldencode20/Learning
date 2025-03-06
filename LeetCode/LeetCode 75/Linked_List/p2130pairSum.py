class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        sums = []
        count = 0
        left_head = ListNode(next=head)
        right_head = head

        while right_head != None and right_head.next.next != None:
            right_head = right_head.next.next
            left_head = left_head.next
            sums.append(left_head.val)
            count += 1
        
        left_head = left_head.next
        sums.append(left_head.val)

        while left_head != None and left_head.next != None:
            left_head = left_head.next
            sums[count] += left_head.val 
            count -= 1

        return max(sums)