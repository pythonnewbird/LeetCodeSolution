    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache={}
        self.count=collections.defaultdict(collections.OrderedDict)
        self.min=0
        self.capacity=capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache: return -1
        value,count=self.cache[key]
        del self.count[count][key]
        if count==self.min and not self.count[count]:
            self.min+=1
        self.count[count+1][key]=0
        self.cache[key]=(value,count+1)
        return value
            
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity<=0: return
        if key in self.cache:
            old,old_=self.cache[key]
            self.cache[key]=(value,old_)
            self.get(key)
        elif len(self.cache)==self.capacity:
            old_k,old_c=self.count[self.min].popitem(last=False)
            del self.cache[old_k]
            self.min=1
            self.cache[key] = (value, 1)
            self.count[1][key] = 0
        else:
            self.min = 1
            self.cache[key] = (value, 1)
            self.count[1][key] = 0
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)