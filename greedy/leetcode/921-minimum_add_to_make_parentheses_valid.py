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
