# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        trav_a,trav_b=headA,headB
        while trav_a is not trav_b:
            trav_a=headB if not trav_a else trav_a.next
            trav_b=headA if not trav_b else trav_b.next
        return trav_a