class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        total, div = 1, 2
        while div * div <= num:
            if num % div == 0:
                total += div
                if div * div != num:
                    total += num / div
            div += 1
        return num > 1 and total == num