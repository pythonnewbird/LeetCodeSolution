# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or k==0:
            return head
        p=head
        length=1
        while p.next!=None:
            p=p.next
            length+=1
        p.next=head
        left_k=length-k%length
        i=0
        while i!=left_k:
            p=p.next
            i+=1
        pp=p.next
        p.next=None
        return pp