class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wset = set([''])
        ans = ''
        for word in sorted(words):
            if word[:-1] in wset:
                wset.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans