class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        tokens = re.sub('[\!\?\'\,;\.]', '', paragraph.lower()).split()
        cnt = collections.Counter(tokens)
        for ban in banned:
            if ban in cnt:
                del cnt[ban]
        return cnt.most_common(1)[0][0]