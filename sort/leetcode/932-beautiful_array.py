from typing import List


def beautifulArray(n: int) -> List[int]:
    if n == 1:
        return [1]

    odd = beautifulArray((n + 1) // 2)
    even = beautifulArray(n // 2)

    return [num * 2 - 1 for num in odd] + [num * 2 for num in even]
