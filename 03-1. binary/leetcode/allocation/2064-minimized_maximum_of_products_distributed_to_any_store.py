"""
given N is length of quantities and M is max(quantities),
Time Complexity: O(NlogM)
Space Complexity: O(1)
"""

def minimizedMaximum(n: int, quantities: list[int]) -> int:
    def can_distribute(max_q):
        stores_needed = 0
        for q in quantities:
            stores_needed += (q + max_q - 1) // max_q  # ceil(q / max_q)
            if stores_needed > n:
                return False
        return stores_needed <= n

    l, r = 1, max(quantities)
    while l < r:
        mid = l + (r - l) // 2
        if can_distribute(mid):
            r = mid
        else:
            l = mid + 1


