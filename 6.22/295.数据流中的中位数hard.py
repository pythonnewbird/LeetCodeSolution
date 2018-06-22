from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap=[]
        self.maxheap=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.maxheap,-num)
        mintop=self.minheap[0] if len(self.minheap) else None
        maxtop=self.maxheap[0] if len(self.maxheap) else None
        if -maxtop>mintop or len(self.minheap)+1<len(self.maxheap):
            heappush(self.minheap,-heappop(self.maxheap))
        if len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))
 

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxheap)>len(self.minheap):
            return -1.0*self.maxheap[0]
        else:
            return (-self.maxheap[0]+self.minheap[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()