class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for i, c in enumerate(sorted(citations, reverse = True)):
            #i+1>=c时，刚好不行
            if i >= c:
                return i
        return len(citations)