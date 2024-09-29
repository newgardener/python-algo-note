def minimizedMaximum(n: int, quantities: list[int]) -> int:
    def can_distribute(max_q):
        stores = 0
        for q in quantities:
            stores += (q + max_q - 1) // max_q
        # there is a room to optimize max_q to be smaller
        return stores > n

    l, r = 1, max(quantities) + 1
    while l < r:
        mid = l + (r - l) // 2
        # find a minimized q which is sufficient to distribute to n stores
        # leftmost search to find a minimized q
        if can_distribute(mid):
            l = mid + 1
        else:
            r = mid
    return l
