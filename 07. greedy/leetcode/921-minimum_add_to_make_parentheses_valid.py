def minAddToMakeValid(s: str) -> int:
    add = 0
    stack = []
    for ch in s:
        if not stack or ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] == ")":
                add += 1
            elif stack[-1] == "(":
                stack.pop()
    return add + len(stack)


def minAddToMakeValid(s: str) -> int:
    left_balance = 0
    right_balance = 0

    for ch in s:
        if ch == "(":
            left_balance += 1
        elif ch == ")":
            if left_balance > 0:
                left_balance -= 1
            else:
                right_balance += 1
    return left_balance + right_balance
