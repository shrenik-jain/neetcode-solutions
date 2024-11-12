'''
Question: https://leetcode.com/problems/time-based-key-value-store/
'''

from collections import defaultdict

class TimeMap:

    def __init__(self):
        # store: { key1: [ [value1, timestamp1], [value2, timestamp2] ], 
        #          key2: [ [value1, timestamp1], [value2, timestamp2] ].... }
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        # get the values list from the key in the hashMap
        values = self.store.get(key, [])
        # init the res variable
        res = ""

        # set the left and right pointers
        left, right = 0, len(values)-1

        while left <= right:
            mid = (left + right) // 2

            # valid timestamp (either exact match or lesser than required timestamp)
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1

            # invalid timestamp (greater than required timestamp)
            else:
                right = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)