class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        nums=[]
        for w in words:
            nums+=sum(1<<(ord(x)-ord('a')) for x in set(w)),
        ans=0
        for x in range(len(words)):
            for y in range(len(words)):
                if not (nums[x]&nums[y]):
                    ans=max(ans,len(words[x]) * len(words[y]))
        return ans