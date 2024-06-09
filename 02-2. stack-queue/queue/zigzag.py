from collections import deque


class Solution:
    def __init__(self, v1, v2):
        self.queue = deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self):
        length, iter = self.queue.popleft()
        value = next(iter)
        if length > 1:
            self.queue.append((length - 1, iter))
        return value

    def has_next(self):
        return bool(self.queue)


if __name__ == "__main__":
    sol = Solution([1, 2, 3], [4, 5])
    print(sol.next())
    print(sol.next())
    print(sol.next())
    print(sol.next())
    print(sol.next())
    print(sol.has_next())
