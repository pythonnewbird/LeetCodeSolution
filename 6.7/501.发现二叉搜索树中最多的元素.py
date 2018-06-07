# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counter = collections.Counter()
        def traverse(root):
            if not root: return
            counter[root.val] += 1
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        maxn = max(counter.values() + [None])
        return [e for e, v in counter.iteritems() if v == maxn]