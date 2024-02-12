# %% two_sum solution 1
# this solution is only applicable to the sorted array


def two_sum(data, sum):
    left, right = 0, len(data) - 1
    while not left == right:
        if data[left] + data[right] < sum:
            left += 1
        elif data[left] + data[right] > sum:
            right -= 1
        else:
            return [left, right]


# %% two_sum solution 2


def two_sum(data, sum):
    nums_map = {}

    for i, num in enumerate(data):
        if sum - num in nums_map:
            return [nums_map[sum - num], i]
        nums_map[num] = i
