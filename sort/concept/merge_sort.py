"""
merge two subArrays of arr[]
1. arr[l...m]
2. arr[m+1, r]
"""


def merge(arr, l, m, r):
    # calculate sizes of subArrays
    n1 = m - l + 1
    n2 = r - m

    # create temporary arrays
    L = arr[l : l + n1]
    R = arr[m + 1 : m + 1 + n2]

    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        # recursion
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)
