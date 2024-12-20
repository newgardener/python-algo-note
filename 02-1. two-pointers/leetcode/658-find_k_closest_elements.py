# %%
# Log(n) + k
# More code but more intuitive
def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
    l, r = 0, len(arr) - 1

    # find index of x or the closest val to x
    val, idx = arr[0], 0
    while l <= r:
        m = l + (r - l) // 2
        curDiff = abs(arr[m] - x)
        resDiff = abs(val - x)
        if curDiff < resDiff or (curDiff == resDiff and arr[m] < val):
            val, idx = arr[m], m

        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            r = m - 1
        else:
            break

    l = r = idx
    for i in range(k - 1):
        if l == 0:
            r += 1
        elif r == len(arr) - 1 or x - arr[l - 1] <= arr[r + 1] - x:
            l -= 1
        else:
            r += 1
    return arr[l : r + 1]


# %%
# Log(n-k) + k
# elegant but difficult to understand
def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
    l, r = 0, len(arr) - k

    while l < r:
        m = l + (r - l) // 2
        if x - arr[m] > arr[m + k] - x:
            l = m + 1
        else:
            r = m
    return arr[l : l + k]
