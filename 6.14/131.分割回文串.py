class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def search(s,i,path,res):
            if i==len(s):
				#注意的是：这个[:]不能省略
                res.append(path[:])
                return
            if len(path)>=1 and path[-1]==s[i]:
                a=path[-1]
                c=a+a
                path[-1]=c
                search(s,i+1,path,res)
                path[-1]=a
            if len(path)>1 and path[-2]==s[i]:
                a,b=path[-2:]
                path.pop()
                c=a+b+a
                path[-1]=c
                search(s,i+1,path,res)
                path[-1]=a
                path.append(b)
            path.append(s[i])
            search(s,i+1,path,res)
            path.pop()
        path=[]
        res=[]
        search(s,0,path,res)
        return res