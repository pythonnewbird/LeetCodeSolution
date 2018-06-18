class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        queue=[s]
        visited=set([s])
        while queue:
            cur=queue.pop(0)
            if cur in wordDict:
                return True
            prefix=''
            for c in cur:
                prefix+=c
                suffix=cur[len(prefix):]
                if prefix in wordDict and suffix not in visited:
                    queue.append(suffix)
                    visited.add(suffix)
        return False
                    