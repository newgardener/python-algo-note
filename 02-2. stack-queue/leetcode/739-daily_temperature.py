from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            tempIndex = stack.pop()
            res[tempIndex] = i - tempIndex
        stack.append(i)
    return res
