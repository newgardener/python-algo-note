from typing import List


def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    i, j = 0, 0
    stack = []
    while i < len(pushed) and j < len(popped):
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1

        stack.append(pushed[i])
        i += 1

    while stack and stack[-1] == popped[j]:
        stack.pop()
        j += 1

    return i == len(pushed) and j == len(popped)






