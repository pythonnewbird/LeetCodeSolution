class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqrt = int(math.sqrt(area))
        L, W = area, 1
        for x in range(sqrt, 0, -1):
            if area % x == 0:
                L, W = area / x, x
                break
        return [L, W]