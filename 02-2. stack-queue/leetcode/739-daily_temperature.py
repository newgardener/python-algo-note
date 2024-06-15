from typing import List

"""
Monotonic Decreasing Stack
Time Complexity: O(N)
"""


def dailyTemperaturesMD(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            tempIndex = stack.pop()
            res[tempIndex] = i - tempIndex
        stack.append(i)
    return res


"""
Monotonic Increasing Stack
Time Complexity: O(N)
"""


def dailyTemperaturesMI(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures) - 1, -1, -1):
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            stack.pop()
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res
