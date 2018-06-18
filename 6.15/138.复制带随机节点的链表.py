# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        h=head
        while h:
            n=RandomListNode(h.label)
            n.next=h.next
            h.next=n
            h=n.next
        h=head
        while h:
            if h.random:
                h.next.random=h.random.next
            h=h.next.next
        nh=dummy=RandomListNode(0)
        h=head
        while h:
            nh.next=h.next
            nh=nh.next
            t=h.next.next
            h.next=t
            h=t
        return dummy.next
#O(N),O(1)
1. 遍历原链表，并复制每一个节点，将新节点插入原节点之后

2. 遍历新链表，为其中的新增节点设置random指针

3. 重建原链表，并提取出拷贝的新节点