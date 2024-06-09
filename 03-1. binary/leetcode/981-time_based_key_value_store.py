import collections

"""
Time Complexity of get: O(logn) where n is the number of value of a target key
"""


class TimeMap:
    def __init__(self):
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""

        value = self.dict[key]
        l, r = 0, len(value) - 1
        while l <= r:
            mid = (l + r) // 2
            if value[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if r < 0:
            return ""
        return value[r][0]
