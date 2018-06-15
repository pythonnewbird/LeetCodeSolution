class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache=collections.OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        value=self.cache.pop(key)
        self.cache[key]=value
        return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache)==self.capacity:
            self.cache.popitem(last=False)
        self.cache[key]=value