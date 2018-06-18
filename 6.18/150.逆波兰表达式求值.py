class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators=['+','-','*','/']
        operand=[]
        for token in tokens:
            if token in operators:
                y,x=operand.pop(),operand.pop()
                operand.append(self.getVal(x,y,token))
            else:
                operand.append(int(token))
        return operand[0]
    def getVal(self,x,y,operator):
        return {'+':lambda x,y : x+y,
                '-':lambda x,y :x-y,
                '*':lambda x,y :x*y,
                '/':lambda x,y :int(float(x)/y)}[operator](x,y)
