class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        if len(S) % K:
            S = '#' * (K - len(S) % K) + S
        return '-'.join(S[x:x + K] for x in range(0, len(S), K)).replace('#', '')