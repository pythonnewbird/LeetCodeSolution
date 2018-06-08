class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = cnt = 0
        for c in S:
            lc = widths[ord(c) - ord('a')]
            if cnt + lc > 100:
                lines += 1
                cnt = lc
            else:
                cnt += lc
        return [lines + (cnt > 0), cnt]