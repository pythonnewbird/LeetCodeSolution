class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        target=collections.defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            target[a]+=b,
        route=[]
        def visit(airport):
            while target[airport]:
                visit(target[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
		
将机场视为顶点，机票看做有向边，可以构成一个有向图。

通过图（无向图或有向图）中所有边且每边仅通过一次的通路称为欧拉通路，相应的回路称为欧拉回路。具有欧拉回路的图称为欧拉图（Euler Graph），具有欧拉通路而无欧拉回路的图称为半欧拉图。

因此题目的实质就是从JFK顶点出发寻找欧拉通路，可以利用Hierholzer算法。


DFS：
#分left，right是关键
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        routes = collections.defaultdict(list)
        for s, e in tickets:
            routes[s].append(e)
        def solve(start):
            left, right = [], []
            for end in sorted(routes[start]):
                if end not in routes[start]:
                    continue
                routes[start].remove(end)
                subroutes = solve(end)
                if start in subroutes:
                    left += subroutes
                else:
                    right += subroutes
            return [start] + left + right
        return solve("JFK")