# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return None
        slow,fast=head.next,head.next.next
        while fast and fast.next and slow!=fast:
            fast=fast.next.next
            slow=slow.next
        if fast is None or fast.next is None:
            return None
        slow=head
        while slow!=fast:
            slow,fast=slow.next,fast.next
        return slow