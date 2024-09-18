import bisect

"""
Find the leftmost position where target should be inserted
"""


def binary_search_left(arr, target):
    index = bisect.bisect_left(arr, target)
    if index != len(arr) and arr[index] == target:
        return index
    return -1


"""
Find the rightmost position where target should be inserted
"""


def binary_search_right(arr, target):
    index = bisect.bisect_right(arr, target)
    if index != 0 and arr[index - 1] == target:
        return index - 1
    return -1


"""
Count the number of occurrences of target in arr
"""


def count_occurrences(arr, target):
    left = bisect.bisect_left(arr, target)
    right = bisect.bisect_right(arr, target)
    return right - left


arr = [1, 2, 3, 3, 3, 4, 4, 5]
target = 3
print(f"Leftmost position of {target}: {binary_search_left(arr, target)}")
print(f"Rightmost position of {target}: {binary_search_right(arr, target)}")
print(f"# of occurrences of {target}: {count_occurrences(arr, target)}")

