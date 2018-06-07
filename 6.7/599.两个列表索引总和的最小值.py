class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {v : i for i, v in enumerate(list1)}
        minSum = len(list1) + len(list2)
        ans = []
        for i, r in enumerate(list2):
            if r not in dict1:
                continue
            currSum = i + dict1[r]
            if currSum < minSum:
                ans = [r]
                minSum = currSum
            elif currSum == minSum:
                ans.append(r)
        return ans