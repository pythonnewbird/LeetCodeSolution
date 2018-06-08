class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        cnt=collections.defaultdict(int)
        for cp in cpdomains:
            count,domain=cp.split()
            parts=domain.split('.')[::-1]
            for x in range(1,len(parts)+1):
                cnt['.'.join(parts[:x][::-1])]+=int(count)
        return ['{} {}'.format(k,v) for v,k in cnt.items()]