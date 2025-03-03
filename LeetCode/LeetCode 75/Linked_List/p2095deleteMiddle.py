import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(unittest.TestCase):

    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        
        zero_node = ListNode(0)
        zero_node.next = head   
        slow = zero_node
        fast = head

        while (fast != None) and (fast.next != None):
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return zero_node.next

    def test(self):
        p1 = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6, None)))))))
        p2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
        p3 = ListNode(2, ListNode(1, None))
        a1 = ListNode(1, ListNode(3, ListNode(4, ListNode(1, ListNode(2, ListNode(6, None))))))
        a2 = ListNode(1, ListNode(2, ListNode(4, None)))
        a3 = ListNode(2, None)
        self.assertEqual(self.deleteMiddle(p1), a1)
        self.assertEqual(self.deleteMiddle(p2), a2)
        self.assertEqual(self.deleteMiddle(p3), a3)

if __name__ == '__main__':
    unittest.main()