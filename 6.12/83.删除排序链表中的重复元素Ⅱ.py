# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next==None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        cur=head
        while cur:
            if cur.next and cur.next.val==cur.val:
                val=cur.val
                while cur and cur.val==val:
                    cur=cur.next
                pre.next=cur
            else:
                pre=cur
                cur=cur.next
        return dummy.next
