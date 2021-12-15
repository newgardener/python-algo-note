# %% 특정한 합을 가지는 부분 연속 수열 찾기

def count_interval_sum(data, sum):
    count = 0
    end = 0
    interval_sum = 0
    
    for start in data:
        while interval_sum < sum and end < len(data):
            interval_sum += data[end]
            end += 1
        if interval_sum == sum:
            count += 1
        interval_sum -= start
    
    return count

data = [1,2,3,2,5]
count_interval_sum(data, 5)

# %% 정렬되어 있는 두 리스트의 합집합

def union_of_two_sorted_list(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    
    result = [0] * (n + m)
    i, j, k = 0, 0, 0

    while i < n or j < m:
        if j >= m or (i < n and arr1[i] <= arr2[j]):
            result[k] = arr1[i]
            i += 1
        else:
            result[k] = arr2[j]
            j += 1
        k += 1
    
    return result

arr1 = [1,3,5]
arr2 = [2,4,6,8]
union_of_two_sorted_list(arr1, arr2)

