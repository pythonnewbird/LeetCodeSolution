class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ''
        round = int(math.ceil(len(s) / (2.0 * k)))
        for x in range(round):
            ans += s[x * 2 * k : (x * 2 + 1) * k][::-1] 
            ans += s[(x * 2 + 1) * k : (x * 2 + 2) * k]
        return ans