# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        l=head
        counter=0
        sum=0
        while counter or l1 or l2:
            sum,counter=counter,0
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            if sum>9:
                counter=1
                sum-=10
            l.next=ListNode(sum)
            l=l.next
        return head.next