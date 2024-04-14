# %% minHeap implementation (1)
def heapify(arr, size, index):
    smallestIndex = index
    leftChildIndex = 2 * index + 1
    rightChildIndex = 2 * index + 2

    if leftChildIndex < size and arr[leftChildIndex] < arr[smallestIndex]:
        smallestIndex = leftChildIndex

    if rightChildIndex < size and arr[rightChildIndex] < arr[smallestIndex]:
        smallestIndex = rightChildIndex

    if smallestIndex != index:
        arr[index], arr[smallestIndex] = arr[smallestIndex], arr[index]
        heapify(arr, size, smallestIndex)


def insert_min_heap(arr, value):
    arr.append(value)
    size = len(arr)

    for index in range(size // 2 - 1, -1, -1):
        heapify(arr, size, index)


# %% minHeap implementation (2)
def insert_min_heap(heap, value):
    n = len(heap)
    heap.append(value)

    index = n
    while index > 0 and value < heap[[(index - 1) // 2]]:
        heap[index] = heap[(index - 1) // 2]
        index = (index - 1) // 2  # 더 작은 parent를 찾을 때까지 탐험을 지속

    heap[index] = value
