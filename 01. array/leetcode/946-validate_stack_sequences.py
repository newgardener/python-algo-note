from typing import List


def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    stack = []
    l = 0
    for i in range(len(pushed)):
        stack.append(pushed[i])
        while stack and stack[-1] == popped[l]:
            stack.pop()
            l += 1
    return not stack
