words = str.split()
        if len(pattern) != len(words):
            return False
        ptnDict, wordDict = {}, {}
        for ptn, word in zip(pattern, words):
            if ptn not in ptnDict:
                ptnDict[ptn] = word
            if word not in wordDict:
                wordDict[word] = ptn
            if wordDict[word] != ptn or ptnDict[ptn] != word:
                return False
        return True