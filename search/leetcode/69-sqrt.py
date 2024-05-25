# https://leetcode.com/problems/sqrtx


def mySqrt(x: int) -> int:
    if x < 2:
        return x

    left, right = 2, x // 2
    while left <= right:
        mid = (left + right) // 2
        num = mid * mid
        if num == x:
            return mid
        if num > x:
            right = mid - 1
        elif num < x:
            left = mid + 1
    return right
