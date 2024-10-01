from collections import Counter
import math


def numRabbits(answers: list[int]) -> int:
    rabbits = 0

    counts = Counter(answers)
    for key, val in counts.items():
        # number of same-colored rabbits
        num = key + 1
        if val <= num:
            rabbits += num
        # if val is greater than num, it means we should add groups => math.ceil(val / num)
        else:
            rabbits += math.ceil(val / num) * num

    return rabbits

