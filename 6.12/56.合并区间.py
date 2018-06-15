# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res=[]
        for i in sorted(intervals,key=lambda i: i.start):
            if res and i.start<=res[-1].end:
                res[-1].end=max(res[-1].end,i.end)
            else:
                res.append(i)
        return res