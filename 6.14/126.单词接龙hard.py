class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wdset=set(wordList)
        if endWord not in wdset:
            return []
        lts="abcdefghijklmnopqrstuvwxyz"
        dist=float("inf")
        q=[beginWord] 
        seen={beginWord:0}
        graph={beginWord:set()}
        while q:
            cur=q.pop(0)
            d=seen[cur]
            if d>=dist:
                break
            for i in range(len(cur)):
                for lt in lts:
                    if lt!=cur[i]:
                        new=cur[:i]+lt+cur[i+1:]
                        if new in wdset and (new not in seen or d+1==seen[new]):
                            if cur in graph:
                                graph[cur].add(new)
                            else:
                                graph[cur]=set([new])
                            if new==endWord:
                                dist=d+1
                            if new not in seen:
                                seen[new]=d+1
                                q.append(new)
        res=[]
        def dfs(path,cur):
            if cur==endWord:
                res.append(path[:])
            else:
                if cur in graph:
                    for new in graph[cur]:
                        dfs(path+[new],new)
        dfs([beginWord],beginWord)
        return res