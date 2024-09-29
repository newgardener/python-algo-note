def maximumCandies(candies: list[int], k: int) -> int:
    total = sum(candies)
    if total < k:
        return 0

    l, r = 1, max(candies) + 1
    max_candy = 0
    while l < r:
        mid = l + (r - l) // 2
        piles = 0
        for candy in candies:
            piles += candy // mid
        if piles < k:
            r = mid
        else:
            # find maximum candy to allocate for k children (rightmost search)
            max_candy = max(max_candy, mid)
            l = mid + 1
    return max_candy
