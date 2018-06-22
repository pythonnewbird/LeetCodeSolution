class Solution(object):
    def __init__(self):
        self.cache=collections.defaultdict(list)
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if not input: return None
        if input.isdigit(): return [int(input)]
        if input in self.cache:
            return self.cache[input]
        result=[]
        for i,c in enumerate(input):
            if c in '+-*':
                left=self.diffWaysToCompute(input[:i])
                right=self.diffWaysToCompute(input[i+1:])
                for x in left:
                    for y in right:
                        result.append(eval(str(x)+c+str(y)))
        self.cache[input]=result
        return result