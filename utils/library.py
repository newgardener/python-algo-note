#%% 내장 함수

# sum, min, max
result = sum([1,2,3,4,5])
result1 = min([1,2,3,4,5])
result2 = max([1,2,3,4,5])
print(result, result1, result2)

# sorted
sorted_ascend = sorted([9,1,8,5,4])
sorted_descend = sorted([9,1,8,5,4], reverse=True)
sorted_tuple = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse=True)
print(sorted_ascend, sorted_descend, sorted_tuple)

# sort
data = [9,1,8,5,4]
data.sort()
print(data)

# %% itertools

from itertools import permutations
from itertools import combinations
from itertools import product

data = ['A', 'B', 'C']
result_permute = list(permutations(data, 3))
result_combi = list(combinations(data, 2))
result_product = list(product(data, repeat=2))

print(result_permute)
print(result_combi)
print(result_product)

# %% heapq

import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        # 오름차순 정렬
        heapq.heappush(h, value)
        # 내림차순 정렬
        # heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# %% bisect
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
    
# %% collections
# dequeue - 첫번째 원소 제거 (popleft()), 마지막 원소 제거 (pop()), 첫번째 인덱스에 x 삽입 (appendleft(x)), 마지막 인덱스에 x 삽입 (append(x))

from collections import deque
from collections import Counter

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter)
print(counter['blue'])
print(dict(counter))

# %%
