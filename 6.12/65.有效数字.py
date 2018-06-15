class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return False
        s=s.strip()
        res=signs=eE=dot=False
        for c in s:
            if '0'<=c<='9':
                res=signs=True
            elif c=='.' and not dot:
                dot=signs=True
            elif (c=='e' or c=='E') and (not eE) and res:
                res=signs=False
                dot=eE=True
            elif (c=='+' or c=='-') and not res and not signs:
                signs=True
            else:
                return False
        return res