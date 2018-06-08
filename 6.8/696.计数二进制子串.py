class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        cnt = [0, 0]
        last = None
        ans = 0
        for c in s:
            c = int(c)
            if c != last: cnt[c] = 0
            cnt[c] += 1
            if cnt[c] <= cnt[1 - c]: ans += 1
            last = c
        return ans