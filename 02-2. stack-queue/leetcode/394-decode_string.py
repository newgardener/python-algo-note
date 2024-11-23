def decodeString(s: str) -> str:
    stack = []
    curr = ""
    k = 0
    for ch in s:
        if ch.isdigit():
            k = k * 10 + int(ch)
        elif ch == "[":
            stack.append((curr, k))
            curr, k = "", 0
        elif ch == "]":
            prev, repeat = stack.pop()
            curr = prev + repeat * curr
        else:
            curr += ch
    return curr
