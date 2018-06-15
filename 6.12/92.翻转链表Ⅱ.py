dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for i in range(m-1):
            pre=pre.next
        cur=pre.next
        for i in range(n-m):
            next=cur.next
            next.next,pre.next,cur.next=pre.next,next,next.next
        return dummy.next