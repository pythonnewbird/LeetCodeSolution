1. 利用快慢指针找到链表中点mid，将链表分为左右两半
2. 将链表的右半部分就地逆置
3. 合并链表的左右两部分


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return None
        fast,slow=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        pre=None
        cur=slow.next
        slow.next=None
        while cur:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        head2=pre
        dummy=ListNode(0)
        head1=head
        while head2 or head1:
            if head1:
                next=head1.next
                dummy.next=head1
                dummy=dummy.next
                head1=next
            if head2:
                next=head2.next
                dummy.next=head2
                dummy=dummy.next
                head2=next
        
            
        