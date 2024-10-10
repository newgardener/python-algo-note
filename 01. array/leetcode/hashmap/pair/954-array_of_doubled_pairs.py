from collections import Counter

"""
arr = [4,-2,2,-4]
iterate -2 -> 2 -> -4 -> 4
decrement the count of matching pair (arr[i] * 2 == arr[j]) ex. (-2, -4), (2, 4)
"""


def canReorderDoubled(self, arr: list[int]) -> bool:
    counter = Counter(arr)
    for key in sorted(counter.keys(), key=abs):
        if counter[key] > counter[2 * key]:
            return False
        counter[2 * key] -= counter[key]
    return True
