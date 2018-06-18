# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        nod=UndirectedGraphNode(node.label)
        dic={node.label:nod}
        stack=[node]
        while stack:
            cur=stack.pop()
            curn=dic[cur.label]
            for n in cur.neighbors:
                if n.label not in dic:
                    dic[n.label]=UndirectedGraphNode(n.label)
                    stack.append(n)
                curn.neighbors.append(dic[n.label])
        return nod