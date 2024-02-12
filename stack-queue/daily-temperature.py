T = [73, 74, 75, 71, 69, 72, 76, 73]


def dailyTemperature(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer


print(dailyTemperature(T))
