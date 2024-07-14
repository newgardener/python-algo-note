# https://leetcode.com/problems/open-the-lock

"""
TODO: 양방향 BFS를 적용한 solution에 대해서도 고민해봐야함
"""

from collections import deque


def openLock(deadends: list[str], target: str) -> int:
    def neighbors(state):
        for i in range(4):
            x = int(state[i])
            for d in (-1, 1):
                y = (x + d) % 10
                yield state[:i] + str(y) + state[i + 1 :]

    visited = set(deadends)
    # early-return condition
    if "0000" in visited:
        return -1

    # (start, turns)
    queue = deque([("0000", 0)])
    while queue:
        state, turns = queue.popleft()
        if state == target:
            return turns

        for next_state in neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, turns + 1))

    return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

print(openLock(deadends, target))
