# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        stack=[]
        while head!=None:
            stack.append(head.val)
            head=head.next
        root=self.helper(stack)
        return root
    def helper(self,stack):
        if not stack:
            return 
        mid=len(stack)/2
        root=TreeNode(stack[mid])
        root.left=self.helper(stack[:mid])
        root.right=self.helper(stack[mid+1:])
        return root