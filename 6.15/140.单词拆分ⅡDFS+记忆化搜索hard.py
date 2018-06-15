class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        tokendict={}
        def dfs(s):
            ans=[]
            if s in wordDict:
                ans.append(s)
            for i in range(len(s)-1):
                prefix,suffix=s[:i+1],s[i+1:]
                
                if prefix not in wordDict:
                    continue
                else:
                    rest=[]
                    if suffix in tokendict:
                        rest=tokendict[suffix]
                    else:
                        rest=dfs(suffix)
                    for n in rest:
                        ans.append(prefix+' '+n)
            tokendict[s]=ans
            return ans
        return dfs(s)
                        