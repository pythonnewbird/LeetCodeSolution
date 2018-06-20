class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1Arr = version1.split(".")
        v2Arr = version2.split(".")
        len1 = len(v1Arr)
        len2 = len(v2Arr)
        lenMax = max(len1, len2)
        for x in range(lenMax):
            v1Token = 0
            if x < len1:
                v1Token = int(v1Arr[x])
            v2Token = 0
            if x < len2:
                v2Token = int(v2Arr[x])
            if v1Token < v2Token:
                return -1
            if v1Token > v2Token:
                return 1
        return 0