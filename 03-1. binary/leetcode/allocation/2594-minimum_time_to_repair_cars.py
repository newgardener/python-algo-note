def repairCars(ranks: list[int], cars: int) -> int:
    def can_repair_in_times(t):
        return sum(int((t // r) ** 0.5) for r in ranks) >= cars

    l, r = 1, min(ranks) * cars * cars
    while l < r:
        mid = l + (r - l) // 2
        # find minimum time to repair cars (leftmost search)
        if can_repair_in_times(mid):
            r = mid
        else:
            l = mid + 1
    return l
