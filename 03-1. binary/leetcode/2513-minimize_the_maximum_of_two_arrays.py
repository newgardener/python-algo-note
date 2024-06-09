def minimizeSet(divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    lcm = divisor1 * divisor2 // gcd(divisor1, divisor2)
    start, end = uniqueCnt1 + uniqueCnt2, divisor1 * uniqueCnt1 * divisor2 * uniqueCnt2

    while start <= end:
        mid = (start + end) // 2
        counter1 = mid - mid // divisor1
        counter2 = mid - mid // divisor2
        commonCounter = mid - mid // lcm
        if (
            counter1 >= uniqueCnt1
            and counter2 >= uniqueCnt2
            and commonCounter >= uniqueCnt1 + uniqueCnt2
        ):
            end = mid - 1
        else:
            start = mid + 1

    return start
