class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ans = 0
        for i, v in enumerate(flowerbed):
            if v: continue
            if i > 0 and flowerbed[i - 1]: continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1]: continue
            ans += 1
            flowerbed[i] = 1
        return ans >= n