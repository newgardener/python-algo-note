"""
Time Complexity: O(NlogN) -> sorting
Space Complexity: O(N) -> stack
"""


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    pairs = [[p, s] for p, s in zip(position, speed)]
    pairs.reverse()

    stack = []
    # iterate pairs in a position-descending order
    for p, s in pairs:
        slope = (target - p) / s
        # merge cars if prev_slope is smaller or equal to cur_slope
        # it means there would be a car fleet
        if not stack or stack[-1] < slope:
            stack.append(slope)

    # what remains in the stack is the distinct number of car fleet
    return len(stack)


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
