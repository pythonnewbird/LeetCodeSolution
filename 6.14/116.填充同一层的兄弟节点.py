# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        while root and root.left:
            node=root.left
            while root:
                root.left.next=root.right
                root.right.next=root.next.left if root.next else None
                root=root.next
            root=node