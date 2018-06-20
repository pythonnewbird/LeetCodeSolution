class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        x=(list(set([i[0] for i in buildings]+[i[1] for i in buildings])))
        x.sort()
        index=0
        heap=[]
        r=[[-1,0]]
        for i in x:
            while index<len(buildings) and buildings[index][0]<=i:
                heapq.heappush(heap,(-buildings[index][2],buildings[index][1]))
                index+=1
            while heap and heap[0][1]<=i:
                heapq.heappop(heap)
            h=-heap[0][0] if heap else 0
            if h!=r[-1][-1]:
                r.append([i,h])
        return r[1:]