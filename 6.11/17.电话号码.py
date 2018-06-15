class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)<1:
            return []
        dic_dig={"1":"","2":'abc',"3":'def',"4":'ghi',"5":'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result=['']
        for digit in digits:
            strSequence=dic_dig.get(digit)
            new_result=[]
            for string in  strSequence:
                for element in result:
                    new_result.append(element+string)
            result=new_result
        return result
        