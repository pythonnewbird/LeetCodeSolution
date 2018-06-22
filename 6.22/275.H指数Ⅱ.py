class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        m=len(citations)
        start=0
        end=m-1
        while start<=end:
            mid=(start+end)/2
            if citations[mid]==m-mid:
                return m-mid
            elif citations[mid]<m-mid:
                start=mid+1
            else:
                end=mid-1
        return m-start