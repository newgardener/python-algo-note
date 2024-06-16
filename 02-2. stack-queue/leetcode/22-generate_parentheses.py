from typing import List


def generateParenthesis(n: int) -> List[str]:
    result = []

    def backtrack(left, right, s):
        if left == right == n:
            result.append(s)
        if left < n:
            backtrack(left + 1, right, s + "(")

        if right < left:
            backtrack(left, right + 1, s + ")")

    backtrack(0, 0, "")
    return result
