class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dic, res = {str(i): i for i in range(10)},[0, 0]
        for i, n1 in enumerate(num1): res[0] += dic[n1] *  (10 ** (len(num1) - 1 - i))
        for i, n2 in enumerate(num2): res[1] += dic[n2] *  (10 ** (len(num2) - 1 - i))
        return str(res[0] * res[1])