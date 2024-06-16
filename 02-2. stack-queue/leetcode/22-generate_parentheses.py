from typing import List


def generateParenthesis(n: int) -> List[str]:
    result = []
    stack = []

    def backtrack(left, right):
        if left == right == n:
            result.append("".join(stack))
        if left < n:
            stack.append("(")
            backtrack(left + 1, right)
            stack.pop()

        if right < left:
            stack.append(")")
            backtrack(left, right + 1)
            stack.pop()

    backtrack(0, 0)
    return result
