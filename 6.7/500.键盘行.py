class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rs = map(set, ['qwertyuiop','asdfghjkl','zxcvbnm'])
        ans = []
        for word in words:
            wset = set(word.lower())
            if any(wset <= rset for rset in rs):
                ans.append(word)
        return ans
        