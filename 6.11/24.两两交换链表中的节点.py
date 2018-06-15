# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pretail=None
        prev=head
        while prev!=None:
            cur=prev.next
            if not cur:
                break
            if not pretail:
                head=cur
            else:
                pretail.next=cur
            prev.next=cur.next
            cur.next=prev
            pretail=prev
            prev=prev.next
        return head