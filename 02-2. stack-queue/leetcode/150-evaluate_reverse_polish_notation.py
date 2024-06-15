import math
from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if token == "+":
                stack.append(num1 + num2)
            elif token == "-":
                stack.append(num1 - num2)
            elif token == "*":
                stack.append(num1 * num2)
            else:
                res = math.trunc(num1 / num2)
                stack.append(res)
    return stack[-1]
