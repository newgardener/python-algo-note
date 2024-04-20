# %%


def binary_search(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def leftmost_binary_search(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        # this ensures even if target is found, we can continue searching to the left to find first occurrence target
        if array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
        print(start, end, mid)

    if start < len(array) and array[start] == target:
        return start
    return None


def rightmost_binary_search(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        # array[mid] <= start skips the current matched target to continue searching to the right to find last occurrence target
        else:
            start = mid + 1
        print(start, end, mid)

    if end >= 0 and array[end] == target:
        return end
    return None


# %%
target = 5
array = [1, 3, 5, 5, 7, 9, 11]

print(leftmost_binary_search(array, target))
print(rightmost_binary_search(array, target))
