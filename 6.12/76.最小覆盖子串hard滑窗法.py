class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mp=collections.defaultdict(int)
        for c in t:
            mp[c]+=1
        count=len(mp)
        begin=head=0
        d=float('inf')
        for end in range(len(s)):
            tmp=s[end]
            if tmp in mp:
                mp[tmp]-=1
                if mp[tmp]==0:
                    count-=1
            while count==0:
                if d>end-begin:
                    d=end-begin+1
                    head=begin
                tmp=s[begin]
                if tmp in mp:
                    mp[tmp]+=1
                    if mp[tmp]>0:
                        count+=1
                begin+=1
        if d==float('inf'):
            return ''
        else:
            return s[head:head+d]