# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        pre=None
        p=slow.next
        while p:
            next=p.next
            p.next=pre
            pre=p
            p=next
        p1=head
        p2=pre
        while p2  and p1.val==p2.val:
            p1=p1.next
            p2=p2.next
        p=pre
        pre=None
        while p:
            next=p.next
            p.next=pre
            pre=p
            p=next
        slow.next=pre
        return p2 is None