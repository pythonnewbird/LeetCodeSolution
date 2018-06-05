class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sourceMap, targetMap = dict(), dict()
        for x in range(len(s)):
            source, target = sourceMap.get(t[x]), targetMap.get(s[x])
            if source is None and target is None:
                sourceMap[t[x]], targetMap[s[x]] = s[x], t[x]
            elif target != t[x] or source != s[x]:
                return False
        return True
        