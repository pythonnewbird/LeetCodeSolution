class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children=collections.defaultdict(set)
        for x,y in edges:
            children[x].add(y)
            children[y].add(x)
        num=set(children.keys())
        while len(num)>2:
            leaves=[x for x in children if len(children[x])==1]
            for x in leaves:
                for y in children[x]:
                    children[y].remove(x)
                del children[x]
                num.remove(x)
        return list(num) if n!=1 else [0]