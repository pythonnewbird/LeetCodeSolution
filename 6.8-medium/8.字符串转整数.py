class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i_max=2147483647
        i_min=-2147483648
        str=str.lstrip()
        slen=len(str)
        if slen==0:
            return 0
        
        i=0
        neg=False
        if str[i] in '+-':
            if str[i]=='-':
                neg=True
            i+=1
        num=0
        while i<slen and str[i].isdigit():
            num=num*10+int(str[i])
            i+=1
        
        if neg:
            num=-num
        if num<=i_min:
            return i_min
        if num>=i_max:
            return i_max
        return num