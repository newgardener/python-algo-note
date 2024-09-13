# https://leetcode.com/problems/compare-version-numbers

# %%


def compareVersion(version1: str, version2: str) -> int:
    def filterZero(str):
        arr = str.split(".")
        return list(map(lambda x: int(x), arr))

    split1, split2 = filterZero(version1), filterZero(version2)
    l1, l2 = len(split1), len(split2)
    length = l2 if l1 >= l2 else l1

    result = 0
    for i in range(length):
        c1, c2 = split1[i], split2[i]
        if c1 > c2:
            return 1
        if c1 < c2:
            return -1

    if l1 >= l2:
        rest = int("".join(str(num) for num in split1[length:]))
        return 1 if rest > 0 else 0

    if l1 < l2:
        rest = int("".join(str(num) for num in split2[length:]))
        return -1 if rest > 0 else 0


# %%
def compareVersion(version1: str, version2: str) -> int:
    def preprocess(version):
        return list(map(lambda char: int(char), version.split(".")))

    part1, part2 = preprocess(version1), preprocess(version2)

    while len(part1) < len(part2):
        part1.append(0)

    while len(part2) < len(part1):
        part2.append(0)

    for p1, p2 in zip(part1, part2):
        if p1 > p2:
            return 1
        if p1 < p2:
            return -1
    return 0
