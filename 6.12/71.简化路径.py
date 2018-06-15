class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        path=path.split('/')
        for each in path:
            if each:
                if each=='.':
                    continue
                elif each=='..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(each)
        return '/'+'/'.join(stack)