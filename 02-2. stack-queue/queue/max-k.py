from collections import deque
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result

    return wrapper


class Solution:
    """
    optimization needed:
    if newly added element is smaller than prev Max, it can be ignored
    """

    @timeit
    def myPrintMax(self, arr, k):
        # edge case
        if len(arr) < k:
            return None

        result = []
        q = deque(arr[0:k])
        for i in range(k, len(arr)):
            result.append(max(q))
            q.popleft()
            q.append(arr[i])

        result.append(max(q))
        return result

    @timeit
    def optimizedPrintMax(self, arr, k):
        dq = deque()
        result = []
        n = len(arr)

        # process first k elements
        for i in range(min(k, n)):
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)

        # process rest k ~ n elements
        for i in range(k, n):
            # append max num among prev 3 elements
            # first element of dq is the index of the largest element
            result.append(arr[dq[0]])

            # drop the index if it is not within current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()

            dq.append(i)

        result.append(arr[dq[0]])
        return result


if __name__ == "__main__":
    sol = Solution()

    print(sol.optimizedPrintMax([9, 7, 2, 4, 6, 8, 2, 11, 1], 3))
    print(sol.myPrintMax([9, 7, 2, 4, 6, 8, 2, 11, 1], 3))
