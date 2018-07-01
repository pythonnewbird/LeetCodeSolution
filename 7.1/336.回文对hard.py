class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        lookup={}
        for i,word in enumerate(words):
            lookup[word[::-1]]=i
        res=[]
        for i,word in enumerate(words):
            for j in range(len(word)+1):
                pre,pos=word[:j],word[j:]
                if pre in lookup and lookup[pre]!=i and pos==pos[::-1]:
                    res.append((i,lookup[pre]))
                if j>0 and pos in lookup and lookup[pos]!=i and pre==pre[::-1] and (lookup[pos],i) not in res:
                    res.append((lookup[pos],i))
        return res