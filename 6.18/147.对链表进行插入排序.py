# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy=ListNode(0)
        dummy.next=head
        cur=head
        while cur.next:
            if cur.next.val<cur.val:
                pre=dummy
                while pre.next.val<cur.next.val:
                    pre=pre.next
                t=cur.next
                cur.next=t.next
                t.next=pre.next
                pre.next=t
            else:
                cur=cur.next
        return dummy.next
        
