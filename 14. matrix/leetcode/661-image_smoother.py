def imageSmoother(img: list[list[int]]) -> list[list[int]]:
    m, n = len(img), len(img[0])

    def apply_filter(r, c):
        total = cnt = 0
        top = max(0, r - 1)
        bottom = min(m, r + 2) # in order to include r + 1
        left = max(0, c - 1)
        right = min(n, c + 2) # in order to include c + 1

        for r in range(top, bottom):
            for c in range(left, right):
                total += img[r][c]
                cnt += 1
        return total // cnt

    return [[apply_filter(r, c) for c in range(n)] for r in range(m)]
