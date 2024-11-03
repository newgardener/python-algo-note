def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
    def mergeSort(arr, l, r):
        if l >= r:
            return 0
        mid = l + (r - l) // 2
        count = mergeSort(arr, l, mid) + mergeSort(arr, mid + 1, r)

        # count pairs
        i = j = mid + 1
        for leftSum in arr[l : mid + 1]:
            while i <= r and arr[i] - leftSum < lower:
                i += 1
            while j <= r and arr[j] - leftSum <= upper:
                j += 1
            count += j - i

        # merge
        merged = []
        i, j = l, mid + 1
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                merged.append(arr[i])
                i += 1
            else:
                merged.append(arr[j])
                j += 1
        merged.extend(arr[i : mid + 1])
        merged.extend(arr[j : r + 1])
        arr[l : r + 1] = merged
        return count

    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    return mergeSort(prefix, 0, len(prefix) - 1)
