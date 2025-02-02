T = [73, 74, 75, 71, 69, 72, 76, 73]
"""
Time Complexity: O(N)
Space Complexity for stack: O(N)
Space Complexity for DP: O(1)
"""


def dailyTemperatureInOrder(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer


print(dailyTemperatureInOrder(T))

def dailyTemperatureInReversed(T):
    answer = [0] * len(T)
    stack = []
    for i in range(len(T)-1, -1, -1):
        temp = T[i]
        while stack and temp >= T[stack[-1]]:
            stack.pop()
        answer[i] = stack[-1] - i if stack else 0
        stack.append(i)
    return answer

print(dailyTemperatureInReversed(T))

def dailyTemperatureDP(T):
    n = len(T)
    answer = [0] * len(T)
    for i in range(n-2, -1, -1):
        j = i + 1
        while j < n and T[j] <= T[i]:
            if answer[j] == 0:
                j = n # in order to denote we don't need to update answer[i]
                break
            j += answer[j]

        if j < n:
            answer[i] = j - i
    return answer

print(dailyTemperatureDP(T))

