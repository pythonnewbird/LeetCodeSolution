class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_dic={}
        for s in strs:
            key=''.join(sorted(s))
            if key in res_dic:
                res_dic[key].append(s)
            else:
                res_dic[key]=[s]
        return res_dic.values()
