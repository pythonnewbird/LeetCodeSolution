class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls,lp=len(s),len(p)
        cp=collections.Counter(p)
        ans=[]
        count=lp
        for i in range(ls):
            if cp[s[i]]>=1:
                count-=1
            cp[s[i]]-=1
            if i>=lp:
                if cp[s[i-lp]]>=0:
                    count+=1
                cp[s[i-lp]]+=1
            if count==0:
                ans.append(i-lp+1)
        return ans