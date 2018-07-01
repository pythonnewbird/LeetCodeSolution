class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = collections.deque()
        for item in preorder.split(','):
            stack.append(item)
            while len(stack) >= 3 and \
                  stack[-1] == stack[-2] == '#' and \
                  stack[-3] != '#':
                stack.pop(), stack.pop(), stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack[0] == '#'
		
		
#在二叉树中，如果我们将空节点视为叶子节点，那么除根节点外的非空节点（分支节点）提供2个出度和1个入度（2个孩子和1个父亲）

所有的空节点提供0个出度和1个入度（0个孩子和1个父亲）

假如我们尝试重建这棵树。在构建的过程中，记录出度与入度之差，记为diff = outdegree - indegree

当遍历节点时，我们令diff - 1（因为节点提供了一个入度）。如果节点非空，再令diff + 2（因为节点提供了2个出度）

如果序列化是正确的，那么diff在任何时刻都不会小于0，并且最终结果等于0


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        diff = 1
        for item in preorder.split(','):
            diff -=1
            if diff < 0: return False
            if item != '#': diff += 2
        return diff == 0