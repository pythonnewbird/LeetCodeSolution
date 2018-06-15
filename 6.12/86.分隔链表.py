# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1=ListNode(0)
        dummy2=ListNode(0)
        cur1=dummy1
        cur2=dummy2
        while head!=None:
            if head.val<x:
                cur1.next=head
                cur1=head
            else:
                cur2.next=head
                cur2=head
            head=head.next
        cur2.next=None
        cur1.next=dummy2.next
        return dummy1.next
