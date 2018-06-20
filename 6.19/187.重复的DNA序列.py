class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        count = {}
        map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        ans = []
        sum = 0
        for x in range(len(s)):
			#确保记录10位DNA序列
            sum = (sum * 4 + map[s[x]]) & 0xFFFFF
            if x < 9:
                continue
            count[sum] = count.get(sum, 0) + 1
            if count[sum] == 2:
                ans.append(s[x - 9:x + 1])
        return ans
