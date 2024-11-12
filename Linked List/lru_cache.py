'''
Question: https://leetcode.com/problems/lru-cache/
'''

from collections import OrderedDict
class LRUCache:
    '''
    Maintain an OrderedDict to keep track of which key-value pairs were added in the end
    Check: https://www.youtube.com/watch?v=c8qKdgEuCh8
    '''
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)