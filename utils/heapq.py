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

#%% heapify
import heapq

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

heapq.heapify(nums)
for _ in range(len(nums) - k):
    heapq.heappop(nums)
heapq.heappop(nums) # Kth largest num

#%% nlargest 
import heapq

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

heapq.nlargest(k, nums)[-1]
