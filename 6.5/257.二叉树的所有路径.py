DFS：


self.ans = []
        if root is None:
            return self.ans
        def dfs(root, path):
            if root.left is None and root.right is None:
                self.ans += path,
            if root.left:
                dfs(root.left, path + "->" + str(root.left.val))
            if root.right:
                dfs(root.right, path + "->" + str(root.right.val))
        dfs(root, str(root.val))
        return self.ans
		
BFS：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        from collections import deque
        if root is None:
            return []
        queue = deque( [ [root, str(root.val)] ] )
        ans = []
        while queue:
            front, path = queue.popleft()
            if front.left is None and front.right is None:
                ans += path,
                continue
            if front.left:
                queue += [front.left, path + "->" + str(front.left.val)],
            if front.right:
                queue += [front.right, path + "->" + str(front.right.val)],
        return ans